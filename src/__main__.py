from utils.harvesthwid import harvest
from utils.sqlitemod import SqliteMod
from gui import gui, splash_screen
from gui.auth import login, register

# register needs hwid passed in

instances = {"gui": gui.Gui, "splash_screen": splash_screen.Splash, "login": login.Login, "register": register.Register, "sql": SqliteMod}




sql = instances["sql"]('data.db')
sql.create_table('data', 'token text')

if sql.select('data', 'token') == []:
    reg = instances["register"]()
    reg.HWID = harvest()



