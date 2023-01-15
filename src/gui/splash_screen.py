import customtkinter as ctk
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter.ttk import Progressbar
import time
ctk.set_appearance_mode("Dark") # Set the apperance mode to dark
ctk.set_default_color_theme("blue") # Set the default color theme to blue


class Gui(ctk.CTk): # The class that will be the main window of the application

    WIDTH = 780 # The size of the window
    HEIGHT = 520 # The size of the window 

    def __init__(self): # The constructor of the class
        super().__init__() # Call the super class constructor

        self.title("Person Generator And Manager By @pvwn") # Set the title of the window
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}") # Set the size of the window
        #self.protocol("WM_DELETE_WINDOW", self.on_closing) # When the user clicks the X button on the window

        text="Welcome {user}!" 

        label = ctk.CTkLabel(master=self, text="" , font=("Arial", 20), text_color="#2273f5")
        label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        out = ""
        for letter in text:
            out += letter 
            label.configure(text=out)
            self.update()
            time.sleep(0.25)
        

        

        







if __name__ == "__main__":
    gui = Gui() # Create an instance of the Gui class
    gui.mainloop() # Start the mainloop of the application