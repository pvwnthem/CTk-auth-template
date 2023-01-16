import eel
import os



class Gui:
    def __init__(self, instances):
        self.instances = instances
        
    def mainloop(self):

        dirname = os.path.dirname(__file__)
        eel.init(os.path.join(dirname, "web/"))
        eel.start("index.html")


    