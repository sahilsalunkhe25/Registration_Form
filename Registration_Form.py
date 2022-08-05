from tkinter import *

import PIL
from PIL import Image,ImageTk
from tkinter import ttk

class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")

        # ----------- Background ----------------
        image = PIL.Image.open(r"C:\Users\Admin11\Desktop\Student Registration Form\images/e_commerce_registration_form_template_thumb (1).png")
        self.bg = ImageTk.PhotoImage(image)
        bg = Label(self.root, image=self.bg)
        bg.place(x=250,y=0,relwidth=1,relheight=1)
        bg.pack()

        #-----------Left Image-------------------
        image1 = PIL.Image.open(r"images/sMSHFr.png")
        self.left = ImageTk.PhotoImage(image1)
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

        #---------------Frame--------------------

        frame1 = Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height =500)

        #------------Title-----------------------

        title = Label(frame1,text = "REGISTER HERE",font=("times new roman",20,"bold"),bg = "white",fg = "purple").place(x=50,y=30)

        #---------Row1---------------------------
        self.var_fname = StringVar()
        f_name = Label(frame1,text = "First Name",font=("times new roman",15,"bold"),bg = "white",fg = "black").place(x=50,y=100)
        txt_fname = Entry(frame1,font =("times new roman",15),bg = "light grey",textvariable = self.var_fname).place(x=50,y=130,width =250)

        l_name = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=370, y=100)
        txt_lname = Entry(frame1, font=("times new roman", 15), bg="light grey").place(x=370, y=130, width=250)

        #-----------------Row 2--------------

        contact_info = Label(frame1, text="Contact No.", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=170)
        txt_cont = Entry(frame1, font=("times new roman", 15), bg="light grey").place(x=50, y=200, width=250)

        Email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white",fg="black").place(x=370, y=170)
        txt_email = Entry(frame1, font=("times new roman", 15), bg="light grey").place(x=370, y=200, width=250)

        #----------------------Row3---------------

        question = Label(frame1, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=50,y=240)
        cmb_quest = ttk.Combobox(frame1, font=("times new roman", 13),state='readonly',justify=CENTER)
        cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Favourite Sport")
        cmb_quest.place(x=50, y=270, width=250)
        cmb_quest.current(0)

        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=370,
                                                                                                                  y=240)
        txt_ans = Entry(frame1, font=("times new roman", 15), bg="light grey").place(x=370, y=270, width=250)

        #-------------Row4---------------------------

        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white",fg="black").place(x=50, y=310)
        txt_pass = Entry(frame1, font=("times new roman", 15), bg="light grey").place(x=50, y=340, width=250)

        conf_password = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=370,y=310)
        txt_conf = Entry(frame1, font=("times new roman", 15), bg="light grey").place(x=370, y=340, width=250)

        #---------Terms----------------------------
        chk = Checkbutton(frame1,text="I Agree To All Terms & Conditions",onvalue=1,offvalue=0,bg="white",font=("Times New Roman",12)).place(x=50,y=380)

        image3 = PIL.Image.open(r"images/register (1).png")
        self.btn_img = ImageTk.PhotoImage(image3)
        btn_register = Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command = self.register_data()).place(x=50,y=420)
        btn_login = Button(self.root,text="Sign In",font=("times new roman",20),bd=0,cursor="hand2").place(x=200,y=460,width=180)

    def register_data(self):
        print(self.var_fname.get())








root = Tk()
object = Register(root)
root.mainloop()