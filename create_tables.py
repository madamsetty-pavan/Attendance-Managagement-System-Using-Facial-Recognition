from tkinter import *
import os
import sys
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox

root = Tk()
root.title('Admin Register')
#root.geometry("400*400")

# Database

#create database or connect to one
conn = sqlite3.connect('DBdemo.db')

#create cursor
c = conn.cursor()

#Create table
c.execute("""
        CREATE TABLE admins (
            admin_user_id text,
            admin_password text
        )
        """)

c.execute("""CREATE TABLE students_demo 
        (
            student_user_id text,
            student_password text
        )
        """)

c.execute("""CREATE TABLE student_att
        (
            student_user_id text,
            min00 int DEFAULT 0
        )
        """)

conn.commit()
conn.close()
