import csv
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import cv2



class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



        # first image
        img = Image.open(r"/Users/amanyadav/Desktop/Face_Recognition_System/images/img20.jpg")
        img = img.resize((800, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=750, height=200)

        # second image
        img1 = Image.open(r"/Users/amanyadav/Desktop/Face_Recognition_System/images/img21.webp")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=750, y=0, width=750, height=200)


        # background image
        img3 = Image.open(r"/Users/amanyadav/Desktop/Face_Recognition_System/images/img2.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)


        # title section
        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=0, width=1530, height=45)


        # main frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1480, height=600)


        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)


        # left label frame image
        img_left = Image.open(r"/Users/amanyadav/Desktop/Face_Recognition_System/images/img14.jpg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)


        # left_inside_frame
        left_inside_frame= Frame(Left_frame, bd=2,relief=RIDGE, bg="white")
        left_inside_frame.place(x=5, y=135, width=715, height=300)



        #labels and entry
        #Attendance id
        attendanceId_label = Label(left_inside_frame, text="AttendanceId:", font=("times new roman", 12, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceId_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)


        # Roll
        rollLabel = Label(left_inside_frame, text="Roll:",bg="white", font=("comicsansns 11 bold"))
        rollLabel.grid(row=0, column=0, padx=4, pady=8)

        atten_roll = ttk.Entry(left_inside_frame, width=22, font=("comicsansns 11 bold"))
        atten_roll.grid(row=0, column=3, pady=8)


        # Name
        nameLabel = Label(left_inside_frame, text="Name:", font=("comicsansns 11 bold"), bg="white")
        nameLabel.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        atten_name = ttk.Entry(left_inside_frame, width=22, font=("comicsansns 11 bold"))
        atten_name.grid(row=1, column=2, padx=10, pady=5, sticky=W)


        # Department
        depLabel = Label(left_inside_frame, text="Department:", font=("comicsansns 11 bold"), bg="white")
        depLabel.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        atten_dep = ttk.Entry(left_inside_frame, width=22, font=("comicsansns 11 bold"))
        atten_dep.grid(row=1, column=3, padx=10, pady=5, sticky=W)


        # Time
        timeLabel = Label(left_inside_frame, text="Timet:", font=("comicsansns 11 bold"), bg="white")
        timeLabel.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        atten_time = ttk.Entry(left_inside_frame, width=22, font=("comicsansns 11 bold"))
        atten_time.grid(row=2, column=1, padx=10, pady=5, sticky=W)


        # date
        dateLabel = Label(left_inside_frame, text="Date:", font=("comicsansns 11 bold"), bg="white")
        dateLabel.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        atten_date = ttk.Entry(left_inside_frame, width=22, font=("comicsansns 11 bold"))
        atten_date.grid(row=2, column=3, padx=10, pady=5, sticky=W)


        # Attendance
        attendanceLabel = Label(left_inside_frame, text="Attendance", font=("comicsansns 11 bold"), bg="white")
        attendanceLabel.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        
        self.atten_status = ttk.Combobox(left_inside_frame , font=("comicsansns 11 bold"), state="readonly", width=18)
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1, padx=10, pady=5, sticky=W)







        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=660, height=580)





if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()