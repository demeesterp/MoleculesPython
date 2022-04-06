import argparse
from Cmd.MolCmdKind import MolCmdKind

class CmdArgParser: 

    def retrieve(self):
        parser = argparse.ArgumentParser("Command details");
        parser.add_argument('--cmd', type=str, required=True)
        parser.add_argument('--basepath', type=str, required=False)
        args = parser.parse_args()
        return args

    def retrievecmd(self):
        args = self.retrieve()
        command = str(args.cmd)
        if  command.lower() == MolCmdKind.process.value :
            return MolCmdKind.process
        elif command.lower() == MolCmdKind.analyse.value :
            return MolCmdKind.analyse
        else :
            return MolCmdKind.dummy        
    
    def retrievebasepath(self):
        args = self.retrieve()
        return str(args.basepath)