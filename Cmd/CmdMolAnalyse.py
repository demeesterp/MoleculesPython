from glob import glob
import json
import logging
from os import read
from pathlib import Path
from typing import Sequence
from Analyse.MoleculeAnalyser import MoleculeAnalyser
from Model.Molecule import Molecule, Bond, ElPot, Orbital, Atom

class CmdMolAnalyse:
    def process(self, basePath):
        files = self.ListMolecules(basePath)
        newlist: Sequence[Molecule] = []
        for file in files:
            try:
                f = open(file, "r")
                fileData = f.read()    
                newlist.append(self._convertToMolecule(json.loads(fileData)))
            except Exception as e:
                logging.exception(e)
            finally:
                if not f.closed:
                    f.close()
        MoleculeAnalyser(newlist).Analyse();


    def _convertToMolecule(self, data):
        retval = Molecule()
        retval.NameInfo = data['NameInfo']
        retval.Description = data['Description']
        retval.Comment = data['Comment']
        retval.Status = data['Status']
        retval.Charge = data['Charge']
        retval.DftEnergy = data['DftEnergy']
        retval.HFEnergy = data['HFEnergy']
        retval.ElectronAffinity = data['ElectronAffinity']
        retval.Hardness = data['Hardness']

        for bond in data['Bonds']:
            retval.Bonds.append(self._convertToBond(bond))
        
        for elpot in data['ElPot']:
            retval.ElPot.append(self._convertToElpot(elpot))

        for atom in data['Atoms']:
            retval.Atoms.append(self._convertToAtom(atom))
        
        return retval

    def _convertToBond(self, data):
        retval = Bond()
        retval.Atom1Position = data['Atom1Position']
        retval.Atom2Position = data['Atom2Position']

        retval.BondOrder = data['BondOrder']
        retval.BondOrderAcid = data['BondOrderAcid']
        retval.BondOrderBase = data['BondOrderBase']

        retval.Distance = data['Distance']

        retval.OverlapPopulation = data['OverlapPopulation']
        retval.OverlapPopulationAcid = data['OverlapPopulationAcid']
        retval.OverlapPopulationBase = data['OverlapPopulationBase']

        return retval
    
    def _convertToElpot(self, data):
        retval = ElPot()
        retval.MoleculeID = data['MoleculeID']
        retval.Electronic = data['Electronic']
        retval.Nuclear = data['Nuclear']
        retval.PosX = data['PosX']
        retval.PosY = data['PosY']
        retval.PosZ = data['PosZ']
        retval.Total = data['Total']
        return retval;
    
    def _convertToAtom(self, data):
        retval = Atom()
        retval.AtomicWeight = data['AtomicWeight']
        retval.CHelpGCharge = data['CHelpGCharge']
        retval.ConnollyCharge = data['ConnollyCharge']
        retval.GeoDiscCharge = data['GeoDiscCharge']

        retval.Info = data["Info"]

        retval.LowdinPopulation = data['LowdinPopulation']
        retval.LowdinPopulationAcid = data['LowdinPopulationAcid']
        retval.LowdinPopulationBase = data['LowdinPopulationBase']

        retval.MullikenPopulation = data['MullikenPopulation']
        retval.MullikenPopulationAcid = data['MullikenPopulationAcid']
        retval.MullikenPopulationBase = data['MullikenPopulationBase']

        retval.Number = data['Number']
        retval.Position = data['Position']
        retval.PosX = data['PosX']
        retval.PosY = data['PosY']
        retval.PosZ = data['PosZ']

        retval.Radius = data['Radius']
        retval.Symbol = data['Symbol']

        for orbital in data["Orbitals"]:
            retval.Orbitals.append(self._convertToOrbital(orbital))

        return retval;

    def _convertToOrbital(self, data):
        retval = Orbital()
        retval.Symbol = data['Symbol']
        retval.Position = data['Position']
        retval.LowdinPopulation = data['LowdinPopulation']
        retval.LowdinPopulationAcid = data['LowdinPopulationAcid']
        retval.LowdinPopulationBase = data['LowdinPopulationBase']
        retval.MullikenPopulation = data['MullikenPopulation']
        retval.MullikenPopulationAcid = data['MullikenPopulationAcid']
        retval.MullikenPopulationBase = data['MullikenPopulationBase']
        return retval;

    
    def ListMolecules(self, basePath):        
        path = Path(basePath)        
        return list(path.glob('**/*.json'))