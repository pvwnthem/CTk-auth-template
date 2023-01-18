import subprocess
import os



#build exe



class Build:
    
        def __init__(self, path):
    
            self.path = path



        def build(self):
    
            print("Building...")
    
            subprocess.call(['pyinstaller', '--onefile', '--noconsole', '--distpath', 'C:/M00N/dist', '--workpath', 'C:/M00N', self.path])

            return os.path.abspath('C:/M00N/dist')
            print("Done!")
    