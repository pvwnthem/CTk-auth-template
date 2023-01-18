import subprocess




#build exe



class Build:
    
        def __init__(self, path):
    
            self.path = path



        def build(self):
    
            print("Building...")
    
            subprocess.call(['pyinstaller', '--onefile', '--noconsole', '--distpath', 'C:/M00N/dist', self.path])
    
            print("Done!")
    