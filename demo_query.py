from tkinter import *
import os
import sys
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox

root = Tk()
root.title('Admin Register')
conn = sqlite3.connect('DBdemo.db')
c=conn.cursor()
s1="amansri"
c.execute("SELECT oid,* FROM STUDENT_ATT where student_user_id= ?",(s1,))
list1=c.fetchall()
q1="SELECT name FROM PRAGMA_TABLE_INFO"
q1+="('student_att')"
c.execute(q1)
col_names = c.fetchall()
#col_names2=col_names
c1=0
min_flag=0
for c1 in range(len(col_names)):
    if(str(col_names[c1][0])=="min00"):
        min_flag=1
    print(col_names[c1][0])
name_flag=0
s1=0
for rec in list1:
    print(rec)
    print(rec[0])
    print(rec[1])
#	if(str(rec[s1])=="Aman"):
#		name_flag=1
 #   s1+=1
print(list1[0][1])
print(list1)
#print(min_flag)
#print(name_flag)
#print(len(col_names))
#print(list1[1])
#print(list1[2])
conn.commit()
conn.close()