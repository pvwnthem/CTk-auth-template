from utils.harvesthwid import harvest
from gui import gui, splash_screen
from gui.auth import login, register
import tinydb
# register needs hwid passed in

x = tinydb.TinyDB("db.json")
instances = {"gui": gui.Gui, "splash_screen": splash_screen.Splash, "login": login.Login, "register": register.Register, "db": x}




if x.get("name") == False:
    instances["register"](harvest(), instances).mainloop()
else:
    instances["login"](instances).mainloop()



