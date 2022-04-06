#!/usr/bin/python
from Cmd.CmdArgParser import CmdArgParser
from Cmd.CmdMolAnalyse import CmdMolAnalyse
from Cmd.CmdMolProcess import CmdMolProcess
from Cmd.MolCmdKind import MolCmdKind

class CmdRunner:
    def run(self):
        cmdParser = CmdArgParser()
        cmd = cmdParser.retrievecmd()
        match cmd:
            case MolCmdKind.process:
                CmdMolProcess().process()
                return
            case MolCmdKind.analyse:
               basePath = cmdParser.retrievebasepath()
               CmdMolAnalyse().process(basePath)
               return
            case _:
                print('dummy run')   
                return 