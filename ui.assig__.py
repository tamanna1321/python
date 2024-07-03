from tkinter import*
from tkinter import messagebox
import re
class Home:
    def __init__(self):
     self.root=Tk()
     self.root.geometry('800x600')
     self.root.resizable(False,False)
     self.root.title("Kindly enter the details")
     self.frame1=Frame(self.root,height=300,width=400)
     self.frame1.place(x=140,y=50)

     self.name=Label(self.frame1,text="Name",font=('Georgia',15,'normal'),bg='#fc0394')
     self.name.place(x=15,y=50)
     self.name_entry=Entry(self.frame1,font=('Georgia',15,'normal'),bg='#03fcd3')
     self.name_entry.place(x=170,y=50)

     self.mail=Label(self.frame1,text="Email",font=('Georgia',15,'normal'),bg='#fc0b03')
     self.mail.place(x=15,y=90)
     self.mail_entry=Entry(self.frame1,font=('Georgia',15,'normal'),bg='#88fc03')
     self.mail_entry.place(x=170,y=90)

     self.pwd=Label(self.frame1,text="Password",font=('Georgia',15,'normal'),bg='#03fc98')
     self.pwd.place(x=15,y=130)
     self.pass_entry=Entry(self.frame1,font=('Georgia',15,'normal'),show="*",bg='#fc03e3')
     self.pass_entry.place(x=170,y=130)

     self.con=Label(self.frame1,text="Contact number",font=('Georgia',15,'normal'),bg='#0352fc')
     self.con.place(x=15,y=170)
     self.contact_entry=Entry(self.frame1,font=('Georgia',15,'normal'),bg='#03fc66')
     self.contact_entry.place(x=170,y=170)

     self.btn= Button(self.frame1,text="Submit", font=('Georgia',15,'normal'),command=self.getVal)
     self.btn.place(x=150, y=230)
            
     self.root.mainloop()
    def getVal(self):
       Name=self.name_entry.get()
       Mail=self.mail_entry.get()
       Password=self.pass_entry.get()
       Contactnumber=self.contact_entry.get()
       
       print(f"Name:'{Name}'")
       print(f"Email:'{Mail}'")
       print(f"Password:'{Password}'")
       print(f"Contact number:'{Contactnumber}'")

       name_pattern=r"^[a-zA-z0-9_]{3,20}$"
       email_pattern=r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
       password_pattern=r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
       Contact_pattern=r"[6-9]{1}\d{9}"

       if re.match(name_pattern,Name):
          print("It's a valid Name")
       else:
          print("Invalid Username")
          messagebox.showerror("Invalid Input")
          return
       if re.match(email_pattern,Mail):
          print("Valid mail")
       else:
          print("Invalid mail")
          messagebox.showerror("Invalid input")
          return   
       if re.match(password_pattern,Password):
          print("Valid password")
       else:
          print("Invalid password") 
          messagebox.showerror("Invalid input")
          return
       if re.match(Contact_pattern,Contactnumber):
          print("Valid Contact Number")
       else:
          print("Invalid Contact Number")
          messagebox.showerror("Invalid input")
          return
       messagebox.showinfo("Details entered successfully")         
obj=Home()  





       
        
        
     




