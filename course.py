from tkinter import*  
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk, messagebox
import sqlite3

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

        #------------------------------------------------------------------------------------------------------------------------------#

        #=====Widgets=====
        # - UI Elements: Labels and matching entry fields for course attributes
        # - Layout: Positioned specifically on the window for structured data entry

        lbl_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)#1
        lbl_duration=Label(self.root,text="Duration",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)#2
        lbl_charges=Label(self.root,text="Charges",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)#3
        lbl_description=Label(self.root,text="Description",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)#4


        #-------------------------------------------------------------------------------------------------------------------------------#

        #=====Entry Fields======

        # - Inputs: Entry fields for Name, Duration, Charges; Text box for Description
        # - Functionality: Linked to variables to capture and store user input
        self.txt_courseName=Entry(self.root, textvariable=self.var_course,font=("goudy old style",15,"bold"),bg="lightyellow")#1
        self.txt_courseName.place(x=150,y=60, width=200)

        self.txt_duration=Entry(self.root, textvariable=self.var_duration,font=("goudy old style",15,"bold"),bg="lightyellow")#2
        self.txt_duration.place(x=150,y=100, width=200)

        self.txt_charges=Entry(self.root, textvariable=self.var_charges,font=("goudy old style",15,"bold"),bg="lightyellow")#3
        self.txt_charges.place(x=150,y=140, width=200)

        self.txt_description=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")#4
        self.txt_description.place(x=150,y=180, width=460, height=130)

        #------------------------------------------------------------------------------------------------------------------------------#

        #=============================Buttons==================================#
        
        # - Actions: Save, Update, Delete, and Clear course details
        # - Styling: Custom fonts, background/foreground colors, and active cursors
        # - Layout: Positioned at specific coordinates for user interaction
        self.btn_save=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#6f5115",fg="white",cursor="hand2",command=self.add)
        self.btn_save.place(x=150,y=335,width=100,height=40)
        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#172266",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=260,y=335,width=100,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#851107",fg="white",cursor="hand2", command=self.delete)
        self.btn_delete.place(x=370,y=335,width=100,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#114816",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=480,y=335,width=100,height=40)



        #------------------------------------------------------------------------------------------------------------------------------#
        #===Search panel==============
        
        # - UI Elements: Label, Entry field, and styled Search button
        # - Styling: Custom font, colors, and cursor for the button
        # - Layout: Placed at a specific position for user interaction
        self.var_search=StringVar()
        lbl_search_courseName=Label(self.root,text="Search By | Course Name:",font=("goudy old style",15,"bold"),bg="white").place(x=675,y=60)
        txt_search_courseName=Entry(self.root, textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=900,y=60, width=180)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#6f5115",fg="white",cursor="hand2",command=self.search).place(x=1095,y=60,width=90,height=28)

        #=====Content=========
        
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=675,y=100,width=520,height=350)


       
        # """Creates and packs a scrollable Treeview widget to display course details 
        # (ID, Name, Duration, Charges, Description) in a tabular format.""""
        #-----------------------------------------------------------------------------------------#

        # - Scrollable Treeview: Implements vertical and horizontal scrollbars for navigating through course data
        
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","duration","charges","description") ,yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)   
        scrolly.config(command=self.CourseTable.yview)
        scrollx.config(command=self.CourseTable.xview)

        #--------------------------------------------------------------------------------------------#
        # - Headings: Defines column headings for the Treeview to display course attributes
        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("charges",text="Charges")
        self.CourseTable.heading("description",text="Description")
       #---------------------------------------------------------------------------------------------#
        # - Configuration: Sets the Treeview to show only headings and defines column widths for each attribute 

        self.CourseTable["show"]="headings"
        self.CourseTable.column("cid",width=60)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("charges",width=100)
        self.CourseTable.column("description",width=150)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#------------------------------------------------------------------------------------------------------------------#
# ================ DELETE RECORDS ====================#

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        
        try:
            print("Button Clicked")
        
            if self.var_course.get().strip() == "":
                messagebox.showerror(
                    "Error",
                    "Course Name is required",
                    parent=self.root
                )
        
            
            print("Checking Course")

            cur.execute(
                "SELECT * FROM course WHERE name=?",
                (self.var_course.get(),)
            )

            row = cur.fetchone()

            print("Database Result:", row)

            if row == None:
                messagebox.showerror(
                    "Error",
                    "Plese select course from the list first ",
                    parent=self.root
                )
            else:
                op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                if op==True:
                    cur.execute("DELETE FROM course WHERE name=?",(self.var_course.get(),))
                    con.commit()
                    messagebox.showinfo("Delete","Course deleted Successfully",parent= self.root)
                    self.clear()
                    
        except Exception as ex:
            print("ERROR:", ex)

            messagebox.showerror(
                "Error",
                f"Error due to {str(ex)}",
                parent=self.root
            )

# ================ SEARCH RECORDS =================#
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        try:
            cur.execute(
                "SELECT * FROM course WHERE name LIKE ?",
                (f"%{self.var_search.get()}%",)
            )

            rows = cur.fetchall()

            self.CourseTable.delete(*self.CourseTable.get_children())

            for row in rows:
                self.CourseTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror(
                "Error",
                f"Error due to {str(ex)}",
                parent=self.root
            )

        finally:
            con.close()
# ================ CLEAR RECORD ====================#
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete('1.0',END)  
        self.txt_courseName.config(state=NORMAL)
# ================ FETCH RECORD ====================#
    def get_data(self,ev):
        self.txt_courseName.config(state='readonly')
        self.txt_courseName
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        # print(row)
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        # self.var_search.set(row[4])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])


    # ============ ADD COURSE =============
    # This function adds a new course to the database.
    # It first validates that the course name is provided,
    # then checks whether the course already exists.
    # If the course is not found, it inserts the new course
    # details into the database.

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        try:
                print("Button Clicked")

                if self.var_course.get().strip() == "":
                    messagebox.showerror(
                        "Error",
                        "Course Name is required",
                        parent=self.root
                    )
            
                
                print("Checking Course")

                cur.execute(
                    "SELECT * FROM course WHERE name=?",
                    (self.var_course.get(),)
                )

                row = cur.fetchone()

                print("Database Result:", row)

                if row is not None:
                    messagebox.showerror(
                        "Error",
                        "Course Name already present",
                        parent=self.root
                    )
                else:
                    print("Inserting Data")

                    cur.execute(
                        "INSERT INTO course(name,duration,charges,description) VALUES(?,?,?,?)",
                        (
                            self.var_course.get(),
                            self.var_duration.get(),
                            self.var_charges.get(),
                            self.txt_description.get("1.0", END).strip()
                        )
                    )

                    print("Insert Executed")

                    con.commit()
                    
                    print("Commit Done")

                    messagebox.showinfo(
                        "Success",
                        "Course Added Successfully",
                        parent=self.root
                    )
                    self.show()
                    

        except Exception as ex:
                print("ERROR:", ex)

                messagebox.showerror(
                    "Error",
                    f"Error due to {str(ex)}",
                    parent=self.root
                )
#=============================================UPDATE COURSE========================================================#

    def update(self):
            con = sqlite3.connect(database="rms.db")
            cur = con.cursor()
    
            try:
                    print("Button Clicked")
    
                    if self.var_course.get().strip() == "":
                        messagebox.showerror(
                            "Error",
                            "Course Name is required",
                            parent=self.root
                        )
                
                    
                    print("Checking Course")
    
                    cur.execute(
                        "SELECT * FROM course WHERE name=?",
                        (self.var_course.get(),)
                    )
    
                    row = cur.fetchone()
    
                    print("Database Result:", row)
    
                    if row == None:
                        messagebox.showerror(
                            "Error",
                            "Select Course from list ",
                            parent=self.root
                        )
                    else:
                        print("Updating Data")
    
                        cur.execute(
                            "UPDATE course SET duration=?,charges=?,description=? where name=?",
                            (
                                self.var_duration.get(),
                                self.var_charges.get(),
                                self.txt_description.get("1.0", END).strip(),
                                self.var_course.get()
                            )
                        )
    
                        print("Updation Executed")
    
                        con.commit()
                        
                        print("Commit Done")
    
                        messagebox.showinfo(
                            "Success",
                            "Course Update Successfully",
                            parent=self.root
                        )
                        self.show()
                        
    
            except Exception as ex:
                    print("ERROR:", ex)
    
                    messagebox.showerror(
                        "Error",
                        f"Error due to {str(ex)}",
                        parent=self.root
                    )
#==================== SHOW RECORDS ==================================================#

    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        try:
            cur.execute("SELECT * FROM course")
            rows = cur.fetchall()
            print(rows)

        # Clear existing Treeview data
            self.CourseTable.delete(*self.CourseTable.get_children())

        # Insert fresh data
            for row in rows:
                self.CourseTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror(
                "Error",
                f"Error due to {str(ex)}",
                parent=self.root
            )

        finally:
            con.close()
        
if __name__ == "__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()