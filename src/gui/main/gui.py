import eel
import os




    
        
def mainloop(instances):
    dirname = os.path.dirname(__file__)
    eel.init(os.path.join(dirname, "web/"))
    @eel.expose
    def gud():
        print('called')
        return instances["jwt"](instances).jwt_decode()
        
    eel.start("index.html")
    

