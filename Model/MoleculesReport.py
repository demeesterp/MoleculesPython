from enum import Enum

class MoleculeReportList:
    def __init__(self):
        self.Reports = []

class MoleculeReportKind(Enum):
    molweight = "molweight"

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