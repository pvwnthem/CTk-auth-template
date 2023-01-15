from utils.harvesthwid import harvest
from gui import gui, splash_screen
from gui.auth import login, register
import pickledb
# register needs hwid passed in

instances = {"gui": gui.Gui, "splash_screen": splash_screen.Splash, "login": login.Login, "register": register.Register, "sql": SqliteMod}




if x.select('data', 'name') == []:
    instances["register"](harvest(), instances).mainloop()
else:
    instances["login"](instances).mainloop()



