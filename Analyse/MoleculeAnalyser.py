
from typing import Sequence
from Model.Molecule import Molecule
from Model.MoleculesReport import MolecularWeight, MoleculeReportList, MoleculeReport, MoleculeReportKind

class MoleculeAnalyser:
    
    def __init__(self, molecules: Sequence[Molecule]):
        self.Molecules = molecules

    def Analyse(self) -> MoleculeReportList() :
        retval = MoleculeReportList()
        for molecule in self.Molecules:
           retval.Reports.append(MoleculeWeightAnalyser(molecule).Analyse())
        return retval;

class MoleculeWeightAnalyser:
    def __init__(self, molecule: Molecule):
        self.Molecule = molecule

    def Analyse(self):
        retval = MolecularWeight(self.Molecule.NameInfo);
        for atom in self.Molecule.Atoms:
            retval.weight += atom.AtomicWeight
        return  retval

