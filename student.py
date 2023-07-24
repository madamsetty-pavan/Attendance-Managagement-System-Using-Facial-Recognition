from tkinter import *
import os
import sys
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox


root = Tk()
root.title('Student attendance')
root.minsize(400,400)
root.geometry('400x400')

global student_user_id
global student_password
global student_login_btn

def student_login():
    global student_user_id
    global student_name

    conn = sqlite3.connect('DBdemo.db')
    c = conn.cursor()

    temp_user_id = student_user_id.get()
    temp_password = student_password.get()

    student_name = student_user_id.get()

    #print(temp_password)

    c.execute("SELECT student_password from students_demo WHERE student_user_id = ?", (temp_user_id,))
    rec_password = str(c.fetchone()[0])
    #print(rec_password)

    conn.commit()
    conn.close()
  
    if(rec_password != temp_password):
        messagebox.showerror("Error !","Either Student usr_id or password is incorrect")
    elif(rec_password == temp_password):
        student_home()

def student_home():
    global student_mark_attn_btn
    global student_attn_recs_btn
    global student_user_id
    global student_password
    global student_login_btn

    student_password.grid_forget()
    student_user_id.grid_forget()
    student_login_btn.grid_forget()

    student_mark_attn_btn = Button(root, text="Give my Attendance", command=student_identify)
    student_mark_attn_btn.grid(row=0, column=0, pady=(150,0), padx=100)
    student_attn_recs_btn = Button(root, text="Check my attendance", command=show_student_records)
    student_attn_recs_btn.grid(row=1, column=0, pady=20, padx=100)

def student_identify():
    global student_name

    os.system('python recognize_video.py --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le output/le.pickle --userid ' + student_name)

def show_student_records():
    show_attn = Tk()
    show_attn.title('My Attendance details')
    show_attn.minsize(400,400)
    show_attn.geometry('400x400')

    global list_of_labels
    global list_of_textboxes
    global student_user_id_show_attn
    global student_user_id_show_attn_lbl
    global student_name
    global present

    list_of_labels = list()
    list_of_textboxes = list()
    present = list()

    conn = sqlite3.connect('DBdemo.db')
    c = conn.cursor()

    c.execute("SELECT oid, * from student_att WHERE student_user_id = ?",(student_name,)) 
    stu_recs_show_attn = c.fetchall()

    c.execute("SELECT name FROM PRAGMA_TABLE_INFO('student_att')")
    col_names = c.fetchall()

    conn.commit()
    conn.close()

    student_user_id_show_attn = Entry(show_attn, width=30)
    student_user_id_show_attn.grid(row=0, column=1, padx=20, pady=(10,0))
    for record4 in stu_recs_show_attn:
        if(str(record4[1])==str(student_name)):
            student_user_id_show_attn.insert(0, record4[1])
    student_user_id_show_attn.config(state=DISABLED)

    student_user_id_show_attn_lbl = Label(show_attn, text="Student id : ")
    student_user_id_show_attn_lbl.grid(row=0, column=0, padx=10, pady=(10,0))

    i=1
    for col in range(len(col_names)-1):
        list_of_labels.append(Label(show_attn, text=str(col_names[i][0])))
        list_of_textboxes.append(Entry(show_attn, width=10))
        i+=1
    
    j=0
    for col2 in range(len(col_names)-1):
        list_of_labels[j].grid(row=j+1, column=0, padx=20, pady=10)
        list_of_textboxes[j].grid(row=j+1, column=1, padx=2, pady=10)
        list_of_textboxes[j].insert(0, stu_recs_show_attn[0][j+2])
        if(stu_recs_show_attn[0][j+2]==1):
            present.append(col_names[j+1][0])
        list_of_textboxes[j].config(state=DISABLED)
        j+=1

    no_present = len(present)
    no_min = len(col_names)-1
    till_now = (no_present/float(no_min))*100
    whole = (float(no_present)/60)*100

    #Create text box labels5
    stu_attn_till_now = Label(show_attn, text="My attendance till now - "+str(round(till_now,2))+"%")
    stu_attn_till_now.grid(row=i, column=0, pady=(10,0), columnspan=2)
    #Create text box labels5
    stu_attn_whole = Label(show_attn, text="My attendance on the whole - "+str(round(whole,2))+"%")
    stu_attn_whole.grid(row=i+1, column=0, pady=(10,0), columnspan=2)

#Create text boxes
student_user_id = Entry(root, width=30)
student_user_id.grid(row=0, column=1, padx=20, pady=(150,0))

student_password = Entry(root, show="*", width=30)
student_password.grid(row=1, column=1, padx=20, pady=10)

#Create text box labels
student_user_id_label = Label(root, text="Student id")
student_user_id_label.grid(row=0, column=0, pady=(150,0))

student_password_label = Label(root, text="Password")
student_password_label.grid(row=1, column=0, pady=10)

#Buttons
student_login_btn = Button(root, text="Login", command=student_login)
student_login_btn.grid(row=2, column=1, padx=10, pady=20)

root.mainloop()