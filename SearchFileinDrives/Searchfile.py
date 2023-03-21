import os
import threading


class SearchFilesDrives(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.path=[]

    def searchfiles(self,drives,filename):
        self.drive=drives
        self.filename=filename
        for root,dir,files in os.walk(self.drive):
            for f in files:
                if f==self.filename:
                    self.path.append(os.path.join(root,filename))
        return self.path
    def run(self)->None:
        self.searchfiles(self.drive,self.filename)
