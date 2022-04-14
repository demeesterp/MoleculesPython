class Molecule:
    def __init__(self):
        self.NameInfo =''
        self.Description=''
        self.Comment=''
        self.Status=0
        self.Charge=0
        self.DftEnergy=0
        self.HFEnergy=0
        self.ElectronAffinity=0
        self.Hardness=0
        self.Bonds = []
        self.Atoms = []
        self.ElPot = []

class Atom:
    def __init__(self):
        self.Orbitals = []

class Orbital:
    def __init__(self):
        pass


class Bond:
    def __init__(self) :
        pass

class ElPot:
    def __init__(self):
        pass