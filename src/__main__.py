from utils.harvesthwid import harvest
from gui import  splash_screen
from gui.main.gui import mainloop
from gui.auth import login, register
from utils.jwt import Jwt

import tkinter
import customtkinter 
import requests
import tinydb
import jwt
import tinydb
# register needs hwid passed in

x = tinydb.TinyDB("db.json")
User = tinydb.Query()

instances = { "splash_screen": splash_screen.Splash, "login": login.Login, "register": register.Register, "db": x, "jwt": Jwt, "harvest": harvest, "main": mainloop}





if x.search(User.token.exists()) == [] :
    z = instances["register"](harvest(), instances)
    z.mainloop()
    
    


if x.search(User.token.exists()) != []:
    z = instances["splash_screen"](instances)
    z.mainloop()

else:
    z = instances["login"](instances)
    z.mainloop()

    




