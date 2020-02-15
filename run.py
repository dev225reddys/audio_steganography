from tkinter import *
import tkinter.filedialog
import tkinter as tk
import sqlite3
import time
import sqlite3
from tkinter import ttk
import datetime
import getopt, os, sys, math, struct, wave
import base64
import ast

dict1={'init':'done!'}

global rdir
cwd=os.getcwd()
rdir=cwd+'/'
cuser=None
            
currentDT = datetime.datetime.now()

LARGE_FONT= ("Verdana", 12)
global admunm,usrnm
admunm=None
usrnm="None"

conn = sqlite3.connect('db-sqlite3/data.db')
with conn:
    cursor=conn.cursor()

global status
status=""

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Audio Steganography")
        self.geometry('500x700')
        container = tk.Frame(self)
        self.cuser=''

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)



        self.frames = {}

        for F in (RootPage, AdminLogin, AdmHmPg):

            frame = F(container,self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(RootPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class RootPage(tk.Frame):

    def printq():
        print ("Hello")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        self.lbl_status = StringVar(parent)
        self.lbl_status.set("waiting input...")
        Label(self,textvariable= self.lbl_status).grid(row=4,column=0,columnspan=2,sticky='W')

        def reg():
            win = Toplevel()
            win.title("Register")
            win.geometry('500x500')

            unm=StringVar()
            pwd=StringVar()
            Email=StringVar()
            name=StringVar()
            
            def database():
                global unm1
                unm1=unm.get()
                pwd1=pwd.get()
                em1=Email.get()
                nm1=name.get()
                if(unm1=='' or pwd1=='' or em1=='' or nm1==''):
                    cp = Label(win, text="No input given! Can't Register",fg='brown',width=40,font=("bold", 10))
                    cp.place(x=100,y=100)
                else:
                    cursor.execute('INSERT INTO user (unm,pwd,name,email) VALUES(?,?,?,?)',(unm1,pwd1,em1,nm1))
                    conn.commit()
                    win.destroy()



             
            label_0 = Label(win, text="Register",width=20,font=("bold", 20))
            label_0.place(x=90,y=53)


            label_1 = Label(win, text="Username",width=20,font=("bold", 10))
            label_1.place(x=80,y=130)

            entry_1 = Entry(win,textvar=unm)
            entry_1.place(x=240,y=130)

            label_1 = Label(win, text="Password",width=20,font=("bold", 10))
            label_1.place(x=80,y=180)

            mobe = Entry(win,textvar=pwd,show="*")
            mobe.place(x=240,y=180)

            label_2 = Label(win, text="Name",width=20,font=("bold", 10))
            label_2.place(x=80,y=230)

            entry_2 = Entry(win,textvar=name)
            entry_2.place(x=240,y=230)


            addr = Label(win, text="Email",width=20,font=("bold", 10))
            addr.place(x=68,y=280)

            addre = Entry(win,textvar=Email)
            addre.place(x=240,y=280)


            Button(win, text='Register',width=20,bg='green',fg='white',command=database).place(x=180,y=340)
            Button(win, text='Cancel',width=20,bg='brown',fg='white',command=win.destroy).place(x=180,y=370)


        label_0 = Label(self, text="Audio Steganography",width=20,font=("bold", 20))
        label_0.place(x=100,y=53)

        label_1 = Label(self, text="Continue by",width=20,font=("default", 14))
        label_1.place(x=100,y=130)


        
        Button(self, text='Login',width=24,bg='brown',fg='white',command=lambda:controller.show_frame(AdminLogin)).place(x=123,y=160)



        label_2 = Label(self, text="Or",width=14,font=("default", 9))
        label_2.place(x=175,y=195)

        Button(self, text='Register',width=24,bg='brown',fg='white',command=reg).place(x=123,y=220)
        


class AdminLogin(tk.Frame):

    cuser=''
    def __init__(self, parent, controller):

        tk.Frame.__init__(self,parent)

        unm=StringVar()
        pwd=StringVar()
        
        def AdmLogCheck():
            unm1=unm.get()
            pwd1=pwd.get()
            self.cuser=unm1

            row=cursor.execute("SELECT `unm`,`pwd` FROM user WHERE unm=? and pwd=?",(unm1,pwd1))
            row=cursor.fetchall()
            le=len(row)
            if(le>0):

                
                AdminLogin.cuser=unm1
                print(AdminLogin.cuser)
                controller.show_frame(AdmHmPg)
            else:
                wp = Label(self, text="Wrong Username or Password!",fg='red',width=40,font=("bold", 10))
                wp.place(x=100,y=100)



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



class StatusBar(tk.Frame):   
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)
        self.variable=StringVar()
        self.label=tk.Label(self, bd=1, relief=SUNKEN, anchor=tk.W,
                           textvariable=self.variable,
                           font=('arial',10,'normal'))
        self.variable.set(status)
        self.label.pack(side=BOTTOM,fill=X)        
        self.pack()


class AdmHmPg(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        def UsrHid():
            win = Toplevel()
            win.geometry('500x500')

            unm=StringVar()
            pwd=StringVar()
            Email=StringVar()
            name=StringVar()
            
            def hidepro():
                try:
                    smg1,smad1,lad1
                except NameError:
                    cp = Label(win, text="File(s) not selected",fg='red',width=40,font=("bold", 10))
                    cp.place(x=100,y=100)

                else:
                    print(smg1,smad1,lad1)

                    soutput_path='hi_process/prsad.wav'
                    citer='smg2smad'
                    hide_data(smad1,smg1,soutput_path,citer)

            def database():

                unm1=unm.get()
                pwd1=pwd.get()
                em1=Email.get()
                nm1=name.get()   
                cursor.execute('INSERT INTO user (unm,pwd,name,email) VALUES(?,?,?,?)',(unm1,pwd1,em1,nm1))
                conn.commit()

            def smg():
                global smg1
                smg1 = tkinter.filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("Text File","*.txt"),("all files","*.*")))  
            def smad():
                global smad1
                smad1 = tkinter.filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("WAVE Audio","*.wav"),("all files","*.*")))  
            def lad():
                global lad1
                lad1 = tkinter.filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("WAVE Audio","*.wav"),("all files","*.*")))  
            def hide_data(sound_path, file_path, output_path,citer):
                if(citer=='smg2smad'):
                    global sound, params, n_frames, n_samples, fmt, mask, smallest_byte,required_LSBs,trig
                    trig='h'
                    def prepare(sound_path):
                        global sound, params, n_frames, n_samples, fmt, mask, smallest_byte,required_LSBs,filesize,trig
                        sound = wave.open(sound_path, "r")


                        params = sound.getparams()
                        num_channels = sound.getnchannels()
                        sample_width = sound.getsampwidth()
                        n_frames = sound.getnframes()
                        n_samples = n_frames * num_channels
                        if (trig=='h'):
                            filesize = os.stat(file_path).st_size
                        else:
                            filesize = os.stat(sound_path).st_size
                        required_LSBs=math.ceil(filesize * 8 / n_samples)
                        print(filesize,required_LSBs)
                        dict1.update({'smglsb':required_LSBs,'smgfs':filesize})
                        print(dict1)


                        if (sample_width == 1):  
                            fmt = "{}B".format(n_samples)
                            
                            mask = (1 << 8) - (1 << required_LSBs)

                            smallest_byte = -(1 << 8)
                        elif (sample_width == 2):  
                            fmt = "{}h".format(n_samples)

                            mask = (1 << 15) - (1 << required_LSBs)
                            smallest_byte = -(1 << 15)
                        else:
                            raise ValueError("File has an unsupported bit-depth")



                    prepare(sound_path)

                    max_bytes_to_hide = (n_samples * required_LSBs) // 8
                    
                    if (filesize > max_bytes_to_hide):
                        required_LSBs = math.ceil(filesize * 8 / n_samples)
                        raise ValueError("Input file too large to hide, "
                                         "requires {} LSBs, using {}"
                                         .format(required_LSBs, required_LSBs))
                    
                    print("Using {} B out of {} B".format(filesize, max_bytes_to_hide))
                    
                    
                    raw_data = list(struct.unpack(fmt, sound.readframes(n_frames)))
                    sound.close()
                    
                    input_data = memoryview(open(file_path, "rb").read())
                    
                    data_index = 0
                    sound_index = 0
                    
                    values = []
                    buffer = 0
                    buffer_length = 0
                    done = False
                    
                    while(not done):
                        while (buffer_length < required_LSBs and data_index // 8 < len(input_data)):

                            buffer += (input_data[data_index // 8] >> (data_index % 8)
                                        ) << buffer_length
                            bits_added = 8 - (data_index % 8)
                            buffer_length += bits_added
                            data_index += bits_added
                            
                        current_data = buffer % (1 << required_LSBs)
                        buffer >>= required_LSBs
                        buffer_length -= required_LSBs

                        while (sound_index < len(raw_data) and
                               raw_data[sound_index] == smallest_byte):

                            values.append(struct.pack(fmt[-1], raw_data[sound_index]))
                            sound_index += 1

                        if (sound_index < len(raw_data)):
                            current_sample = raw_data[sound_index]
                            sound_index += 1

                            sign = 1
                            if (current_sample < 0):

                                current_sample = -current_sample
                                sign = -1

                            altered_sample = sign * ((current_sample & mask) | current_data)

                            values.append(struct.pack(fmt[-1], altered_sample))

                        if (data_index // 8 >= len(input_data) and buffer_length <= 0):
                            done = True
                        
                    while(sound_index < len(raw_data)):

                        values.append(struct.pack(fmt[-1], raw_data[sound_index]))
                        sound_index += 1
                    
                    sound_steg = wave.open(output_path, "w")
                    sound_steg.setparams(params)
                    sound_steg.writeframes(b"".join(values))
                    sound_steg.close()
                    print("Data hidden over {} audio file".format(output_path))
                    
                    if(os.path.exists(output_path)):
                        citer='smad2lad'
                        s2output_path='processed/prlad.wav'
                        hide_data2(lad1,output_path,s2output_path,citer)
                    else:
                        print("File not Found!")

            def hide_data2(sound_path, file_path, output_path,citer):
                if(citer=='smad2lad'):
                    global sound, params, n_frames, n_samples, fmt, mask, smallest_byte,required_LSBs,trig
                    trig='h'
                    def prepare(sound_path):
                        global sound, params, n_frames, n_samples, fmt, mask, smallest_byte,required_LSBs,filesize,trig
                        sound = wave.open(sound_path, "r")


                        params = sound.getparams()
                        num_channels = sound.getnchannels()
                        sample_width = sound.getsampwidth()
                        n_frames = sound.getnframes()
                        n_samples = n_frames * num_channels
                        if (trig=='h'):
                            filesize = os.stat(file_path).st_size
                        else:
                            filesize = os.stat(sound_path).st_size
                        required_LSBs=math.ceil(filesize * 8 / n_samples)
                        print(filesize,required_LSBs)
                        dict1.update({'sadlsb':required_LSBs,'sadfs':filesize})
                        print(dict1)


                        if (sample_width == 1): 
                            fmt = "{}B".format(n_samples)
                            mask = (1 << 8) - (1 << required_LSBs)

                            smallest_byte = -(1 << 8)
                        elif (sample_width == 2):  
                            fmt = "{}h".format(n_samples)
                            mask = (1 << 15) - (1 << required_LSBs)
                            smallest_byte = -(1 << 15)
                        else:
                            # Python's wave module doesn't support higher sample widths
                            raise ValueError("File has an unsupported bit-depth")



                    prepare(sound_path)

                    max_bytes_to_hide = (n_samples * required_LSBs) // 8
                    
                    if (filesize > max_bytes_to_hide):
                        required_LSBs = math.ceil(filesize * 8 / n_samples)
                        raise ValueError("Input file too large to hide, "
                                         "requires {} LSBs, using {}"
                                         .format(required_LSBs, required_LSBs))
                    
                    print("Using {} B out of {} B".format(filesize, max_bytes_to_hide))
                    
                    
                    raw_data = list(struct.unpack(fmt, sound.readframes(n_frames)))
                    sound.close()
                    
                    input_data = memoryview(open(file_path, "rb").read())
                    
                    data_index = 0
                    sound_index = 0
                    
                    values = []
                    buffer = 0
                    buffer_length = 0
                    done = False
                    
                    while(not done):
                        while (buffer_length < required_LSBs and data_index // 8 < len(input_data)):

                            buffer += (input_data[data_index // 8] >> (data_index % 8)
                                        ) << buffer_length
                            bits_added = 8 - (data_index % 8)
                            buffer_length += bits_added
                            data_index += bits_added
                            
                        current_data = buffer % (1 << required_LSBs)
                        buffer >>= required_LSBs
                        buffer_length -= required_LSBs

                        while (sound_index < len(raw_data) and
                               raw_data[sound_index] == smallest_byte):

                            values.append(struct.pack(fmt[-1], raw_data[sound_index]))
                            sound_index += 1

                        if (sound_index < len(raw_data)):
                            current_sample = raw_data[sound_index]
                            sound_index += 1

                            sign = 1
                            if (current_sample < 0):

                                current_sample = -current_sample
                                sign = -1


                            altered_sample = sign * ((current_sample & mask) | current_data)

                            values.append(struct.pack(fmt[-1], altered_sample))

                        if (data_index // 8 >= len(input_data) and buffer_length <= 0):
                            done = True
                        
                    while(sound_index < len(raw_data)):

                        values.append(struct.pack(fmt[-1], raw_data[sound_index]))
                        sound_index += 1
                    
                    cp = Label(win, text="Successfully Hidden!",fg='green',width=40,font=("bold", 10))
                    cp.place(x=100,y=100)
                    sound_steg = wave.open(output_path, "w")
                    sound_steg.setparams(params)
                    sound_steg.writeframes(b"".join(values))
                    sound_steg.close()
                    print("Data hidden over {} audio file".format(output_path))

                    enc=base64.b64encode(bytes(repr(dict1), "utf-8"))
                    file=open('recover.key','wb')
                    file.write(enc)

                    winhi=Toplevel()
                    winhi.geometry('500x500')
                    winhi.title('Hide Success!')

                    label_0 = Label(winhi, text="Hidden Successfully!",width=20,font=("bold", 20))
                    label_0.place(x=90,y=53)
                    label_0 = Label(winhi, text="Files are in following locations",width=25,font=("bold", 15))
                    label_0.place(x=90,y=83)

                    label_1 = Label(winhi, text="Large Audio",width=20,font=("bold", 10))
                    label_1.place(x=80,y=130)
                    entry_1 = Entry(winhi)
                    entry_1.insert(0,"processed/prlad.wav")
                    entry_1.place(x=240,y=130)

                    label_2 = Label(winhi, text="Key",width=20,font=("bold", 10))
                    label_2.place(x=80,y=230)

                    entry_2 = Entry(winhi)
                    entry_2.insert(0,"recover.key")
                    entry_2.place(x=240,y=230)

                    Button(winhi, text='Done!',width=20,bg='green',fg='white',command=winhi.destroy).place(x=180,y=280)

             
            label_0 = Label(win, text="Hide",width=20,font=("bold", 20))
            label_0.place(x=90,y=53)
            ttk.Separator(win).place(x=0, y=90, relwidth=1)

            label_1 = Label(win, text="Secret Msg",width=20,font=("bold", 10))
            label_1.place(x=80,y=130)

            Button(win, text='SELECT',width=15,bg='brown',fg='white',command=smg).place(x=260,y=130)

            label_1 = Label(win, text="Small Audio",width=20,font=("bold", 10))
            label_1.place(x=80,y=180)

            Button(win, text='SELECT',width=15,bg='brown',fg='white',command=smad).place(x=260,y=180)

            label_2 = Label(win, text="Large Audio",width=20,font=("bold", 10))
            label_2.place(x=80,y=230)


            Button(win, text='SELECT',width=15,bg='brown',fg='white',command=lad).place(x=260,y=230)




            Button(win, text='Proceed',width=20,bg='green',fg='white',command=hidepro).place(x=180,y=340)
            Button(win, text='Cancel',width=20,bg='red',fg='white',command=win.destroy).place(x=180,y=370)


        def UsrRec():

            win = Toplevel()
            win.geometry('500x500')
            win.title("Recover")

            def RecPro():
                try:
                    rlad1,rkey1
                except NameError:
                    cp = Label(win, text="File(s) not selected",fg='red',width=40,font=("bold", 10))
                    cp.place(x=100,y=100)

                else:
                    file=open(rkey1,'r')
                    dec=file.read()
                    deco=base64.b64decode(dec).decode("utf-8", "ignore")
                    global dict1
                    dict1=ast.literal_eval(deco)
                    global smglsb,smgfs,sadlsb,sadfs
                    smglsb=dict1['smglsb']
                    smgfs=dict1['smgfs']
                    sadlsb=dict1['sadlsb']
                    sadfs=dict1['sadfs']

                    outp='re_process/smad.wav'
                    recover_data(rlad1,outp,sadlsb,sadfs)

            def rlad():
                global rlad1
                rlad1 = tkinter.filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("WAVE Audio","*.wav"),("all files","*.*")))
            def rkey():
                global rkey1
                rkey1 = tkinter.filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("Key File","*.key"),("all files","*.*")))  

            def recover_data(sound_path, output_path, num_lsb, bytes_to_recover):
                global sound, n_frames, n_samples, fmt, smallest_byte

                def prepare(sound_path):
                    global sound, params, n_frames, n_samples, fmt, mask, smallest_byte
                    sound = wave.open(sound_path, "r")
                    
                    params = sound.getparams()
                    num_channels = sound.getnchannels()
                    sample_width = sound.getsampwidth()
                    n_frames = sound.getnframes()
                    n_samples = n_frames * num_channels

                    if (sample_width == 1): 
                        fmt = "{}B".format(n_samples)

                        mask = (1 << 8) - (1 << num_lsb)
                        smallest_byte = -(1 << 8)
                    elif (sample_width == 2):  
                        fmt = "{}h".format(n_samples)
                        mask = (1 << 15) - (1 << num_lsb)

                        smallest_byte = -(1 << 15)
                    else:
                        raise ValueError("File has an unsupported bit-depth")

                prepare(sound_path)

                raw_data = list(struct.unpack(fmt, sound.readframes(n_frames)))
                mask = (1 << num_lsb) - 1
                output_file = open(output_path, "wb+")
                
                data = bytearray()
                sound_index = 0 
                buffer = 0
                buffer_length = 0
                sound.close()

                while (bytes_to_recover > 0):
                    
                    next_sample = raw_data[sound_index]
                    if (next_sample != smallest_byte):

                        buffer += (abs(next_sample) & mask) << buffer_length
                        buffer_length += num_lsb
                    sound_index += 1
                    
                    while (buffer_length >= 8 and bytes_to_recover > 0):

                        current_data = buffer % (1 << 8)
                        buffer >>= 8
                        buffer_length -= 8
                        data += struct.pack('1B', current_data)
                        bytes_to_recover -= 1

                output_file.write(bytes(data))
                output_file.close()
                print("Data recovered to {} Wave file".format(output_path))
                op='processed/recovered.txt'
                recover_data2(output_path,op,smglsb,smgfs)

            def recover_data2(sound_path, output_path, num_lsb, bytes_to_recover):
                global sound, n_frames, n_samples, fmt, smallest_byte

                def prepare(sound_path):
                    global sound, params, n_frames, n_samples, fmt, mask, smallest_byte
                    sound = wave.open(sound_path, "r")
                    
                    params = sound.getparams()
                    num_channels = sound.getnchannels()
                    sample_width = sound.getsampwidth()
                    n_frames = sound.getnframes()
                    n_samples = n_frames * num_channels

                    if (sample_width == 1):  
                        fmt = "{}B".format(n_samples)
                        mask = (1 << 8) - (1 << num_lsb)

                        smallest_byte = -(1 << 8)
                    elif (sample_width == 2):  
                        fmt = "{}h".format(n_samples)
                        mask = (1 << 15) - (1 << num_lsb)
                        smallest_byte = -(1 << 15)
                    else:
                        raise ValueError("File has an unsupported bit-depth")
                        
                prepare(sound_path)

                raw_data = list(struct.unpack(fmt, sound.readframes(n_frames)))
                mask = (1 << num_lsb) - 1
                output_file = open(output_path, "wb+")
                
                data = bytearray()
                sound_index = 0 
                buffer = 0
                buffer_length = 0
                sound.close()

                while (bytes_to_recover > 0):
                    
                    next_sample = raw_data[sound_index]
                    if (next_sample != smallest_byte):

                        buffer += (abs(next_sample) & mask) << buffer_length
                        buffer_length += num_lsb
                    sound_index += 1
                    
                    while (buffer_length >= 8 and bytes_to_recover > 0):
                        current_data = buffer % (1 << 8)
                        buffer >>= 8
                        buffer_length -= 8
                        data += struct.pack('1B', current_data)
                        bytes_to_recover -= 1

                output_file.write(bytes(data))
                output_file.close()
                print("Data recovered to {} text file".format(output_path))

                def dlg():
                    cp = Label(win, text="Successfully Recovered!",fg='green',width=40,font=("bold", 10))
                    cp.place(x=100,y=100)
       

                    winhi=Toplevel()
                    winhi.geometry('500x500')
                    winhi.title('Recover Success!')

                    label_0 = Label(winhi, text="Recovered Successfully!",width=20,font=("bold", 20))
                    label_0.place(x=90,y=53)
                    label_0 = Label(winhi, text="Files are in following locations",width=25,font=("bold", 15))
                    label_0.place(x=90,y=83)

                    label_1 = Label(winhi, text="Small Audio",width=20,font=("bold", 10))
                    label_1.place(x=80,y=130)
                    entry_1 = Entry(winhi)
                    entry_1.insert(0,"re_process/smad.wav")
                    entry_1.place(x=240,y=130)

                    label_2 = Label(winhi, text="Text File",width=20,font=("bold", 10))
                    label_2.place(x=80,y=230)

                    entry_2 = Entry(winhi)
                    entry_2.insert(0,"processed/recovered.txt")
                    entry_2.place(x=240,y=230)

                    Button(winhi, text='Done!',width=20,bg='green',fg='white',command=winhi.destroy).place(x=180,y=280)

                dlg()


            label_0 = Label(win, text="Recover",width=20,font=("bold", 20))
            label_0.place(x=90,y=53)
            ttk.Separator(win).place(x=0, y=90, relwidth=1)

            label_1 = Label(win, text="Audio File",width=20,font=("bold", 10))
            label_1.place(x=80,y=130)

            Button(win, text='SELECT',width=15,bg='brown',fg='white',command=rlad).place(x=260,y=130)

            label_1 = Label(win, text="Recovery Key",width=20,font=("bold", 10))
            label_1.place(x=80,y=180)
            Button(win, text='SELECT',width=15,bg='brown',fg='white',command=rkey).place(x=260,y=180)

            Button(win, text='Proceed',width=20,bg='green',fg='white',command=RecPro).place(x=180,y=340)
            Button(win, text='Cancel',width=20,bg='red',fg='white',command=win.destroy).place(x=180,y=370)            





        def AdmChPwd():
            win=Toplevel()
            win.geometry('500x500')

            crpwd=StringVar()
            nwpwd=StringVar()
            cnwpwd=StringVar()
            nwpwd1=StringVar()

            def updAdmPwd():
                crpwd1=crpwd.get()
                nwpwd1=nwpwd.get()
                print(nwpwd1)
                cursor.execute('UPDATE admin set pwd=? where unm="admin"',(nwpwd1,))
                conn.commit()
                cp = Label(win, text="Succesfully Changed Password!",fg='Green',width=40,font=("bold", 10))
                cp.place(x=100,y=90)
                cp = Label(win, text="Please Close this Window.",fg='red',width=40,font=("bold", 10))
                cp.place(x=100,y=110)
                
                Button(win, text='Exit',width=24,bg='brown',fg='white',command=win.destroy).place(x=180,y=320)

            
            def vrPwd():
                n=1
                cpwd=crpwd.get()
                row=cursor.execute("SELECT `pwd` FROM admin where id=1")
                row=cursor.fetchall()
                print(row[0][0])
                if(cpwd==row[0][0]):
                    icrpwd.config(state="disable")
                    Button(win, text='Verified',width=24,bg='green',fg='white',state="disable").place(x=123,y=180)
                    #vrbtn.config(text="Verified")
                    mob = Label(win, text="New Password",width=20,font=("bold", 10))
                    mob.place(x=80,y=250)

                    mobe = Entry(win,textvar=nwpwd)
                    mobe.place(x=240,y=250)

                    Button(win, text='Submit',width=24,bg='brown',fg='white',command=updAdmPwd).place(x=180,y=320)

                
            label_0 = Label(win, text="Change Password",width=20,font=("bold", 20))
            label_0.place(x=100,y=53)

            Button(win, text='Exit',width=8,bg='black',fg='white',command=win.destroy).place(x=390,y=53)

            label_1 = Label(win, text="Current Password",width=20,font=("bold", 10))
            label_1.place(x=80,y=130)

            icrpwd = Entry(win,textvar=crpwd)
            icrpwd.place(x=240,y=130)

            vrbtn=Button(win, text='Verify',width=24,bg='brown',fg='white',command=vrPwd).place(x=123,y=180)


        label_0 = Label(self, text="Hello, User!",width=20,font=("bold", 20))
        label_0.place(x=100,y=53)


        Button(self, text='Signout',width=8,bg='black',fg='white',command=lambda:controller.show_frame(RootPage)).place(x=390,y=53)

        ttk.Separator(self).place(x=0, y=120, relwidth=1)
        label_1 = Label(self, text="Steganography",width=20,font=("default", 14))
        label_1.place(x=100,y=130)
        
        
        Button(self, text='Hide',width=24,bg='brown',fg='white',command=UsrHid).place(x=123,y=160)


        Button(self, text='Extract',width=24,bg='brown',fg='white',command=UsrRec).place(x=123,y=190)

        ttk.Separator(self).place(x=0, y=240, relwidth=1)


        label_2 = Label(self, text="User Settings",width=20,font=("default",14))
        label_2.place(x=100,y=260)
        
        
        Button(self, text='Change Password',width=24,bg='brown',fg='white',command=AdmChPwd).place(x=123,y=290)

        ttk.Separator(self).place(x=0, y=360, relwidth=1)


app = SeaofBTCapp()
app.mainloop()