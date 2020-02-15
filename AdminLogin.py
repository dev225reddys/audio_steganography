class AdminLogin(tk.Frame):


    def __init__(self, parent, controller):

        tk.Frame.__init__(self,parent)



        #aunm=StringVar()
        #apwd=StringVar()
        unm=StringVar()
        pwd=StringVar()
        
        def AdmLogCheck():
            # global unm1
            unm1=unm.get()
            pwd1=pwd.get()
            # print(unm1)
            self.cuser=unm1

            # print(cuser)
            row=cursor.execute("SELECT `unm`,`pwd` FROM user WHERE unm=? and pwd=?",(unm1,pwd1))
            row=cursor.fetchall()
            le=len(row)
            if(le>0):
                #print ("Login Success!")
                cp = Label(self, text="Succesfully Logged in! Redirecting soon..!!",fg='Green',width=40,font=("bold", 10))
                cp.place(x=100,y=100)
                #time.sleep(2)

                """cp = Label(self, text="Succesfully Logged in! Redirecting soon..!!",fg='Green',width=40,font=("bold", 10))
                cp.place(x=100,y=100)
                
                """
                admunm="admin"
                controller.show_frame(AdmHmPg)
            else:
                wp = Label(self, text="Wrong Username or Password!",fg='red',width=40,font=("bold", 10))
                wp.place(x=100,y=100)
                #print("Wrong Cred")

            """cunm="a"
            cpwd="t"

            if(cunm==unm1 and cpwd==pwd1):
                status="Admin Login Success"
                print (status)
                time.sleep(0.5)
                status="Redirecting Now"
                print (status)
                time.sleep(0.5)
                status="Welcome Admin"
                print (status)
                #print("Login Success")
                #StatusBar1("Login Sucess.. Redirecting now")
                #self.variable.set("Login Success")            
            else:
                print("Wrong Cred")"""



        


        label_0 = Label(self, text="User Login",width=20,font=("bold", 20))
        label_0.place(x=100,y=53)

        label_1 = Label(self, text="Username :",width=20,font=("bold", 10))
        label_1.place(x=80,y=130)

        unm = Entry(self)
        unm.place(x=240,y=130)

        plbl= Label(self, text="Password :",width=20,font=("bold", 10))
        plbl.place(x=80,y=180)

        pwd = Entry(self,show="*")
        pwd.place(x=240,y=180)

        Button(self, text='Login',width=13,bg='green',fg='white',command=AdmLogCheck).place(x=123,y=230)
        Button(self, text='Cancel',width=13,bg='brown',fg='white',command=lambda:controller.show_frame(RootPage)).place(x=273,y=230)
