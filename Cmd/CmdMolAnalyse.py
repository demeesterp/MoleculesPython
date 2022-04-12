from glob import glob
import json
from os import read
from pathlib import Path, PurePath, PureWindowsPath


class CmdMolAnalyse:
    def process(self, basePath):
        files = self.ListMolecules(basePath)
        newlist = []
        for file in files:
            f = open(file, "r")
            fileData = f.read()            
            newlist.append(json.loads(fileData))
            f.close()

        print(len(newlist))




    def ListMolecules(self, basePath):        
        path = Path(basePath)        
        return list(path.glob('**/*.json'))