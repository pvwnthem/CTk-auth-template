from utils.harvesthwid import harvest
from gui import gui, splash_screen
from gui.auth import login, register
import tinydb
# register needs hwid passed in

x = tinydb.TinyDB("db.json")
User = tinydb.Query()
instances = {"gui": gui.Gui, "splash_screen": splash_screen.Splash, "login": login.Login, "register": register.Register, "db": x}





if x.search(User.username.exists()) == [] :
    z = instances["register"](harvest(), instances)
    z.mainloop()
    
    


if x.search(User.token.exists()) != []:
    z = instances["login"](instances)
    z.mainloop()

else:
    z = instances["login"](instances)
    z.mainloop()

    




