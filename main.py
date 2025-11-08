from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk  
import os
from student import Student
from train import Train
from face_recognition import Face_recognition



class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
    
    # first image
        img = Image.open(r"/Users/amanyadav/Desktop/Face_Recognition_System/images/images.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

    # second image
        img1 = Image.open(r"/Users/amanyadav/Desktop/Face_Recognition_System/images/download.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)           

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

    # third image
        img2 = Image.open(r"/Users/amanyadav/Desktop/Face_Recognition_System/images/images-1.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)           

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)


    # background image
        img3 = Image.open(r"/Users/amanyadav/Desktop/Face_Recognition_System/images/img2.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)   

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

    
    # title section
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=0, width=1530, height=45)


    # student button
        img4 = Image.open(r"/Users/amanyadav/Desktop/Face_Recognition_System/images/img3.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)   

        b1 = Button(bg_img, image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details",command=self.student_details,cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="black")
        b1_1.place(x=200, y=300, width=220, height=40)

    
    # face detector button
        img5 = Image.open(r"/Users/amanyadav/Desktop/Face_Recognition_System/images/img4.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=500, y=100, width=220, height=220)   

        b2_2 = Button(bg_img, text="Face Detector",cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="black")
        b2_2.place(x=500, y=300, width=220, height=40)

    # attendance button
        img6 = Image.open(r"/Users/amanyadav/Desktop/Face_Recognition_System/images/img5.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)   

        b3 = Button(bg_img, image=self.photoimg6,cursor="hand2")
        b3.place(x=800, y=100, width=220, height=220)

        b3_3 = Button(bg_img, text="Attendance",cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="black")
        b3_3.place(x=800, y=300, width=220, height=40)

    
    # help button
        img7 = Image.open(r"/Users/amanyadav/Desktop/Face_Recognition_System/images/img6.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)   

        b4 = Button(bg_img, image=self.photoimg7,cursor="hand2")
        b4.place(x=1100, y=100, width=220, height=220)

        b4_4 = Button(bg_img, text="Help Desk",cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="black")
        b4_4.place(x=1100, y=300, width=220, height=40)

    # train data button
        img8 = Image.open(r"/Users/amanyadav/Desktop/Face_Recognition_System/images/img7.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)   

        b5 = Button(bg_img, image=self.photoimg8,cursor="hand2",command=self.train_data)
        b5.place(x=200, y=400, width=220, height=220)

        b5_5 = Button(bg_img, text="Train Data",cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="black")
        b5_5.place(x=200, y=600, width=220, height=40)

    # photo button
        img9 = Image.open(r"/Users/amanyadav/Desktop/Face_Recognition_System/images/img8.jpg")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)       

        b6 = Button(bg_img, image=self.photoimg9,cursor="hand2",command=self.open_img)
        b6.place(x=500, y=400, width=220, height=220)

        b6_6 = Button(bg_img, text="Photos",cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="black")
        b6_6.place(x=500, y=600, width=220, height=40)

    # developer button
        img10 = Image.open(r"/Users/amanyadav/Desktop/Face_Recognition_System/images/img9.jpg")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)   

        b7 = Button(bg_img, image=self.photoimg10,cursor="hand2")
        b7.place(x=800, y=400, width=220, height=220)

        b7_7 = Button(bg_img, text="Developer",cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="black")
        b7_7.place(x=800, y=600, width=220, height=40)

    # exit button
        img11 = Image.open(r"/Users/amanyadav/Desktop/Face_Recognition_System/images/img10.jpg")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)   

        b8 = Button(bg_img, image=self.photoimg11,cursor="hand2")
        b8.place(x=1100, y=400, width=220, height=220)

        b8_8 = Button(bg_img, text="Exit",cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="black")
        b8_8.place(x=1100, y=600, width=220, height=40)




    # =============Open photos folder============
    def open_img(self):
        folder = "data"
        if not os.path.exists(folder):
            os.makedirs(folder)  # Create folder if it doesn't exist

        # Open folder on macOS
        os.system(f"open {folder}")



    # ============= Function buttons =============

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)



    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)



    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)


















if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()