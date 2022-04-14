from glob import glob
import json
from os import read
from pathlib import Path, PurePath, PureWindowsPath

from Model import Molecule

class CmdMolAnalyse:
    def process(self, basePath):
        files = self.ListMolecules(basePath)
        newlist = []
        for file in files:
            f = open(file, "r")
            fileData = f.read()    
            newlist.append(self.convertToMolecule(json.loads(fileData)))
            f.close()
        
        print(len(newlist))


    def convertToMolecule(self, data):
        retval = Molecule()
        retval.NameInfo = data['NameInfo']
        retval.Description = data['Description']
        return retval


    def convertToBond(self, data):
        pass

    def ListMolecules(self, basePath):        
        path = Path(basePath)        
        return list(path.glob('**/*.json'))