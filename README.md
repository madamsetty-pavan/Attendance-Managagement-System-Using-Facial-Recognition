# Attendance-Managagement-System-Using-Facial-Recognition

Attendance management system is a necessary tool for taking attendance in any environment
where attendance is critical. However, most of the existing approach are time consuming,
intrusive and it require manual work from the users. 
This research is aimed at developing a less intrusive, cost effective and more efficient automated student attendance management system
using face recognition that leverages on OpenCV functions for facial recognition. 
The system provides a GUI for marking attendance. It provides an interface for updating attendance using
facial recognition libraries of OpenCV. 
The system stores attendance in a database which is maintained by the administrator. The administrator can view, update and change the attendance of the students. The students can view and update their attendance. 
The system is developed on Open Source image processing library and the interface is developed using Python Tkinter
module. The Tkinter module is an open source module by which we can develop GUI screens
hence, it is not vendor hardware nor software dependent. The OpenCV module used for image
processing is interfaced using Python.


This project consists of 2 parts:
1) Admin
2) Student

   1) Admin: The admin component is a GUI which helps to:
         - Create new student accounts
         - Update existing student accounts and credentials
         - Register new students into the database and train the algorithm with the new face against the student
         - View, Update and Delete the existing attendance records
     
   2) Student: The student component is a GUI which helps to:
        - Login into the portal
        - Update and View Attendance for the day
        - Check the overall attendance percentage 

Link to the research paper used to implement the facial recognition: https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Schroff_FaceNet_A_Unified_2015_CVPR_paper.pdf
