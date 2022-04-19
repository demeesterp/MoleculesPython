from enum import Enum

class MoleculeReportList:
    def __init__(self):
        self.Reports = []

class MoleculeReportKind(Enum):
    molweight = "molweight"
    molhardness="molhardness"
    molsoftness="molsoftness"
    molenergy="molenergy"

class MoleculeReport:
    def __init__(self, name):
        self.Name = name

    def type(self):
        raise NotImplementedError()

class MolecularWeight(MoleculeReport):
    def __init__(self, name):
        super().__init__(name)
        self.weight = 0

    def type(self):
        return MoleculeReportKind.molweight;

class MolecularHardness(MoleculeReport):
    def __init__(self, name):
        super().__init__(name)
        self.hardness = 0

    def type(self):
        return MoleculeReportKind.molhardness;

class MolecularSoftness(MoleculeReport):
    def __init__(self, name):
        super().__init__(name)
        self.softness = 0

    def type(self):
        return MoleculeReportKind.molsoftness;

class MolecularEnergy(MoleculeReport):
    def __init__(self, name):
        super().__init__(name)
        self.energy = 0

    def type(self):
        return MoleculeReportKind.molenergy;