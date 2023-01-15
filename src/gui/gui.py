import customtkinter as ctk
import tkinter as tk
import tkinter.messagebox as mbox

ctk.set_apperance_mode("Dark")
ctk.set_default_color_theme("blue")


class Gui(ctk.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("Person Generator And Manager By @pvwn")

        


