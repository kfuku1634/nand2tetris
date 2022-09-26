import sys

class Parser():
    def __init__(self, infile):
        fdata = infile.readlines()
        self.fdata = []
        for i in fdata:
            line = i.split("/")[0].strip()
            if line != "":
                self.fdata.append(line)

        self.current_idx = -1
        self.current_command = []

    def hasMoreCommands(self) -> bool:
        Ncommands = len(self.fdata)
        if self.current_idx < (Ncommands - 1):
            return True
        else:
            return False

    def advance(self):
        if self.hasMoreCommands():
            self.current_idx += 1
            self.current_command = self.fdata[self.current_idx]
            self.current_command_list = self.current_command.split()

    def command_list(self):
        return self.current_command_list

    def commandType(self):
        if self.current_command_list[0] == "push":
            self.current_commandType = "C_PUSH"
        else:
            self.current_commandType = "C_ARITHMETIC"
        return self.current_commandType

    def arg1(self):
        if self.current_commandType == "C_RETURN":
            print("Parser.arg1 shouldn't be called when current_commandType is C_RETURN")
            sys.exit(1)
        elif self.current_commandType == "C_ARITHMETIC":
            arg1 = self.current_command_list[0]
        else:
            arg1 = self.current_command_list[1]
        return arg1

    def arg2(self):
        if self.current_commandType == "C_POP" or self.current_commandType == "C_PUSH" or self.current_commandType == "C_FUNCTION" or self.current_commandType == "C_CALL" :
            return self.current_command_list[2]
        else:
            print("Parser.arg2 should be called only when current_command is C_PUSH or C_POP or C_FUNCTION or C_CALL")
            sys.exit(1)
