import customtkinter as ctk
import tkinter as tk
import tkinter.messagebox as mbox

ctk.set_appearance_mode("Dark") # Set the apperance mode to dark
ctk.set_default_color_theme("blue") # Set the default color theme to blue


class Gui(ctk.CTk): # The class that will be the main window of the application

    WIDTH = 780 # The size of the window
    HEIGHT = 520 # The size of the window 

    def __init__(self): # The constructor of the class
        super().__init__() # Call the super class constructor

        self.title("Person Generator And Manager By @pvwn") # Set the title of the window
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}") # Set the size of the window
        self.protocol("WM_DELETE_WINDOW", self.on_closing) # When the user clicks the X button on the window


         # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)


        # create sidebar with widgets





if __name__ == "__main__":
    gui = Gui() # Create an instance of the Gui class
    gui.mainloop() # Start the mainloop of the application