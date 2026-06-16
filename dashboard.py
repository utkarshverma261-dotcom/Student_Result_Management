from tkinter import*  
from PIL import Image,ImageTk #pip install pillow

class RMS:
    def __init__(self,root): #function for initializing the window and its properties for the result management system
        self.root=root
        self.root.title("Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # ---icons---
        # path of the logo image for the dashboard 
        # --resizing the logo image to fit the dashboard title--
        # --converting the logo image to a format that can be used in tkinter--

        self.logo_dash= Image.open("images/logo.png") 
        self.logo_dash=self.logo_dash.resize((50,50),Image.LANCZOS) 
        self.logo_dash=ImageTk.PhotoImage(self.logo_dash)

        #---title--
            #`--creating a label for the title of the dashboard with the logo image and styling--`
        title=Label(self.root,text="Student Result Management System",padx=10,compound=LEFT,image= self.logo_dash,font=("goudy old style",20,"bold"),bg="#133365",fg="white",anchor="center").place(x=0,y=0,relwidth=1,height=50)

        #===Menu===
        #---menu frame for the dashboard with styling---

        screen_width = self.root.winfo_screenwidth() # 1. Get the screen width dynamically and subtract margins
        dynamic_width = screen_width - 20 

        M_Frame=LabelFrame(self.root, text="Menus", font=("goudy old style",15,"bold"), bg="#133365",fg="white")
        M_Frame.place(x=10,y=70,relwidth=0.98,height=80)

        # --button for the menu with styling--
        #--from the menu frame, create buttons for different functionalities of the dashboard and pack them to the left side of the menu frame with padding and styling--
        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#007E91",fg="white",cursor="hand2")#1
        btn_course.pack(side="left", expand=True, fill="x", padx=10, pady=5) #1
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#007E91",fg="white",cursor="hand2")#2
        btn_student.pack(side="left", expand=True, fill="x", padx=10, pady=5) #2
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#007E91",fg="white",cursor="hand2")#3
        btn_result.pack(side="left", expand=True, fill="x", padx=10, pady=5) #3
        btn_view=Button(M_Frame,text="View",font=("goudy old style",15,"bold"),bg="#007E91",fg="white",cursor="hand2")#4
        btn_view.pack(side="left", expand=True, fill="x", padx=10, pady=5) #4
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#007E91",fg="white",cursor="hand2")#5
        btn_logout.pack(side="left", expand=True, fill="x", padx=10, pady=5) #5
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#007E91",fg="white",cursor="hand2")#6
        btn_exit.pack(side="left", expand=True, fill="x", padx=10, pady=5) #6

        #===content_window===
        #---background image for the dashboard with styling---
        self.bg_img = Image.open("images/bg.png")
        # Fixed Pillow error: changed Image.ANTIALIAS to Image.Resampling.LANCZOS
        self.bg_img = self.bg_img.resize((920, 450), Image.Resampling.LANCZOS) 
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl = Label(self.root, image=self.bg_img)
        self.lbl.place(x=450, y=180, relwidth=0.6, relheight=0.5)


        #===Update_Details===
        #--labels for displaying the total number of courses, students, and results with styling--
        #=== Course Dashboard Box ===
        self.lbl_course = Label(self.root, text="Total Course\n[ 0 ]", font=("goudy old style", 20, "bold"), bd=10, bg="#092e53", fg="white", relief=RIDGE)
        # Position is fixed at x=400, y=505, but width and height scale automatically
        self.lbl_course.place(x=400, y=510, relwidth=0.18, relheight=0.13)

        #=== Student Dashboard Box ===
        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]", font=("goudy old style", 20, "bold"), bd=10, bg="#0676ad", fg="white", relief=RIDGE)
        # Position is fixed at x=710, y=505, but width and height scale automatically
        self.lbl_student.place(x=710, y=510, relwidth=0.18, relheight=0.13)

        #=== Result Dashboard Box ===
        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]", font=("goudy old style", 20, "bold"), bd=10, bg="#038074", fg="white", relief=RIDGE)
        # Position is fixed at x=1020, y=505, but width and height scale automatically
        self.lbl_result.place(x=1020, y=510, relwidth=0.18, relheight=0.13)





        #===footer===
        #footer for the dashboard with styling
        footer=Label(self.root,text="SRMS-Student Result Management System\nContact Us for any Technical Issue:987xxxx01",font=("goudy old style",12),bg="#262626",fg="white",anchor="center").pack(side=BOTTOM,fill=X)

        
        
     

if __name__ == "__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()