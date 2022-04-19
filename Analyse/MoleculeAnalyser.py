
from typing import Sequence
from Model.Molecule import Molecule
from Model.MoleculesReport import MolecularEnergy, MolecularHardness, MolecularSoftness, MolecularWeight, MoleculeReportList

class MoleculeAnalyser:   
    def __init__(self, molecules: Sequence[Molecule]):
        self.Molecules = molecules

    def Analyse(self) -> MoleculeReportList() :
        retval = MoleculeReportList()
        for molecule in self.Molecules:
           retval.Reports.append(MoleculeWeightAnalyser(molecule).Analyse())
           retval.Reports.append(MoleculeHardnessAnalyser(molecule).Analyse())
           retval.Reports.append(MoleculeSoftnessAnalyser(molecule).Analyse())
           retval.Reports.append(MoleculeEnergyAnalyser(molecule).Analyse())
        return retval;

class MoleculeWeightAnalyser:
    def __init__(self, molecule: Molecule):
        self.Molecule = molecule

    def Analyse(self):
        retval = MolecularWeight(self.Molecule.NameInfo);
        for atom in self.Molecule.Atoms:
            retval.weight += atom.AtomicWeight
        return  retval

class MoleculeHardnessAnalyser:
        def __init__(self, molecule: Molecule):
            self.Molecule = molecule
        
        def Analyse(self):
            retval = MolecularHardness(self.Molecule.NameInfo)
            retval.hardness = self.Molecule.Hardness

class MoleculeSoftnessAnalyser:
        def __init__(self, molecule: Molecule):
            self.Molecule = molecule
        
        def Analyse(self):
            retval = MolecularSoftness(self.Molecule.NameInfo)
            retval.softness = self.Molecule.ElectronAffinity


class MoleculeEnergyAnalyser:
        def __init__(self, molecule: Molecule):
            self.Molecule = molecule
        
        def Analyse(self):
            retval = MolecularEnergy(self.Molecule.NameInfo)
            retval.energy = self.Molecule.DftEnergy

