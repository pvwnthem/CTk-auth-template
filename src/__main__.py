from utils.harvesthwid import harvest
from utils.sqlitemod import SqliteMod
from gui import gui, splash_screen
from gui.auth import login, register

# register needs hwid passed in

instances = {"gui": gui.Gui, "splash_screen": splash_screen.Splash, "login": login.Login, "register": register.Register}

SqliteMod().create_table("user", "username text, password text, hwid text, invite text")

