from tkinter import *
import os
import sys
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox

main_window=Tk()
main_window.title('Attendance Management System - Admin')
main_window.minsize(400,400)
main_window.geometry('500x500')

print_some_recs = StringVar()
col_name = StringVar()

def page_one():
    hide_frames()
    f1.place(relx=0.5, rely=0.5, anchor=CENTER)

def hide_frames():
    f1.place_forget()
    admin_reg.place_forget()
    login_f.place_forget()
    admin_home_f.place_forget()
    student_enlist_f.place_forget()
    student_reg_f.place_forget()
    student_remove_f.place_forget()
    student_modify_f.place_forget()
    studentid_modify_f.place_forget()
    attn_modify_f.place_forget()
    search_box_f.place_forget()
    search_box_back_f.place_forget()
    all_stu_recs.place_forget()
    some_stu_recs_f.place_forget()
    attn_rec_modify_f.place_forget()

def admin_register():
    hide_frames()
    admin_user_id_admin_reg.delete(0, END)
    admin_password_admin_reg.delete(0, END)
    admin_reg.place(relx=0.5, rely=0.5, anchor=CENTER)

def admin_submit():
    #create database or connect to one
    conn = sqlite3.connect('DBdemo.db')

    #create cursor
    c = conn.cursor()

    #insert into table
    c.execute("INSERT INTO admins VALUES (:admin_user_id, :admin_password)",
        {
            'admin_user_id': admin_user_id_admin_reg.get(),
            'admin_password': admin_password_admin_reg.get()
        }  
    )

    #Commit changes
    conn.commit()

    #Close connection
    conn.close()

    hide_frames()
    admin_user_id_login_f.delete(0, END)
    admin_password_login_f.delete(0, END)
    login_f.place(relx=0.5, rely=0.5, anchor=CENTER)

def admin_login():
    conn = sqlite3.connect('DBdemo.db')
    c = conn.cursor()

    temp_user_id = admin_id_f1.get()
    temp_password = admin_password_f1.get()

    c.execute("SELECT admin_user_id from admins")
    admin_ids=c.fetchall()

    name_flag=0
    for rec in admin_ids:
        if(str(rec[0])==str(temp_user_id)):
            #print(rec[0])
            name_flag=1
    
    if(name_flag==0):
        messagebox.showerror("Error !","This User ID does not exist")

        conn.commit()
        conn.close()

        hide_frames()
        admin_id_f1.delete(0, END)
        admin_password_f1.delete(0, END)
        f1.place(relx=0.5, rely=0.5, anchor=CENTER)
    else:
        c.execute("SELECT admin_password from admins WHERE admin_user_id = ?", (temp_user_id,))
        rec_password = str(c.fetchone()[0])
        conn.commit()
        conn.close()
  
        if(rec_password != temp_password and name_flag==1):
            messagebox.showerror("Error !","The password is incorrect ! Try again.")
            hide_frames()
            admin_password_f1.delete(0, END)
            f1.place(relx=0.5, rely=0.5, anchor=CENTER)
        elif(rec_password == temp_password and name_flag==1):
            print("Admin login as %s was successful",temp_user_id)
            hide_frames()
            admin_home_f.place(relx=0.5, rely=0.5, anchor=CENTER)

def admin_login1():
    conn = sqlite3.connect('DBdemo.db')
    c = conn.cursor()

    temp_user_id = admin_user_id_login_f.get()
    temp_password = admin_password_login_f.get()

    c.execute("SELECT admin_user_id from admins")
    admin_ids=c.fetchall()

    name_flag=0
    for rec in admin_ids:
        if(str(rec[0])==str(temp_user_id)):
            name_flag=1

    if(name_flag==0):
        messagebox.showerror("Error !","This User ID does not exist")

        conn.commit()
        conn.close()

        hide_frames()
        login_f.tkraise()
        admin_user_id_login_f.delete(0, END)
        admin_password_login_f.delete(0, END)
        login_f.place(relx=0.5, rely=0.5, anchor=CENTER)
    else:
        c.execute("SELECT admin_password from admins WHERE admin_user_id = ?", (temp_user_id,))
        rec_password = str(c.fetchone()[0])

        conn.commit()
        conn.close()
        if(rec_password != temp_password and name_flag==1):
            messagebox.showerror("Error !","Either the usr_id or password is incorrect ! Try again.")
            hide_frames()
            login_f.tkraise()
            admin_user_id_login_f.delete(0, END)
            admin_password_login_f.delete(0, END)
            login_f.place(relx=0.5, rely=0.5, anchor=CENTER)
        elif(rec_password == temp_password and name_flag==1):
            hide_frames()
            admin_home_f.tkraise()
            admin_home_f.place(relx=0.5, rely=0.5, anchor=CENTER)

def student_enlist():
    hide_frames()
    student_enlist_f.tkraise()
    student_user_id_student_enlist_f.delete(0, END)
    student_password_student_enlist_f.delete(0, END)
    student_enlist_f.place(relx=0.5, rely=0.5, anchor=CENTER)

def show_student_records():
    
    hide_frames()

    search_box_f.place(relx=1, x=-20, y=20, anchor=NE)
    all_stu_recs.place(relx=0.5, rely=0.5, anchor=CENTER)
    search_box_back_f.place(relx=0, x=20, y=20, anchor=NW)
    
    
######################################################################################################
def show_some_stu_recs():
    all_stu_recs.place_forget()

    conn = sqlite3.connect('DBdemo.db')
    c = conn.cursor()

    name_string=str(t_var)
    q1 = "SELECT oid, * from student_att where student_user_id like '%"+str(name_string)+"%' "
    print(q1)

    c.execute(q1)
    some_stu_recs = c.fetchall()

    print(some_stu_recs)

    c.execute("SELECT name FROM PRAGMA_TABLE_INFO('student_att')")
    col_names = c.fetchall()

    print_some_attn_recs_show = "S.no.\t"

    for c1 in range(len(col_names)):
        print_some_attn_recs_show+=str(col_names[c1][0]) + "\t"
   
    print_some_attn_recs_show += "\n"

    for rec1 in range(len(some_stu_recs)):
        for cols1 in range(len(col_names)+1):
            if(cols1==1):
                print_some_attn_recs_show += str(some_stu_recs[rec1][cols1]) + "\t" + "\t"
            else:
                print_some_attn_recs_show += str(some_stu_recs[rec1][cols1]) + "\t"
        print_some_attn_recs_show += "\n"

    conn.commit()
    conn.close()

    print_some_recs.set(" ")
    print_some_recs.set(print_some_attn_recs_show)

def validate(newtext):
    global t_var

    t_var=str(newtext)
    print('validate: {}'.format(newtext))
    return True
vcmd = main_window.register(validate)

def key(event):
    print('key: {}'.format(event.char))

def var(*args):
    print('var: {} (args {})'.format(svar.get(), args))
    if(len(t_var)==0):
        some_stu_recs_f.place_forget()
        all_stu_recs.place(relx=0.5, rely=0.5, anchor=CENTER)
    else:
        show_some_stu_recs()
        some_stu_recs_f.place(relx=0.5, rely=0.5, anchor=CENTER)

svar = StringVar()
svar.trace('w', var)

def ret_pressed():
    stu_search_entry.delete(0, END)
####################################################################################################################

def student_modify():
    hide_frames()
    student_modify_id_student_modify_f.delete(0, END)
    student_modify_f.place(relx=0.5, rely=0.5, anchor=CENTER)

def student_remove():
    hide_frames()
    student_remove_f.tkraise()
    student_remove_id_student_remove_f.delete(0, END)
    student_remove_f.place(relx=0.5, rely=0.5, anchor=CENTER)

def attn_modify_func():
    hide_frames()
    student_user_id_attn_modify.delete(0, END)
    attn_modify_f.place(relx=0.5, rely=0.5, anchor=CENTER)

def admin_logout():
    hide_frames()
    f1.tkraise()
    admin_id_f1.delete(0, END)
    admin_password_f1.delete(0, END)
    f1.place(relx=0.5, rely=0.5, anchor=CENTER)

def student_register():
    temp_student_name = student_user_id_student_enlist_f.get()

    conn = sqlite3.connect('DBdemo.db')
    c = conn.cursor()

    c.execute("SELECT student_user_id from students_demo")
    stu_ids=c.fetchall()

    name_flag=0
    for rec in stu_ids:
        if(str(rec[0])==str(temp_student_name)):
            name_flag=1

    if(name_flag==1):
        messagebox.showerror("Error !","This Student ID already exist")

        conn.commit()
        conn.close()
        
        hide_frames()
        student_enlist_f.tkraise()
        student_user_id_student_enlist_f.delete(0, END)
        student_password_student_enlist_f.delete(0, END)
        student_enlist_f.place(relx=0.5, rely=0.5, anchor=CENTER)
    else:
        c.execute("INSERT INTO students_demo VALUES (:student_user_id, :student_password)",
            {
                'student_user_id': student_user_id_student_enlist_f.get(),
                'student_password': student_password_student_enlist_f.get()
            }  
        )

        conn.commit()
        conn.close()

        hide_frames()
        student_reg_f.tkraise()
        student_reg_f.place(relx=0.5, rely=0.5, anchor=CENTER)

def student_face_id():
    student_name = student_user_id_student_enlist_f.get()

    os.system('python dataSetGenerator.py ' + student_name)
    os.system('python extract_embeddings.py --dataset dataset --embeddings output/embeddings.pickle --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7')
    os.system('python train_model.py --embeddings output/embeddings.pickle --recognizer output/recognizer.pickle --le output/le.pickle')

    messagebox.showinfo("Message","Face id for "+student_name+" has been successfully created.")
    
    hide_frames()
    admin_home_f.tkraise()
    admin_home_f.place(relx=0.5, rely=0.5, anchor=CENTER)

def studentid_remove():
    temp_studentid = student_remove_id_student_remove_f.get()
    
    conn = sqlite3.connect('DBdemo.db')
    c = conn.cursor()

    c.execute("SELECT student_user_id from students_demo")
    student_userids = c.fetchall()
    
    i=0
    stu_flag_id=0
    for stu_id in student_userids:
        if(str(temp_studentid)==str(student_userids[i][0])):
            stu_id_flag=1
        i+=1
    
    if(stu_id_flag!=1):
        messagebox.showerror("Error !","Given Student id doesn't exist ! Try again.")
        
        conn.commit()
        conn.close()

        hide_frames()
        student_remove_f.tkraise()
        student_remove_id_student_remove_f.delete(0, END)
        student_remove_f.place(relx=0.5, rely=0.5, anchor=CENTER)
    else:
        c.execute("DELETE * from students_demo WHERE student_user_id = ?", (temp_studentid,))
        messagebox.showinfo("Message","The record with given Student_id"+temp_studentid+ "has been deleted")

        conn.commit()
        conn.close()
 
        dS = "/home/aman/Desktop/1951/Python/opencv-face-recognition/op4_frames/dataset"
        dataSet_path = os.path.join(dS, temp_studentid)
        os.remove(dataSet_path)

        hide_frames()
        admin_home_f.tkraise()
        admin_home_f.place(relx=0.5, rely=0.5, anchor=CENTER)

def studentid_modify():
    stu_name = student_modify_id_student_modify_f.get()

    conn = sqlite3.connect('DBdemo.db')
    c = conn.cursor()

    c.execute("SELECT student_user_id from students_demo")
    student_userids = c.fetchall()
    
    i=0
    stu_id_flag=0
    for stu_id in student_userids:
        if(str(stu_name)==str(student_userids[i][0])):
            stu_id_flag=1
        i+=1
    
    if(stu_id_flag!=1):
        messagebox.showerror("Error !","Given Student id doesn't exist ! Try again.")
        
        conn.commit()
        conn.close()

        hide_frames()
        student_modify_id_student_modify_f.delete(0, END)
        student_modify_f.place(relx=0.5, rely=0.5, anchor=CENTER)
    else:
        c.execute("SELECT oid, * from student_att WHERE student_user_id = ?", (stu_name,)) 
        stu_recs = c.fetchall()

        conn.commit()
        conn.close()

        hide_frames()
        student_user_id_modify.insert(0, stu_name)
        student_user_id_modify.config(state=DISABLED)
        student_new_pwd.delete(0, END)
        student_new_pwd_confirm.delete(0, END)
        studentid_modify_f.place(relx=0.5, rely=0.5, anchor=CENTER)

def student_det_modify():
    student_id = student_user_id_modify.get()
    student_pwd = student_new_pwd.get()
    student_pwd2 = student_new_pwd_confirm.get()

    if(str(student_pwd)!=str(student_pwd2)):
        messagebox.showerror("Error !","The two passwords doesn't match ! Try again.")
        hide_frames()
        studentid_modify_f.tkraise()
        studentid_modify_f.place(relx=0.5, rely=0.5, anchor=CENTER)
    else:
        conn = sqlite3.connect('DBdemo.db')
        c = conn.cursor()

        c.execute("SELECT oid, * from students_demo") 
        stu_recs = c.fetchall()

        c.execute("UPDATE students_demo SET student_password = ?1  WHERE student_user_id = ?2", (student_pwd, student_id,))
    
        conn.commit()
        conn.close()

        messagebox.showinfo("Message","The changes have been made in the database")
    
        hide_frames()
        admin_home_f.tkraise()
        admin_home_f.place(relx=0.5, rely=0.5, anchor=CENTER)

def update_face_id():
    student_id = student_user_id_modify.get()

    dS = "/home/aman/Desktop/1951/Python/opencv-face-recognition/op4_frames/dataset"
    dataSet_path = os.path.join(dS, student_id)
    os.remove(dataSet_path)
    os.system('python dataSetGenerator.py ' + student_id)
    os.system('python extract_embeddings.py --dataset dataset --embeddings output/embeddings.pickle --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7')
    os.system('python train_model.py --embeddings output/embeddings.pickle --recognizer output/recognizer.pickle --le output/le.pickle')

    messagebox.showinfo("Message","Face id for "+student_id+"has been successfully updated.")

    hide_frames()
    admin_home_f.tkraise()
    admin_home_f.place(relx=0.5, rely=0.5, anchor=CENTER)

def attn_rec_modify():
    '''attn_modify.update()
    attn_modify.title('Modify Student attendance')
    attn_modify.minsize(400,400)
    attn_modify.geometry('400x400')'''

    stu_name = student_user_id_attn_modify.get()

    conn = sqlite3.connect('DBdemo.db')
    c = conn.cursor()

    c.execute("SELECT student_user_id from students_demo")
    student_userids = c.fetchall()
    
    i=0
    stu_id_flag=0
    for stu_id in student_userids:
        if(str(stu_name)==str(student_userids[i][0])):
            stu_id_flag=1
        i+=1
    
    if(stu_id_flag!=1):
        messagebox.showerror("Error !","Given Student id doesn't exist ! Try again.")
        
        conn.commit()
        conn.close()

        attn_modify.destroy()

        hide_frames()
        attn_modify_f.place(relx=0.5, rely=0.5, anchor=CENTER)
    else:
        hide_frames()

        '''student_user_id_modify2 = student_user_id_attn_modify.get()

        '''
        conn = sqlite3.connect('DBdemo.db')
        c = conn.cursor()

        c.execute("SELECT oid, * from student_att WHERE student_user_id = ?", (stu_name,)) 
        stu_recs = c.fetchall()

        c.execute("SELECT name FROM PRAGMA_TABLE_INFO('student_att')")
        col_names = c.fetchall()

        conn.commit()
        conn.close()

        #student_user_id_attn_modify2 = Entry(attn_rec_modify_f, width=30)
        #student_user_id_attn_modify2.grid(row=0, column=1, padx=20, pady=(50,0))
        student_user_id_attn_modify2.insert(0, stu_recs[0][1])
        student_user_id_attn_modify2.config(state=DISABLED)

        #print(len(col_names)-1)

        '''i=1
        for col in range(len(col_names)-1):
            list_of_labels.append(Label(attn_rec_modify_f, text=col_names[i][0]))
            list_of_textboxes.append(Entry(attn_rec_modify_f, width=10))
            i+=1
    
        '''
        j=0
        for col2 in range(len(col_names)-1):
            #print(j)
            #list_of_labels[j].grid(row=j+1, column=0, padx=2, pady=10)
            #list_of_textboxes[j].grid(row=j+1, column=1, padx=2, pady=10)
            list_of_textboxes[j].insert(0, stu_recs[0][j+2])
            col_name_svr[j].set(col_names[j+1][0])
            j+=1

        #Create text box labels5
        '''student_user_id_label_attn_modify2 = Label(attn_rec_modify_f, text="Student User id")
        student_user_id_label_attn_modify2.grid(row=0, column=0, pady=(150,0))

        student_attn_modify2_btn = Button(attn_rec_modify_f, text="Submit", command=student_attn_modify)
        student_attn_modify2_btn.grid(row=i, column=0,columnspan=2, padx=10, pady=20)'''


        attn_rec_modify_f.tkraise()
        attn_rec_modify_f.place(relx=0.5, rely=0.5, anchor=CENTER)
    
def student_attn_modify():
    student_att_modify_id = student_user_id_attn_modify.get()
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
    
    messagebox.showinfo("Message","The attendance of "+str(student_att_modify_id)+" has been changed successfully !")

    conn.commit()
    conn.close()

    hide_frames()
    admin_home_f.place(relx=0.5, rely=0.5, anchor=CENTER)

def search_box_back():
    hide_frames()
    admin_home_f.place(relx=0.5, rely=0.5, anchor=CENTER)

def attn_rec_modify_f_back():
    hide_frames()
    admin_home_f.place(relx=0.5, rely=0.5, anchor=CENTER)

f1=Frame(main_window)
admin_id_f1 = Entry(f1, width=30)
admin_id_f1.grid(row=0, column=1, padx=20, pady=(150,0))
admin_password_f1 = Entry(f1, show="*", width=30)
admin_password_f1.grid(row=1, column=1, padx=20, pady=10)

#Create text box labels
admin_user_id_label_f1 = Label(f1, text="Admin id")
admin_user_id_label_f1.grid(row=0, column=0, pady=(150,0))

admin_password_label_f1 = Label(f1, text="Password")
admin_password_label_f1.grid(row=1, column=0, pady=10)

#Buttons
admin_register_btn_f1 = Button(f1, text="Register", command=admin_register)
admin_register_btn_f1.grid(row=2, column=0, padx=20, pady=20)

admin_login_btn_f1 = Button(f1, text="Login", command=admin_login)
admin_login_btn_f1.grid(row=2, column=1, padx=10, pady=20)

#f1.place(relx=0.5, rely=0.5, anchor=CENTER)


admin_reg=Frame(main_window)
admin_user_id_admin_reg = Entry(admin_reg, width=30)
admin_user_id_admin_reg.grid(row=0, column=1, padx=20, pady=(150,0))

admin_password_admin_reg = Entry(admin_reg, show="*", width=30)
admin_password_admin_reg.grid(row=1, column=1, padx=20, pady=10)

#Create text box labels
admin_user_id_label_admin_reg = Label(admin_reg, text="Admin id")
admin_user_id_label_admin_reg.grid(row=0, column=0, pady=(150,0))

admin_password_label_admin_reg = Label(admin_reg, text="Password")
admin_password_label_admin_reg.grid(row=1, column=0, pady=10)

#Buttons
admin_submit_btn_admin_reg = Button(admin_reg, text="Submit", command=admin_submit)
admin_submit_btn_admin_reg.grid(row=2, column=0, columnspan=2, padx=10, pady=20)


login_f=Frame(main_window)
admin_user_id_login_f = Entry(login_f, width=30)
admin_user_id_login_f.grid(row=0, column=1, padx=20, pady=(150,0))

admin_password_login_f = Entry(login_f, show="*", width=30)
admin_password_login_f.grid(row=1, column=1, padx=20, pady=10)

#Create text box labels
admin_user_id_label_login_f = Label(login_f, text="Admin id")
admin_user_id_label_login_f.grid(row=0, column=0, pady=(150,0))

admin_password_label_login_f = Label(login_f, text="Password")
admin_password_label_login_f.grid(row=1, column=0, pady=10)

#Buttons
admin_login_btn_login_f = Button(login_f, text="Login", command=admin_login1)
admin_login_btn_login_f.grid(row=2, column=1, padx=10, pady=20)


admin_home_f=Frame(main_window)
add_student_btn_admin_home_f = Button(admin_home_f, text="Add Student", command=student_enlist)
add_student_btn_admin_home_f.grid(row=0, column=0, pady=(50,20), padx=50)
show_student_records_btn_admin_home_f = Button(admin_home_f, text="Show all records", command=show_student_records)
show_student_records_btn_admin_home_f.grid(row=1, column=0, pady=20, padx=50)
remove_student_btn_admin_home_f = Button(admin_home_f, text="Remove Student record", command=student_remove)
remove_student_btn_admin_home_f.grid(row=2, column=0, pady=20, padx=50)
modify_student_btn_admin_home_f = Button(admin_home_f, text="Modify Student record", command=student_modify)
modify_student_btn_admin_home_f.grid(row=3, column=0, pady=20, padx=50)
modify_student_attn_btn_admin_home_f = Button(admin_home_f, text="Modify Student attendance", command=attn_modify_func)
modify_student_attn_btn_admin_home_f.grid(row=4, column=0, pady=20, padx=50)
admin_logout_btn_admin_home_f = Button(admin_home_f, text="Log Out", command=admin_logout)
admin_logout_btn_admin_home_f.grid(row=5, column=0, pady=20, padx=50)


student_enlist_f=Frame(main_window)
student_user_id_student_enlist_f = Entry(student_enlist_f, width=30)
student_user_id_student_enlist_f.grid(row=0, column=1, padx=20, pady=(150,0))

student_password_student_enlist_f = Entry(student_enlist_f, show="*", width=30)
student_password_student_enlist_f.grid(row=1, column=1, padx=20, pady=10)

#Create text box labels5
student_user_id_label_student_enlist_f = Label(student_enlist_f, text="Student id")
student_user_id_label_student_enlist_f.grid(row=0, column=0, pady=(150,0))

student_password_label_student_enlist_f = Label(student_enlist_f, text="Password")
student_password_label_student_enlist_f.grid(row=1, column=0, pady=10)

student_register_btn_student_enlist_f = Button(student_enlist_f, text="Register", command=student_register)
student_register_btn_student_enlist_f.grid(row=2, column=0,columnspan=2, padx=10, pady=20)

student_enlist_f_back_btn = Button(student_enlist_f, text="Back to home", command=attn_rec_modify_f_back)
student_enlist_f_back_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=20)


student_reg_f=Frame(main_window)
student_name=student_user_id_student_enlist_f.get()

face_id_inst1 = Label(student_reg_f, text="Welcome " + student_name + "!")
face_id_inst1.grid(row=1, column=0, padx=20, pady=(50,0))

face_id_inst2 = Label(student_reg_f, text="Your record has been added to our database")
face_id_inst2.grid(row=2, column=0, padx=20, pady=10)

face_id_inst3 = Label(student_reg_f, text="To create your unique face_id, click on the below button.")
face_id_inst3.grid(row=3, column=0, padx=20, pady=10)
    
student_face_id_btn_student_reg_f = Button(student_reg_f, text="Create Face ID", command=student_face_id)
student_face_id_btn_student_reg_f.grid(row=4, column=0, padx=20, pady=30)

student_reg_f_back_btn = Button(student_reg_f, text="Back to home", command=attn_rec_modify_f_back)
student_reg_f_back_btn.grid(row=5, column=0, padx=20, pady=30)


student_remove_f = Frame(main_window)
student_remove_id_label_student_remove_f = Label(student_remove_f, text="Student id")
student_remove_id_label_student_remove_f.grid(row=0, column=0, padx=20, pady=(150,0))

student_remove_id_student_remove_f = Entry(student_remove_f,width=30)
student_remove_id_student_remove_f.grid(row=0, column=1, padx=20, pady=(150,0))

student_remove_id_btn_student_remove_f = Button(student_remove_f, text="Remove", command=studentid_remove)
student_remove_id_btn_student_remove_f.grid(row=1, column=1, padx=20, pady=50)

student_remove_f_back_btn = Button(student_remove_f, text="Back to home", command=attn_rec_modify_f_back)
student_remove_f_back_btn.grid(row=2, column=1, padx=20, pady=20)


student_modify_f = Frame(main_window)
student_modify_id_label_student_modify_f = Label(student_modify_f, text="Student id")
student_modify_id_label_student_modify_f.grid(row=0, column=0, padx=20, pady=(150,0))

student_modify_id_student_modify_f = Entry(student_modify_f,width=30)
student_modify_id_student_modify_f.grid(row=0, column=1, padx=20, pady=(150,0))

student_modify_id_btn_student_modify_f = Button(student_modify_f, text="Modify", command=studentid_modify)
student_modify_id_btn_student_modify_f.grid(row=1, column=0, padx=20, pady=50)

student_update_faceid_btn_student_modify_f = Button(student_modify_f, text="Update Face id", command=update_face_id)
student_update_faceid_btn_student_modify_f.grid(row=1, column=1, padx=20, pady=50)

student_modify_f_back_btn = Button(student_modify_f, text="Back to home", command=attn_rec_modify_f_back)
student_modify_f_back_btn.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

studentid_modify_f = Frame(main_window)
stu_name = student_modify_id_student_modify_f.get()

student_user_id_modify = Entry(studentid_modify_f, width=30)
student_user_id_modify.grid(row=0, column=1, padx=20, pady=(150,0))

#Create text box labels5
student_user_id_label_modify = Label(studentid_modify_f, text="Student User id")
student_user_id_label_modify.grid(row=0, column=0, pady=(150,0))

student_new_pwd_label = Label(studentid_modify_f, text="New Password")
student_new_pwd_label.grid(row=1, column=0, pady=10)

student_new_pwd_confirm_label = Label(studentid_modify_f, text="Confirm new Password")
student_new_pwd_confirm_label.grid(row=2, column=0, pady=10)

student_new_pwd = Entry(studentid_modify_f, show="*", width=30)
student_new_pwd.grid(row=1, column=1, padx=20, pady=10)

student_new_pwd_confirm = Entry(studentid_modify_f, show="*", width=30)
student_new_pwd_confirm.grid(row=2, column=1, pady=10)

conn = sqlite3.connect('DBdemo.db')
c = conn.cursor()

c.execute("SELECT oid, * from student_att WHERE student_user_id = ?", (stu_name,)) 
stu_recs = c.fetchall()

for record in range(len(stu_recs)):
    if(str(stu_recs[record][1])==str(stu_name)):
        student_user_id_modify.insert(0, stu_recs[record][1])

conn.commit()
conn.close()

student_register_btn_modify = Button(studentid_modify_f, text="Submit", command=student_det_modify)
student_register_btn_modify.grid(row=3, column=0,columnspan=2, padx=10, pady=20)

studentid_modify_f_back_btn = Button(studentid_modify_f, text="back to home", command=attn_rec_modify_f_back)
studentid_modify_f_back_btn.grid(row=4, column=0, columnspan=2, padx=10, pady=20)


attn_modify_f = Frame(main_window)
student_user_id_attn_modify = Entry(attn_modify_f, width=30)
student_user_id_attn_modify.grid(row=0, column=1, padx=20, pady=(150,0))

#Create text box labels5
student_user_id_label_attn_modify = Label(attn_modify_f, text="Student User id")
student_user_id_label_attn_modify.grid(row=0, column=0, pady=(150,0))

student_attn_modify_btn = Button(attn_modify_f, text="Modify the attendance", command=attn_rec_modify)
student_attn_modify_btn.grid(row=1, column=1, padx=20, pady=50)

attn_modify_f_back_btn = Button(attn_modify_f, text="Back to home", command=attn_rec_modify_f_back )
attn_modify_f_back_btn.grid(row=2, column=1, padx=20, pady=20)

attn_rec_modify_f = Frame(main_window)
list_of_labels = list()
list_of_textboxes = list()
col_name_svr  = list()

#student_user_id_modify2 = student_user_id_attn_modify.get()

conn = sqlite3.connect('DBdemo.db')
c = conn.cursor()

#c.execute("SELECT oid, * from student_att WHERE student_user_id = ?", (student_user_id_modify2,)) 
#stu_recs = c.fetchall()

c.execute("SELECT name FROM PRAGMA_TABLE_INFO('student_att')")
col_names = c.fetchall()

conn.commit()
conn.close()

student_user_id_attn_modify2 = Entry(attn_rec_modify_f, width=30)
student_user_id_attn_modify2.grid(row=0, column=1, padx=20, pady=50)
#student_user_id_attn_modify2.insert(0, student_user_id_attn_modify2)
#student_user_id_attn_modify2.config(state=DISABLED)

i=1
for col in range(len(col_names)-1):
    col_name_svr.append(StringVar())
    col_name_svr[i-1].set("")
    list_of_labels.append(Label(attn_rec_modify_f, textvariable=col_name_svr[i-1]))
    list_of_textboxes.append(Entry(attn_rec_modify_f, width=10))
    i+=1
    
j=0
for col2 in range(len(col_names)-1):
    #print(j)
    list_of_labels[j].grid(row=j+1, column=0, padx=2, pady=10)
    list_of_textboxes[j].grid(row=j+1, column=1, padx=2, pady=10)
    #list_of_textboxes[j].insert(0, stu_recs[0][j+2])
    j+=1

#Create text box labels5
student_user_id_label_attn_modify2 = Label(attn_rec_modify_f, text="Student User id")
student_user_id_label_attn_modify2.grid(row=0, column=0, pady=50)

student_attn_modify2_btn = Button(attn_rec_modify_f, text="Submit", command=student_attn_modify)
student_attn_modify2_btn.grid(row=i, column=0, columnspan=2, padx=10, pady=20)

attn_rec_modify_f_back_btn = Button(attn_rec_modify_f, text="Back to home", command=attn_rec_modify_f_back)
attn_rec_modify_f_back_btn.grid(row=i+1, column=0, columnspan=2, padx=10, pady=20)


search_box_f=Frame(main_window)

stu_search_lbl = Entry(search_box_f)
stu_search_lbl.insert(0, "Search for students here")
stu_search_lbl.config(state=DISABLED)
stu_search_lbl.pack()

stu_search_entry = Entry(search_box_f, textvariable=svar, validate="key", validatecommand=(vcmd, '%P'))
stu_search_entry.pack()


all_stu_recs = Frame(main_window)
conn = sqlite3.connect('DBdemo.db')
c = conn.cursor()

c.execute("SELECT oid, * from student_att") 
stu_recs = c.fetchall()

c.execute("SELECT name FROM PRAGMA_TABLE_INFO('student_att')")
col_names = c.fetchall()

print_attn_recs_show = "S.no.\t"

for c1 in range(len(col_names)):
    print_attn_recs_show+=str(col_names[c1][0]) + "\t"
   
print_attn_recs_show += "\n"

for rec1 in range(len(stu_recs)):
    for cols1 in range(len(col_names)+1):
        if(cols1==1):
            print_attn_recs_show += str(stu_recs[rec1][cols1]) + "\t" + "\t"
        else:
            print_attn_recs_show += str(stu_recs[rec1][cols1]) + "\t"
    print_attn_recs_show += "\n"

conn.commit()
conn.close()

stu_lbl = Label(all_stu_recs, text=print_attn_recs_show)
stu_lbl.pack()


some_stu_recs_f = Frame(main_window)

print_some_attn_recs_show = "Demo"

some_stu_lbl = Label(some_stu_recs_f, textvariable=print_some_recs)
some_stu_lbl.pack()


search_box_back_f = Frame(main_window)

search_box_back_btn = Button(search_box_back_f, text="Back to home", command=search_box_back)
search_box_back_btn.pack()

page_one()

main_window.mainloop()