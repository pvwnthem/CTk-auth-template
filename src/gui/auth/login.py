import customtkinter as ctk
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter.ttk import Progressbar
import time
ctk.set_appearance_mode("Dark") # Set the apperance mode to dark
ctk.set_default_color_theme("blue") # Set the default color theme to blue


class Login(ctk.CTk): # The class that will be the main window of the application

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

        username_entry = ctk.CTkEntry(master=self, width=240)
        username_entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

        password_entry = ctk.CTkEntry(master=self, width=240)
        password_entry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)



if __name__ == "__main__":
    gui = Login()
    gui.mainloop()
        

        

        





