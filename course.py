from tkinter import*  
from PIL import Image,ImageTk #pip install pillow

class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System") 
        self.root.geometry("1200x480+50+100")
        self.root.config(bg="white")
        self.root.focus_force()   #to focus on the course window when it is opened

        #===title===
        #`--creating a label for the title of the dashboard with the logo image and styling--`
        title=Label(self.root,text="Manage Course details",font=("goudy old style",20,"bold"),bg="#133365",fg="white",anchor="center").place(x=10,y=15,relwidth=0.98,height=35)

        #=======Variables=======
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()

        #=====Widgets=====
        # ----this section creates the labels and entry fields for course details such as course name, duration, charges, and description. Each label is placed at a specific position on the window, and the corresponding entry fields are created for user input.----

        lbl_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)#1
        lbl_duration=Label(self.root,text="Duration",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)#2
        lbl_charges=Label(self.root,text="Charges",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)#3
        lbl_description=Label(self.root,text="Description",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)#4


        #=====Entry Fields======

        #------this section creates entry fields for the course name, duration, charges, and a text box for the description. The entry fields are linked to the corresponding variables defined earlier, allowing the user to input and store the course details.----
        self.roottxt_courseName=Entry(self.root, textvariable=self.var_course,font=("goudy old style",15,"bold"),bg="lightyellow")#1
        self.roottxt_courseName.place(x=150,y=60, width=200)

        self.roottxt_duration=Entry(self.root, textvariable=self.var_duration,font=("goudy old style",15,"bold"),bg="lightyellow")#2
        self.roottxt_duration.place(x=150,y=100, width=200)

        self.roottxt_charges=Entry(self.root, textvariable=self.var_charges,font=("goudy old style",15,"bold"),bg="lightyellow")#3
        self.roottxt_charges.place(x=150,y=140, width=200)

        self.roottxt_description=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")#4
        self.roottxt_description.place(x=150,y=180, width=460, height=130)

        #=====Buttons======
        #------this section creates buttons for saving, updating, deleting, and clearing course details. Each button is styled with a specific font, background color, foreground color, and cursor type. The buttons are placed at specific positions on the window for user interaction.----
        self.btn_save=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#6f5115",fg="white",cursor="hand2")
        self.btn_save.place(x=150,y=335,width=100,height=40)
        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#172266",fg="white",cursor="hand2")
        self.btn_update.place(x=260,y=335,width=100,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#851107",fg="white",cursor="hand2")
        self.btn_delete.place(x=370,y=335,width=100,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#114816",fg="white",cursor="hand2")
        self.btn_clear.place(x=480,y=335,width=100,height=40)


        #===Search panel==============
        self.var_search=StringVar()
        lbl_search_courseName=Label(self.root,text="Search By | Course Name:",font=("goudy old style",15,"bold"),bg="white").place(x=675,y=60)
        txt_search_courseName=Entry(self.root, textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=900,y=60, width=180)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#6f5115",fg="white",cursor="hand2").place(x=1095,y=60,width=90,height=28)

        
        


if __name__ == "__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()