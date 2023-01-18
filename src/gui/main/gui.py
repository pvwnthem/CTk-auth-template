import eel
import os




    
        
def mainloop(instances):
    dirname = os.path.dirname(__file__)
    eel.init(os.path.join(dirname, "web/"))
    @eel.expose
    def gud():
        return instances["jwt"](instances).jwt_decode()
    @eel.expose
    def build():
        return instances["build"]('C:/M00N/src/test.py').build()


    
        
    eel.start("index.html")
    

