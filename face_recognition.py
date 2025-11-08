import csv
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
from time import strftime
from datetime import datetime
import cv2
import numpy as np




class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



        # Title
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=0, width=1530, height=45)


        # image 1
        img_top = Image.open(r"/Users/amanyadav/Desktop/Face_Recognition_System/images/img18.jpg")
        img_top  = img_top .resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top )

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)


        # image2

        img_bottom = Image.open(r"/Users/amanyadav/Desktop/Face_Recognition_System/images/img19.webp")
        img_bottom = img_bottom .resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom )

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)


        # button
        b1_1 = Button(f_lbl, text="Face Recognition",cursor="hand2",command=self.face_recog, font=("times new roman", 30, "bold"), bg="darkblue", fg="black")
        b1_1.place(x=365, y=620, width=250, height=40)

    # ================Attendence====================

    def mark_attendance(self,sid, name, roll, dep):
        with open("Attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((sid not in name_list) and (name not in name_list)and (roll not in name_list)and (dep not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{sid},{name},{roll},{dep},{dtString},{d1},Present")





    # =============face recognition===============
    
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0,255,0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])

                # predict confidence
                confidence = int((100 * (1 - predict / 300)))

                if confidence > 77:
                    # ========== Get student details from CSV ==========
                    sid, name, roll, dep = self.get_student_details(id)

                    cv2.putText(img, f"ID: {sid}", (x, y-95), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
                    cv2.putText(img, f"Name: {name}", (x, y-75), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
                    cv2.putText(img, f"Roll: {roll}", (x, y-55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
                    cv2.putText(img, f"Department: {dep}", (x, y-35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
                    self.mark_attendance(sid,name,roll,dep)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0,0,255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")  # <-- trained model

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()


    # ============= get student details from CSV ================
    def get_student_details(self, student_id):
        try:
            with open("student_data.csv", "r") as f:
                reader = csv.reader(f)
                next(reader)  # skip header
                for row in reader:
                    # Compare with Student ID column (row[4])
                    if row[4] == str(student_id):  
                        dep = row[0]      # Department
                        sid = row[4]      # Student ID
                        name = row[5]     # Name
                        roll = row[7]     # Roll No
                        return sid, name, roll, dep
        except Exception as e:
            print("CSV Read Error:", e)
        return "Unknown", "Unknown", "Unknown", "Unknown"









if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()