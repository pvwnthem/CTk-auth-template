import customtkinter as ctk
import tkinter as tk
import tkinter.messagebox as mbox
import requests
import subprocess

ctk.set_appearance_mode("Dark") # Set the apperance mode to dark
ctk.set_default_color_theme("blue") # Set the default color theme to blue


class Register(ctk.CTk): # The class that will be the main window of the application

    WIDTH = 780 # The size of the window
    HEIGHT = 520 # The size of the window 

    def __init__(self): # The constructor of the class
        super().__init__() # Call the super class constructor

        self.title("Logger By @pvwn") # Set the title of the window
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}") # Set the size of the window
        #self.protocol("WM_DELETE_WINDOW", self.on_closing) # When the user clicks the X button on the window


        username_label = ctk.CTkLabel(master=self, text="Username: ", font=("Arial", 12), text_color="#2273f5")
        username_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        password_label = ctk.CTkLabel(master=self, text="Password: ", font=("Arial", 12), text_color="#2273f5")
        password_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        invite_label = ctk.CTkLabel(master=self, text="Invite Code: ", font=("Arial", 12), text_color="#2273f5")
        invite_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        invite_entry = ctk.CTkEntry(master=self, width=240)
        invite_entry.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

        username_entry = ctk.CTkEntry(master=self, width=240)
        username_entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

        password_entry = ctk.CTkEntry(master=self, width=240)
        password_entry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

        login_button = ctk.CTkButton(master=self, text="Register", width=240, height=40, command=lambda: self.register(username_entry.get(), password_entry.get(), invite_entry.get()))
        login_button.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

    
    def register(self, username, password, invite):
        x = requests.post('http://localhost:8080/auth/register', data={'username': username, 'password': password,  'invite': invite})
        print(x.status_code)
        if x.status_code == 200:
            mbox.showinfo("Register", "Register Successful, Please Login")
        else:
            mbox.showinfo("Register", "Register Failed, Please Try Again")


        

        





if __name__ == "__main__": # If this file is the main file
    app = Register() # Create an instance of the class
    app.mainloop() # Start the main loop