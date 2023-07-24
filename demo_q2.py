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
c.execute("insert into student_att (student_user_id, min00) values (?,1)", (s1,))
#list1=c.fetchall()
#print(list1)
#for c1 in range(len(list1)):
#	print(list1[c1])
#	print(list1[c1][0])
#print("End for c1")
#for rec in list1:
#    print(rec)
#    print(rec[0])

#print(list1[0][1])
#print(list1[0])
conn.commit()
conn.close()