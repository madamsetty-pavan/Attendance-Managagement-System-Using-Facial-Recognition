from tkinter import *
import os
import sys
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox

root = Tk()
root.title('Show tables')
#root.geometry("400*400")

# Database

#create database or connect to one
conn = sqlite3.connect('DBdemo.db')

#create cursor
c = conn.cursor()

#Create table
c.execute("""
        SELECT oid,* from admins
        """)
admin_records = c.fetchall()

print "Admin Records"

label1 = Label(root, text="Admin records")
label1.grid(row=0, column=0, columnspan=3)

print_admin_records = ''
for record1 in admin_records:
    print_admin_records += str(record1[0]) + "\t" + str(record1[1]) + "\t" + str(record1[2]) + "\n"
    
admin_rec_label = Label(root, text=print_admin_records)
admin_rec_label.grid(row=1, column=0, columnspan=2)

c.execute("""
        SELECT oid,* from students_demo
        """)
student_records = c.fetchall()
    #print(admin_records)

print "Student records"

label2 = Label(root, text="Student records")
label2.grid(row=2, column=0, columnspan=3)

print_student_records = ''
for record2 in student_records:
    print_student_records += str(record2[0]) + "\t" + str(record2[1]) + "\t" + str(record2[2]) + "\n"
    
students_rec_label = Label(root, text=print_student_records)
students_rec_label.grid(row=3, column=0, columnspan=2)

c.execute("""
        SELECT oid,* from student_att
        """)
att_records = c.fetchall()
    #print(admin_records)

label3 = Label(root, text="Studnts attendance records")
label3.grid(row=4, column=0, columnspan=3)

c.execute("""
        SELECT name FROM PRAGMA_TABLE_INFO('student_att')
        """)
col_names = c.fetchall()
i=0

print "Student attendance records"
print_att_records = ''
for record3 in att_records:
    for col in col_names:
        print_att_records += str(record3[i]) + "\t"
    i += 1
    print_att_records += "\n"
    
attn_label = Label(root, text=print_att_records)
attn_label.grid(row=5, column=0, columnspan=2)


conn.commit()
conn.close()

root.mainloop()