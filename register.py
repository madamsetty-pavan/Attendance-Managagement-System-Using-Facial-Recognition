from tkinter import *
import os
import sys
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox


root = Tk()
root.title('Admin Register')
root.minsize(400,400)
root.geometry('400x600')

#Create admin function
def admin_register():
    global admin_user_id_label
    global admin_user_id
    global admin_password_label
    global admin_password
    global admin_login_btn
    global admin_register_btn
    global admin_submit_btn

    admin_user_id_label.grid_forget()
    admin_user_id.grid_forget()
    admin_password_label.grid_forget()
    admin_password.grid_forget()
    admin_login_btn.grid_forget()
    admin_register_btn.grid_forget()

    #Create text boxes
    admin_user_id = Entry(root, width=30)
    admin_user_id.grid(row=0, column=1, padx=20, pady=(150,0))

    admin_password = Entry(root, show="*", width=30)
    admin_password.grid(row=1, column=1, padx=20, pady=10)

    #Create text box labels
    admin_user_id_label = Label(root, text="Admin id")
    admin_user_id_label.grid(row=0, column=0, pady=(150,0))

    admin_password_label = Label(root, text="Password")
    admin_password_label.grid(row=1, column=0, pady=10)

    #Buttons
    admin_submit_btn = Button(root, text="Submit", command=admin_submit)
    admin_submit_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

def admin_submit():
    global admin_user_id_label
    global admin_user_id
    global admin_password_label
    global admin_password
    global admin_login_btn
    global admin_register_btn
    global admin_submit_btn
    # Database

    #create database or connect to one
    conn = sqlite3.connect('DBdemo.db')

    #create cursor
    c = conn.cursor()

    #insert into table
    c.execute("INSERT INTO addresses VALUES (:admin_user_id, :admin_password)",
        {
            'admin_user_id': admin_user_id.get(),
            'admin_password': admin_password.get()
        }  
    )

    #Commit changes
    conn.commit()

    #Close connection
    conn.close()

    admin_submit_btn.grid_forget()

    #Create text boxes
    admin_user_id = Entry(root, width=30)
    admin_user_id.grid(row=0, column=1, padx=20, pady=(150,0))

    admin_password = Entry(root, show="*", width=30)
    admin_password.grid(row=1, column=1, padx=20, pady=10)

    #Create text box labels
    admin_user_id_label = Label(root, text="Admin id")
    admin_user_id_label.grid(row=0, column=0, pady=(150,0))

    admin_password_label = Label(root, text="Password")
    admin_password_label.grid(row=1, column=0, pady=10)

    #Buttons
    admin_login_btn = Button(root, text="Login", command=admin_login)
    admin_login_btn.grid(row=2, column=1, padx=10, pady=20)

def admin_login():

    global admin_user_id_label
    global admin_user_id
    global admin_password_label
    global admin_password
    global admin_login_btn
    global admin_register_btn
    global admin_submit_btn

    admin_user_id.grid_forget()
    admin_password.grid_forget()
    
    conn = sqlite3.connect('DBdemo.db')
    c = conn.cursor()

    temp_user_id = admin_user_id.get()
    temp_password = admin_password.get()

    #print(temp_password)

    c.execute("SELECT admin_password from addresses WHERE admin_user_id = ?", (temp_user_id,))
    rec_password = str(c.fetchone()[0])
    #print(rec_password)

    conn.commit()
    conn.close()
  
    if(rec_password != temp_password):
        messagebox.showerror("Error !","Either the usr_id or password is incorrect ! Try again.")
    elif(rec_password == temp_password):
        admin_home(5)

def admin_home(num):
    global admin_user_id_label
    global admin_user_id
    global admin_password_label
    global admin_password
    global admin_login_btn
    global admin_register_btn
    global add_student_btn
    global show_student_records_btn
    global remove_student_btn
    global modify_student_btn
    global modify_student_attn_btn

    if(num==1):
        global face_id_inst1
        global face_id_inst2
        global face_id_inst3
        global student_face_id_btn

        face_id_inst1.grid_forget()
        face_id_inst2.grid_forget()
        face_id_inst3.grid_forget()
        student_face_id_btn.grid_forget()
    
    elif(num==2):
        global student_remove_id_label
        global student_remove_id
        global student_remove_id_btn

        student_remove_id.grid_forget()
        student_remove_id_btn.grid_forget()
        student_remove_id_label.grid_forget()

    elif(num==3):
        global student_modify_id
        global student_modify_id_label
        global student_modify_id_btn
        global student_update_faceid_btn

        student_modify_id.grid_forget()
        student_modify_id_btn.grid_forget()
        student_modify_id_label.grid_forget()
        student_update_faceid_btn.grid_forget()
    
    elif(num==4):
        global student_user_id_attn_modify
        global student_user_id_label_attn_modify
        global student_attn_modify_btn

        student_attn_modify_btn = Button(root, text="Modify the attendance")

        student_user_id_label_attn_modify.grid_forget()
        student_user_id_attn_modify.grid_forget()
        student_attn_modify_btn.grid_forget()

    admin_user_id_label.grid_forget()
    admin_user_id.grid_forget()
    admin_password_label.grid_forget()
    admin_password.grid_forget()
    admin_login_btn.grid_forget()
    admin_register_btn.grid_forget()
    #face_id_inst1.grid_forget()
    #face_id_inst2.grid_forget()
    #face_id_inst3.grid_forget()
    #student_face_id_btn.grid_forget()

    add_student_btn = Button(root, text="Add Student", command=student_enlist)
    add_student_btn.grid(row=0, column=0, pady=(50,20), padx=50)
    show_student_records_btn = Button(root, text="Show all records", command=show_student_records)
    show_student_records_btn.grid(row=1, column=0, pady=20, padx=50)
    remove_student_btn = Button(root, text="Remove Student record", command=student_remove)
    remove_student_btn.grid(row=2, column=0, pady=20, padx=50)
    modify_student_btn = Button(root, text="Modify Student record", command=student_modify)
    modify_student_btn.grid(row=3, column=0, pady=20, padx=50)
    modify_student_attn_btn = Button(root, text="Modify Student attendance", command=attn_modify)
    modify_student_attn_btn.grid(row=4, column=0, pady=20, padx=50)

def student_enlist():
    global admin_user_id_label
    global admin_user_id
    global admin_password_label
    global admin_password
    global admin_login_btn
    global admin_register_btn
    global add_student_btn
    global show_student_records_btn
    global remove_student_btn
    global student_user_id
    global student_password
    global student_password_label
    global student_user_id_label
    global modify_student_btn
    global modify_student_attn_btn
    global student_register_btn

    admin_user_id_label.grid_forget()
    admin_user_id.grid_forget()
    admin_password_label.grid_forget()
    admin_password.grid_forget()
    admin_login_btn.grid_forget()
    admin_register_btn.grid_forget()
    add_student_btn.grid_forget()
    show_student_records_btn.grid_forget()
    remove_student_btn.grid_forget()
    modify_student_btn.grid_forget()
    modify_student_attn_btn.grid_forget()

    student_user_id = Entry(root, width=30)
    student_user_id.grid(row=0, column=1, padx=20, pady=(150,0))

    student_password = Entry(root, show="*", width=30)
    student_password.grid(row=1, column=1, padx=20, pady=10)

    #Create text box labels5
    student_user_id_label = Label(root, text="Student User id")
    student_user_id_label.grid(row=0, column=0, pady=(150,0))

    student_password_label = Label(root, text="Password")
    student_password_label.grid(row=1, column=0, pady=10)

    student_register_btn = Button(root, text="Register", command=student_register)
    student_register_btn.grid(row=2, column=0,columnspan=2, padx=10, pady=20)

def student_register():
    
    global student_user_id
    global student_user_id_label
    global student_password
    global student_password_label
    global student_name
    global student_register_btn
    global face_id_inst1
    global face_id_inst2
    global face_id_inst3
    global student_face_id_btn

    student_user_id.grid_forget()
    student_user_id_label.grid_forget()
    student_password_label.grid_forget()
    student_password.grid_forget()
    student_register_btn.grid_forget()

    student_name = student_user_id.get()

    conn = sqlite3.connect('DBdemo.db')
    c = conn.cursor()

    c.execute("INSERT INTO students_demo VALUES (:student_user_id, :student_password)",
        {
            'student_user_id': student_user_id.get(),
            'student_password': student_password.get()
        }  
    )

    conn.commit()
    conn.close()

    face_id_inst1 = Label(root, text="Welcome " + student_name + "!")
    face_id_inst1.grid(row=1, column=0, padx=20, pady=(150,0))

    face_id_inst2 = Label(root, text="Your record has been added to our database")
    face_id_inst2.grid(row=2, column=0, padx=20, pady=10)

    face_id_inst3 = Label(root, text="To create your unique face_id, click on the below button.")
    face_id_inst3.grid(row=3, column=0, padx=20, pady=10)
    
    student_face_id_btn = Button(root, text="Create Face ID", command=student_face_id)
    student_face_id_btn.grid(row=4, column=0, padx=20, pady=30)

def student_face_id():
    global student_name

    os.system('python dataSetGenerator.py ' + student_name)
    os.system('python extract_embeddings.py --dataset dataset --embeddings output/embeddings.pickle --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7')
    os.system('python train_model.py --embeddings output/embeddings.pickle --recognizer output/recognizer.pickle --le output/le.pickle')

    messagebox.showinfo("Message","Face id for "+student_name+" has been successfully created.")

    admin_home(1)    

def student_remove():
    global student_remove_id
    global student_remove_id_label
    global student_remove_id_btn
    global add_student_btn
    global show_student_records_btn
    global remove_student_btn
    global modify_student_btn
    global modify_student_attn_btn
    global student_remove_id_label
    global student_remove_id
    global student_remove_id_btn

    add_student_btn.grid_forget()
    remove_student_btn.grid_forget()
    show_student_records_btn.grid_forget()
    modify_student_btn.grid_forget()
    modify_student_attn_btn.grid_forget()

    student_remove_id_label = Label(root, text="Student id")
    student_remove_id_label.grid(row=0, column=0, padx=20, pady=(150,0))

    student_remove_id = Entry(root,width=30)
    student_remove_id.grid(row=0, column=1, padx=20, pady=(150,0))

    student_remove_id_btn = Button(root, text="Remove", command=studentid_remove)
    student_remove_id_btn.grid(row=1, column=1, padx=20, pady=50)

def studentid_remove():
    global temp_studentid
    global temp2_studentid

    temp_studentid = student_remove_id.get()
    
    conn = sqlite3.connect('DBdemo.db')
    c = conn.cursor()

    c.execute("SELECT student_user_id from students_demo")
    student_userids = c.fetchall()
    
    i=0
    stu_flag_id=0
    for stu_id in student_userids:
        if(str(temp_studentid)==str(student_userids[i][0])):
            stu_id_flag=1
    
    if(stu_id_flag!=1):
        messagebox.showerror("Error !","Given Student id doesn't exist ! Try again.")
    else:
        c.execute("DELETE * from students_demo WHERE student_user_id = ?", (temp_studentid,))
        messagebox.showinfo("Message","The record with given Student_id"+temp_studentid+ "has been deleted")

    conn.commit()
    conn.close()
 
    dS = "/home/aman/Desktop/1951/Python/opencv-face-recognition/op3/dataset"
    dataSet_path = os.path.join(dS, temp_studentid)
    os.remove(dataSet_path)

    admin_home(2)

def student_modify():
    global student_modify_id
    global student_modify_id_label
    global student_modify_id_btn
    global student_update_faceid_btn
    global add_student_btn
    global show_student_records_btn
    global remove_student_btn
    global modify_student_btn
    global modify_student_attn_btn

    add_student_btn.grid_forget()
    remove_student_btn.grid_forget()
    show_student_records_btn.grid_forget()
    modify_student_btn.grid_forget()
    modify_student_attn_btn.grid_forget()

    student_modify_id_label = Label(root, text="Student id")
    student_modify_id_label.grid(row=0, column=0, padx=20, pady=(150,0))

    student_modify_id = Entry(root,width=30)
    student_modify_id.grid(row=0, column=1, padx=20, pady=(150,0))

    student_modify_id_btn = Button(root, text="Modify", command=studentid_modify)
    student_modify_id_btn.grid(row=1, column=0, padx=20, pady=50)

    student_update_faceid_btn = Button(root, text="Update Face id", command=update_face_id)
    student_update_faceid_btn.grid(row=1, column=1, padx=20, pady=50)

def studentid_modify():
    global modify

    modify = Tk()
    modify.title('Modify Student record')
    modify.minsize(400,400)
    modify.geometry('400x400')

    global student_user_id_modify
    global student_user_id_label_modify
    global student_new_pwd_label
    global student_new_pwd
    global student_new_pwd_confirm_label
    global student_new_pwd_confirm
    global student_modify_id
    global stu_name

    stu_name = student_modify_id.get()

    conn = sqlite3.connect('DBdemo.db')
    c = conn.cursor()

    c.execute("SELECT oid, * from student_att WHERE student_user_id = ?", (stu_name,)) 
    stu_recs = c.fetchall()

    conn.commit()
    conn.close()

    student_user_id_modify = Entry(modify, width=30)
    student_user_id_modify.grid(row=0, column=1, padx=20, pady=(150,0))

    #Create text box labels5
    student_user_id_label_modify = Label(modify, text="Student User id")
    student_user_id_label_modify.grid(row=0, column=0, pady=(150,0))

    student_new_pwd_label = Label(modify, text="New Password")
    student_new_pwd_label.grid(row=1, column=0, pady=10)

    student_new_pwd_confirm_label = Label(modify, text="Confirm new Password")
    student_new_pwd_confirm.grid(row=2, column=0, pady=10)

    student_new_pwd = Entry(modify, show="*", width=30)
    student_new_pwd.grid(row=1, column=1, padx=20, pady=10)

    student_new_pwd_confirm = Entry(modify, show="*", width=30)
    student_new_pwd_confirm.grid(row=2, column=1, pady=10)

    for record in range(len(stu_recs)):
        if(str(stu_recs[record][1])==str(stu_name)):
            student_user_id_modify.insert(0, stu_recs[record][1])

    student_register_btn_modify = Button(modify, text="Submit", command=student_det_modify)
    student_register_btn_modify.grid(row=2, column=0,columnspan=2, padx=10, pady=20)

def student_det_modify():
    global student_user_id_modify
    global student_new_pwd
    global student_new_pwd_confirm
    global student_id
    global student_pwd
    global student_pwd2

    student_id = student_user_id_modify.get()
    student_pwd = student_new_pwd.get()
    student_pwd2 = student_new_pwd_confirm.get()

    if(str(student_pwd)!=str(student_pwd2)):
        messagebox.showerror("Error !","The two passwords doesn't match ! Try again.")

    conn = sqlite3.connect('DBdemo.db')
    c = conn.cursor()

    c.execute("SELECT oid, * from students_demo") 
    stu_recs = c.fetchall()

    c.execute("UPDATE students_demo SET student_password = ?1  WHERE student_user_id = ?2", (student_pwd, student_id,))
    
    conn.commit()
    conn.close()

    messagebox.showinfo("Message","The changes have been made in the database")
    
    modify.destroy()

    admin_home(3)

def update_face_id():
    global student_user_id_modify
    global student_id

    student_id = student_user_id_modify

    dS = "/home/aman/Desktop/1951/Python/opencv-face-recognition/op3/dataset"
    dataSet_path = os.path.join(dS, student_id)
    os.remove(dataSet_path)
    os.system('python dataSetGenerator.py ' + student_id)
    os.system('python extract_embeddings.py --dataset dataset --embeddings output/embeddings.pickle --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7')
    os.system('python train_model.py --embeddings output/embeddings.pickle --recognizer output/recognizer.pickle --le output/le.pickle')

    messagebox.showinfo("Message","Face id for "+student_id+"has been successfully updated.")

    admin_home(3)    

def show_student_records():
    global print_stu_recs
    global stu_search_lbl
    global stu_lbl

    stu_rec = Toplevel()
    stu_rec.title('Records of all students')

    conn = sqlite3.connect('DBdemo.db')
    c = conn.cursor()

    c.execute("SELECT oid, * from student_att") 
    stu_recs = c.fetchall()

    c.execute("SELECT name FROM PRAGMA_TABLE_INFO('student_att')")
    col_names = c.fetchall()

    print_attn_recs_show = ''

    for rec1 in range(len(stu_recs)):
        for cols1 in range(len(col_names)):
            print_attn_recs_show += str(stu_recs[rec1][cols1]) + "\t"
        print_attn_recs_show += "\n"

    conn.commit()
    conn.close()

    stu_search_lbl = Label(stu_rec, text="Search for students here")
    stu_search_lbl.grid(row=0, column=1, pady=(20,0))

    stu_lbl = Label(stu_rec, text=print_attn_recs_show)
    stu_lbl.grid(row=1, column=0, columnspan=3)

def attn_modify():
    global student_user_id_attn_modify
    global student_user_id_label_attn_modify
    global add_student_btn
    global show_student_records_btn
    global remove_student_btn
    global modify_student_btn
    global modify_student_attn_btn

    add_student_btn.grid_forget()
    remove_student_btn.grid_forget()
    show_student_records_btn.grid_forget()
    modify_student_btn.grid_forget()
    modify_student_attn_btn.grid_forget()

    student_user_id_attn_modify = Entry(root, width=30)
    student_user_id_attn_modify.grid(row=0, column=1, padx=20, pady=(150,0))

    #Create text box labels5
    student_user_id_label_attn_modify = Label(root, text="Student User id")
    student_user_id_label_attn_modify.grid(row=0, column=0, pady=(150,0))

    student_attn_modify_btn = Button(root, text="Modify the attendance", command=attn_rec_modify)
    student_attn_modify_btn.grid(row=1, column=1, padx=20, pady=50)

def attn_rec_modify():
    global attn_modify

    attn_modify = Tk()
    attn_modify.title('Modify Student attendance')
    attn_modify.minsize(400,400)
    attn_modify.geometry('400x400')

    global student_user_id_attn_modify
    global student_user_id_label_attn_modify
    global cols
    global t_boxes
    global list_of_labels
    global list_of_textboxes
    global student_user_id_modify2
    global student_user_id_attn_modify2
    global student_user_id_label_attn_modify2
    global student_attn_modify_btn

    list_of_labels = list()
    list_of_textboxes = list()

    cols=list()
    t_boxes=list()
    stu_recs = ''

    student_user_id_modify2 = student_user_id_attn_modify.get()

    conn = sqlite3.connect('DBdemo.db')
    c = conn.cursor()

    c.execute("SELECT oid, * from student_att WHERE student_user_id = ?", (student_user_id_modify2,)) 
    stu_recs = c.fetchall()

    c.execute("SELECT name FROM PRAGMA_TABLE_INFO('student_att')")
    col_names = c.fetchall()

    conn.commit()
    conn.close()

    student_user_id_attn_modify2 = Entry(attn_modify, width=30)
    student_user_id_attn_modify2.grid(row=0, column=1, padx=20, pady=(50,0))
    student_user_id_attn_modify2.insert(0, stu_recs[0][1])
    student_user_id_attn_modify2.config(state=DISABLED)

    i=1
    for col in range(len(col_names)-1):
        list_of_labels.append(Label(attn_modify, text=col_names[i][0]))
        list_of_textboxes.append(Entry(attn_modify, width=10))
        i+=1
    
    j=0
    for col2 in range(len(col_names)-1):
        list_of_labels[j].grid(row=j+1, column=0, padx=2, pady=10)
        list_of_textboxes[j].grid(row=j+1, column=1, padx=2, pady=10)
        list_of_textboxes[j].insert(0, stu_recs[0][j+2])
        j+=1

    #Create text box labels5
    student_user_id_label_attn_modify2 = Label(attn_modify, text="Student User id")
    student_user_id_label_attn_modify2.grid(row=0, column=0, pady=(150,0))

    student_attn_modify2_btn = Button(attn_modify, text="Submit", command=student_attn_modify)
    student_attn_modify2_btn.grid(row=i, column=0,columnspan=2, padx=10, pady=20)

def student_attn_modify():
    global student_user_id_attn_modify2
    global student_user_id_label_attn_modify2
    global attn_recs
    global list_of_textboxes
    global attn_modif

    student_att_modify_id = student_user_id_attn_modify2.get()
    attn_recs = list()

    for t in range(len(list_of_textboxes)):
        attn_recs.append(list_of_textboxes[t].get())

    conn = sqlite3.connect('DBdemo.db')
    c = conn.cursor()

    c.execute("SELECT * from student_att WHERE student_user_id = ?", (student_att_modify_id,)) 
    stu_recs = c.fetchall()

    c.execute("SELECT name FROM PRAGMA_TABLE_INFO('student_att')")
    col_names = c.fetchall()

    q1="UPDATE student_att SET "

    cn=1
    for col3 in range(len(col_names)-1):
        q1+=str(col_names[cn][0])+" = "+str(attn_recs[cn-1])+" WHERE student_user_id = ?"
        c.execute(q1, (student_att_modify_id, ))
        q1="UPDATE student_att SET "
        #c.execute("UPDATE student_att SET %s = %s WHERE student_user_id = %s", (s2, s3, student_att_modify_id ))
        cn+=1
    
    messagebox.showinfo("Message","The attendance of "+str(student_att_modify_id)+" has been changed successfully !", parent=attn_modify)

    conn.commit()
    conn.close()

    attn_modify.destroy()

    admin_home(4)

def page_one(number):
    global admin_user_id
    global admin_user_id_label
    global admin_password
    global admin_password_label
    global admin_register_btn
    global admin_login_btn

    if(number==1):
        global add_student_btn
        global show_student_records_btn
        global remove_student_btn
        global modify_student_btn
        global modify_student_attn_btn

        add_student_btn.grid_forget()
        show_student_records_btn.grid_forget()
        remove_student_btn.grid_forget()
        modify_student_btn.grid_forget()
        modify_student_attn_btn.grid_forget()

    #Create text boxes
    admin_user_id = Entry(root, width=30)
    admin_user_id.grid(row=0, column=1, padx=20, pady=(150,0))

    admin_password = Entry(root, show="*", width=30)
    admin_password.grid(row=1, column=1, padx=20, pady=10)

    #Create text box labels
    admin_user_id_label = Label(root, text="Admin id")
    admin_user_id_label.grid(row=0, column=0, pady=(150,0))

    admin_password_label = Label(root, text="Password")
    admin_password_label.grid(row=1, column=0, pady=10)

    #Buttons
    admin_register_btn = Button(root, text="Register", command=admin_register)
    admin_register_btn.grid(row=2, column=0, padx=20, pady=20)

    admin_login_btn = Button(root, text="Login", command=admin_login)
    admin_login_btn.grid(row=2, column=1, padx=10, pady=20)

page_one(2)

root.mainloop()