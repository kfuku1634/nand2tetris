class CodeWriter():
    def __init__(self):
        with open("out.asm", mode="w") as f:
            self.f = f
        self.njmp = 0

    def _setAddresFromSP(self):
        print("@SP")
        print("A=M")

    def _incSP(self):
        print("@SP")
        print("M=M+1")

    def _decSP(self):
        print("@SP")
        print("M=M-1")

    def _writePopFromStackToDRegister(self):
        print("@SP")
        print("A=M")
        print("D=M")

    def setFileName(self, fileName):
        pass

    def writeArithmetric(self, command):
        if command == "add":
            self._decSP()
            self._writePopFromStackToDRegister()
            self._decSP()
            self._setAddresFromSP()
            print("M=D+M")
            self._incSP()
        elif command == "sub":
            self._decSP()
            self._writePopFromStackToDRegister()
            self._decSP()
            self._setAddresFromSP()
            print("M=D-M")
            self._incSP()
        elif command == "neg":
            self._decSP()
            self._setAddresFromSP()
            print("M=-M")
            self._incSP()
        elif command == "eq":
            self._decSP()
            self._writePopFromStackToDRegister()
            self._decSP()
            self._setAddresFromSP()
            print("D=D-M")
            print("M=-1")
            print("@TMP{}".format(self.njmp))
            print("D;JEQ")
            self._setAddresFromSP()
            print("M=0")
            print("(TMP{})".format(self.njmp))
            self._incSP()
            self.njmp += 1
        elif command == "gt":
            self._decSP()
            self._writePopFromStackToDRegister()
            self._decSP()
            self._setAddresFromSP()
            print("D=D-M")
            print("M=-1")
            print("@TMP{}".format(self.njmp))
            print("D;JGT")
            self._setAddresFromSP()
            print("M=0")
            print("(TMP{})".format(self.njmp))
            self._incSP()
            self.njmp += 1
        elif command == "lt":
            self._decSP()
            self._writePopFromStackToDRegister()
            self._decSP()
            self._setAddresFromSP()
            print("D=D-M")
            print("M=-1")
            print("@TMP{}".format(self.njmp))
            print("D;JGT")
            self._setAddresFromSP()
            print("M=0")
            print("(TMP{})".format(self.njmp))
            self._incSP()
            self.njmp += 1
        elif command == "and":
            self._decSP()
            self._writePopFromStackToDRegister()
            self._decSP()
            self._setAddresFromSP()
            print("M=D&M")
            self._incSP()
        elif command == "or":
            self._decSP()
            self._writePopFromStackToDRegister()
            self._decSP()
            self._setAddresFromSP()
            print("M=D|M")
            self._incSP()
        elif command == "not":
            self._decSP()
            self._writePopFromStackToDRegister()
            self._setAddresFromSP()
            print("M=!M")
            self._incSP()
        else:
            pass

    def writePushPop(self, command, segment, index):
        if command == "C_PUSH":
            if segment == "constant":
                print("@{}".format(index))
                print("D=A")
                self._setAddresFromSP()
                print("M=D")
                self._incSP()
