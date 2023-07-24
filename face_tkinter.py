import sys
import os
import Tkinter
import tkMessageBox

top=Tkinter.Tk()

def register():
	os.system('python dataSetGenerator.py')
	os.system('python extract_embeddings.py --dataset dataset --embeddings output/embeddings.pickle --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7')
	os.system('python train_model.py --embeddings output/embeddings.pickle --recognizer output/recognizer.pickle --le output/le.pickle')

def identify():
	os.system('python recognize_video.py --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le output/le.pickle')

B1=Tkinter.Button(top,text="Register",command= register)
B2=Tkinter.Button(top,text="Identify",command = identify)

B1.grid(row=0, column=0)
B2.grid(row=1, column=1)

top.mainloop()
