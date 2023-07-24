# USAGE
# python recognize_video.py --detector face_detection_model \
#	--embedding-model openface_nn4.small2.v1.t7 \
#	--recognizer output/recognizer.pickle \
#	--le output/le.pickle

# python recognize_video.py --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le output/le.pickle

# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
from tkinter import messagebox
import numpy as np
import datetime
import sqlite3
import argparse
import imutils
import pickle
import time
import cv2
import sys
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--detector", required=True,
	help="path to OpenCV's deep learning face detector")
ap.add_argument("-m", "--embedding-model", required=True,
	help="path to OpenCV's deep learning face embedding model")
ap.add_argument("-r", "--recognizer", required=True,
	help="path to model trained to recognize faces")
ap.add_argument("-l", "--le", required=True,
	help="path to label encoder")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
	help="minimum probability to filter weak detections")
ap.add_argument("-n", "--userid", required=True, 
	help="user_id to search for")
args = vars(ap.parse_args())

global q1
q1=''
#mark_attendance definition
def mark_attendance():
	global user_name
	global min
	global col_names2
	global q1

	q1=''

	min1="min"+str(min)
	user_name1="(u'"+user_name+"',)"

	q1="INSERT INTO student_att ("

	conn = sqlite3.connect('DBdemo.db')
	c = conn.cursor()
	
	c.execute("SELECT oid, * from student_att") 
	stu_recs = c.fetchall()
	stu_names = stu_recs
	
	c.execute("SELECT name FROM PRAGMA_TABLE_INFO('student_att')")
	col_names = c.fetchall()
	col_names2=col_names

	c1=0
	min_flag=0
	for c1 in range(len(col_names)):
		if(c1==(len(col_names)-1)):
			q1+=str(col_names[c1][0])
		else:
			q1+=str(col_names[c1][0])+","
		if(str(col_names[c1][0])==str(min1)):
			min_flag=1
		c1+=1

	q1+=") values (?,"
	val=list()
	val.append(str(user_name))

	for c2 in range((len(col_names)-1)):
		if(c2==(len(col_names)-2)):
			q1+="?"
			val.append(0)
		else:
			q1+="?,"
			val.append(0)

	q1+=")"

	name_flag=0
	for name in stu_recs:
		if(str(name[1])==str(user_name)):
			name_flag=1

	if(min_flag==1 and name_flag==1):
		print "min found name found"
		c.execute("UPDATE student_att SET "+str(col_names[col])+" = 1 WHERE student_user_id = ?", (user_name,))
	if(name_flag!=1 and min_flag!=1):
		print "name not found and min not found"
		c.execute(q1,val)
		c.execute("ALTER TABLE student_att ADD COLUMN "+str(min1)+" INT DEFAULT 0")
		c.execute("UPDATE student_att SET "+str(min1)+" = 1 WHERE student_user_id = ?", (user_name,))
	if(min_flag!=1 and name_flag==1):
		print "min not found but name found"
		c.execute("ALTER TABLE student_att ADD COLUMN "+str(min1)+" INT DEFAULT 0")
		c.execute("UPDATE student_att SET "+str(min1)+" = 1 WHERE student_user_id = ?", (user_name,))
	if(min_flag==1 and name_flag!=1):
		print "min found but name not found"
		c.execute(q1,val)
		c.execute("UPDATE student_att SET "+str(min1)+" = 1 WHERE student_user_id = ?", (user_name,))
	
	conn.commit()
	conn.close()

#read the userid from argparse
global user_name

user_name=str(args["userid"])

#get the time as minutes value
global min
now1 = datetime.datetime.now()
min=now1.strftime("%M")
proba=0

# load our serialized face detector from disk
print("[INFO] loading face detector...")
protoPath = os.path.sep.join([args["detector"], "deploy.prototxt"])
modelPath = os.path.sep.join([args["detector"],
	"res10_300x300_ssd_iter_140000.caffemodel"])
detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)

# load our serialized face embedding model from disk
print("[INFO] loading face recognizer...")
embedder = cv2.dnn.readNetFromTorch(args["embedding_model"])

# load the actual face recognition model along with the label encoder
recognizer = pickle.loads(open(args["recognizer"], "rb").read())
le = pickle.loads(open(args["le"], "rb").read())

# initialize the video stream, then allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

# start the FPS throughput estimator
fps = FPS().start()

# loop over frames from the video file stream
while True:
	# grab the frame from the threaded video stream
	frame = vs.read()

	# resize the frame to have a width of 600 pixels (while
	# maintaining the aspect ratio), and then grab the image
	# dimensions
	frame = imutils.resize(frame, width=600)
	(h, w) = frame.shape[:2]

	# construct a blob from the image
	imageBlob = cv2.dnn.blobFromImage(
		cv2.resize(frame, (300, 300)), 1.0, (300, 300),
		(104.0, 177.0, 123.0), swapRB=False, crop=False)

	# apply OpenCV's deep learning-based face detector to localize
	# faces in the input image
	detector.setInput(imageBlob)
	detections = detector.forward()

	# loop over the detections
	for i in range(0, detections.shape[2]):
		# extract the confidence (i.e., probability) associated with
		# the prediction
		confidence = detections[0, 0, i, 2]

		# filter out weak detections
		if confidence > args["confidence"]:
			# compute the (x, y)-coordinates of the bounding box for
			# the face
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			# extract the face ROI
			face = frame[startY:endY, startX:endX]
			(fH, fW) = face.shape[:2]

			# ensure the face width and height are sufficiently large
			if fW < 20 or fH < 20:
				continue

			# construct a blob for the face ROI, then pass the blob
			# through our face embedding model to obtain the 128-d
			# quantification of the face
			faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
				(96, 96), (0, 0, 0), swapRB=True, crop=False)
			embedder.setInput(faceBlob)
			vec = embedder.forward()

			# perform classification to recognize the face
			preds = recognizer.predict_proba(vec)[0]
			j = np.argmax(preds)
			proba = preds[j]
			name = le.classes_[j]

			# draw the bounding box of the face along with the
			# associated probability
			text = "{}: {:.2f}%".format(name, proba * 100)
			y = startY - 10 if startY - 10 > 10 else startY + 10
			cv2.rectangle(frame, (startX, startY), (endX, endY),
				(0, 0, 255), 2)
			cv2.putText(frame, text, (startX, y),
				cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
			#if(proba*100>90 and name==user_name):
			#	mark_attendance()
			#	break

	# update the FPS counter
	fps.update()

	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	
	if(proba*100 >90 and name==user_name):
		print('Dear ',name,', your attendance has been marked')
		messagebox.showinfo("Message","Dear "+name+ ", your attendance has been marked for "+str(min1))
		mark_attendance()
		break

	# if the `q` key was pressed, break from the loop
	#if key == ord("q"):
	#	break

# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
