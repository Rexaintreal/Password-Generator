import tkinter
from tkinter.ttk import *
import customtkinter 
import random
import random
import array
import clipboard

class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = customtkinter.CTkLabel(self,font=("",20))
        self.label.grid(row=0, column=0, padx=20)
        with open('passwords.txt') as f:
          contents = f.read()
          f.close()
          if 1 == 1:
              self.label.configure(text=contents)

class my_tab(customtkinter.CTkTabview):

    def generate_pass(self):
        global password
        MAX_LEN = 12
        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                    'z']
        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '<']
        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
        rand_digit = random.choice(DIGITS)
        rand_upper = random.choice(UPCASE_CHARACTERS)
        rand_lower = random.choice(LOCASE_CHARACTERS)
        rand_symbol = random.choice(SYMBOLS)
        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
        for x in range(MAX_LEN - 4):
            temp_pass = temp_pass + random.choice(COMBINED_LIST)
            temp_pass_list = array.array('u', temp_pass)
            random.shuffle(temp_pass_list)
            password = ""
        for x in temp_pass_list:
            password = password + x
        if 1 == 1:
            self.passlabel.configure(text=password)
    def save_pass(self):
           with open('passwords.txt', 'a+') as f:
               f.write("\t\t"+password+"\n")
               f.close()
           if 1 == 1:
               text=password
    def copy_pass(self):
        clipboard.copy(password)

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.add("Generate")
        self.add("Saved Passwords")
        self.passlabel=customtkinter.CTkLabel(master=self.tab("Generate"),
                                              font=("",20),
                                              text="Password")
        self.passlabel.place(relx=0.5,rely=0.3,anchor=tkinter.CENTER)
        self.generatebutton=customtkinter.CTkButton(master=self.tab("Generate"),
                                                    font=("",20),
                                                    text="Generate Password",
                                                    command=self.generate_pass)
        self.generatebutton.place(relx=0.30,rely=0.5,anchor=tkinter.CENTER)
        self.savebutton=customtkinter.CTkButton(master=self.tab("Generate"),
                                                    font=("",20),
                                                    text="Save Password",
                                                    command=self.save_pass)
        self.savebutton.place(relx=0.70,rely=0.5,anchor=tkinter.CENTER)
        self.my_frame = MyFrame(master=self.tab("Saved Passwords"), width=530, height=330, corner_radius=0, fg_color="transparent")
        self.my_frame.grid(row=0, column=0, sticky="nsew")
        self.copy=customtkinter.CTkButton(master=self.tab("Generate"),
                                          font=("",20),
                                          text="Copy Password",
                                          command=self.copy_pass)
        self.copy.place(relx=0.5,rely=0.7,anchor=tkinter.CENTER)

class Application(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("640x480")
        self.title("Password Generator")
        self.fg_color='steel blue'
        self.maxsize(width=640,height=480)
        self.minsize(width=640,height=480)
        self.Tab=my_tab(master=self,width=600,height=435,)
        self.Tab.configure(fg_color='medium orchid')
        self.Tab.configure(border_color='medium orchid')
        self.Tab.grid(row=0,column=0,padx=20,pady=20)
        
application = Application()

application.mainloop()
