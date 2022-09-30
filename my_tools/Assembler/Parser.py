import sys

class Parser():
    def __init__(self, infile):
        fdata = infile.readlines()
        self.fdata = []
        for i in fdata:
            line = i.split("/")[0].strip().replace(" ","")
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

    def commandType(self):
        if "@" in self.current_command:
            self.current_type = "A_COMMAND"
        elif "(" in self.current_command:
            self.current_type = "L_COMMAND"
        else:
            self.current_type = "C_COMMAND"
        return self.current_type

    def symbol(self) -> str:
        if self.current_type == "C_COMMAND":
            print("symbol function must be called when current_command is not C_COMMAND")
            sys.exit(1)
        elif self.current_type == "A_COMMAND":
            return self.current_command[1:]
        elif self.current_type == "L_COMMAND":
            return self.current_command[1:-1]
        else:
            print("output of commandType is must be [CAL]_COMMAND")
            sys.exit(1)

    def dest(self) -> str:
        if self.current_type != "C_COMMAND":
            print("dest function must be called when current_command is C_COMMAND")
            sys.exit(1)

        res = ""
        if "=" in self.current_command:
            res = self.current_command.split("=")[0]
        return res

    def comp(self) -> str:
        if self.current_type != "C_COMMAND":
            print("dest function must be called when current_command is C_COMMAND")
            sys.exit(1)

        res = self.current_command
        if "=" in self.current_command:
            res = res.split("=")[1]

        if ";" in self.current_command:
            res = res.split(";")[0]

        return res

    def jump(self) -> str:
        if self.current_type != "C_COMMAND":
            print("dest function must be called when current_command is C_COMMAND")
            sys.exit(1)

        res = ""
        if ";" in self.current_command:
            res = self.current_command.split(";")[1]
        return res

