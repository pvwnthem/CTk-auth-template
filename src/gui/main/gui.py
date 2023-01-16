import eel
import os




    
        
def mainloop(instances):
    dirname = os.path.dirname(__file__)
    eel.init(os.path.join(dirname, "web/"))
    @eel.expose
    def gud(self):
        return instances["jwt"]().jwt_decode(self)
        
    eel.start("index.html")
    

