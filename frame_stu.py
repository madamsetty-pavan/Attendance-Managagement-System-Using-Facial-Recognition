from tkinter import *
import os
import sys
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox

main_window=Tk()
main_window.title('Attendance Management System - Student')
main_window.minsize(400,400)
main_window.geometry('500x500')

global show_attn
#show_attn = Toplevel()
#show_attn.withdraw()

def hide_frames():
    f1.place_forget()
    student_home_f.place_forget()

def student_login():
    conn = sqlite3.connect('DBdemo.db')
    c = conn.cursor()

    temp_user_id = student_id_f1.get()
    temp_password = student_password_f1.get()

    c.execute("SELECT student_user_id from students_demo")
    student_ids=c.fetchall()

    name_flag=0
    for rec in student_ids:
        if(str(rec[0])==str(temp_user_id)):
            name_flag=1
    
    if(name_flag==0):
        messagebox.showerror("Error !","This User ID does not exist")

        conn.commit()
        conn.close()

        hide_frames()
        f1.tkraise()
        student_id_f1.delete(0, END)
        student_password_f1.delete(0, END)
        f1.place(relx=0.5, rely=0.5, anchor=CENTER)
    else:
        c.execute("SELECT student_password from students_demo WHERE student_user_id = ?", (temp_user_id,))
        rec_password = str(c.fetchone()[0])
        conn.commit()
        conn.close()
  
        if(rec_password != temp_password and name_flag==1):
            messagebox.showerror("Error !","The password is incorrect ! Try again.")
            hide_frames()
            f1.tkraise()
            student_id_f1.delete(0, END)
            student_password_f1.delete(0, END)
            f1.place(relx=0.5, rely=0.5, anchor=CENTER)
        elif(rec_password == temp_password and name_flag==1):
            hide_frames()
            student_home_f.tkraise()
            student_home_f.place(relx=0.5, rely=0.5, anchor=CENTER)



def student_identify():
    student_name = student_id_f1.get()
    os.system('python recognize_video.py --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le output/le.pickle --userid ' + student_name)

    hide_frames()
    student_home_f.tkraise()
    student_home_f.place(relx=0.5, rely=0.5, anchor=CENTER)

def show_student_records():
    global show_attn

    show_attn = Toplevel()
    show_attn.title('My Attendance details')
    show_attn.minsize(400,400)
    show_attn.geometry('400x600')

    list_of_labels = list()
    list_of_attn_labels = list()
    present = list()
    attn_rec = list()

    student_name = student_id_f1.get()

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

    k=0
    for col3 in range(len(col_names)-1):
    #    print(k)
        attn_rec.append(str(stu_recs_show_attn[0][k+2]))
        k+=1

    i=1
    for col in range(len(col_names)-1):
        list_of_labels.append(Label(show_attn, text=str(col_names[i][0])))
        list_of_attn_labels.append(Label(show_attn, text=attn_rec[i-1]))
        i+=1
    
    j=0
    for col2 in range(len(col_names)-1):
        list_of_labels[j].grid(row=j+1, column=0, padx=20, pady=10)
        list_of_attn_labels[j].grid(row=j+1, column=1, padx=2, pady=10)
        if(stu_recs_show_attn[0][j+2]==1):
            present.append(col_names[j+1][0])
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

    stu_attn_back_btn = Button(show_attn, text="Back to home", command=back_show_attn)
    stu_attn_back_btn.grid(row=i+2, column=0, pady=(10,0), columnspan=2)

    #hide_frames()
#    show_attn_f.tkraise()
#    show_attn_f.place(relx=0.5, rely=0.5, anchor=CENTER)
    
def back_show_attn():
    global show_attn
    
    hide_frames()
    show_attn.destroy()
    student_home_f.tkraise()
    student_home_f.place(relx=0.5, rely=0.5, anchor=CENTER)

def stu_logout():
    hide_frames()
    f1.tkraise()
    student_id_f1.delete(0, END)
    student_password_f1.delete(0, END)
    f1.place(relx=0.5, rely=0.5, anchor=CENTER)

f1=Frame(main_window)
student_id_f1 = Entry(f1, width=30)
student_id_f1.grid(row=0, column=1, padx=20, pady=(150,0))
student_password_f1 = Entry(f1, show="*", width=30)
student_password_f1.grid(row=1, column=1, padx=20, pady=10)

#Create text box labels
student_user_id_label_f1 = Label(f1, text="Student id")
student_user_id_label_f1.grid(row=0, column=0, pady=(150,0))

student_password_label_f1 = Label(f1, text="Password")
student_password_label_f1.grid(row=1, column=0, pady=10)

#Buttons
student_login_btn_f1 = Button(f1, text="Login", command=student_login)
student_login_btn_f1.grid(row=2, column=1, padx=10, pady=20)

f1.place(relx=0.5, rely=0.5, anchor=CENTER)


student_home_f = Frame(main_window)
student_mark_attn_btn = Button(student_home_f, text="Give my Attendance", command=student_identify)
student_mark_attn_btn.grid(row=0, column=0, pady=(150,0), padx=100)
student_attn_recs_btn = Button(student_home_f, text="Check my attendance", command=show_student_records)
student_attn_recs_btn.grid(row=1, column=0, pady=20, padx=100)
student_logout_btn = Button(student_home_f, text="Log Out", command=stu_logout)
student_logout_btn.grid(row=2, column=0, pady=20, padx=100)

main_window.mainloop()