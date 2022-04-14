class Molecule:
    def __init__(self):
        self.NameInfo = ''
        self.Description = ''
        self.Comment = ''
        self.Status = 0
        self.Charge = 0
        self.DftEnergy = 0.0
        self.HFEnergy = 0.0
        self.ElectronAffinity = 0.0
        self.Hardness = 0.0
        self.Bonds = []
        self.Atoms = []
        self.ElPot = []

class Atom:
    def __init__(self):
        self.Orbitals = []
        self.Position = 0
        self.Number = 0
        self.Symbol = ""
        self.AtomicWeight = 0
        self.Info = ""
        self.PosX = 0.0
        self.PosY = 0.0
        self.PosZ = 0.0
        self.Radius = 0
        self.MullikenPopulation = 0.0
        self.MullikenPopulationAcid = 0.0
        self.MullikenPopulationBase = 0.0
        self.LowdinPopulation = 0.0
        self.LowdinPopulationAcid = 0.0
        self.LowdinPopulationBase = 0.0
        self.CHelpGCharge = 0.0
        self.ConnollyCharge = 0.0
        self.GeoDiscCharge = 0.0

class Orbital:
    def __init__(self):
        self.Position = 0
        self.Symbol = ""
        self.MullikenPopulation = 0.0
        self.MullikenPopulationAcid = 0.0
        self.MullikenPopulationBase = 0.0
        self.LowdinPopulation = 0.0
        self.LowdinPopulationAcid = 0.0
        self.LowdinPopulationBase =  0.0


class Bond:
    def __init__(self) :
        self.Atom1Position = 0
        self.Atom2Position = 0
        self.Distance = 0.0
        self.BondOrder = 0.0
        self.BondOrderAcid = 0.0
        self.BondOrderBase = 0.0
        self.OverlapPopulation = 0.0
        self.OverlapPopulationAcid = 0.0
        self.OverlapPopulationBase = 0.0

class ElPot:
    def __init__(self):
      self.MoleculeID = 0
      self.Type = 1
      self.PosX = 0.0
      self.PosY = 0.0
      self.PosZ = 0.0
      self.Nuclear = 0.0
      self.Electronic = 0.0
      self.Total = 0.0