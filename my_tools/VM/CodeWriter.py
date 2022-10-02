class CodeWriter():
    def __init__(self):
        # with open("out.asm", mode="w") as f:
            # self.f = f
        self.njmp = 0
        self.direct_map = { "TEMP":   "5",
                            "POINTER": "3"    }

    def _setAddressFromSP(self):
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
        self._fileSymbol = fileName.split(".")[0]
        pass

    def writeArithmetric(self, command):
        if command == "add":
            self._decSP()
            self._writePopFromStackToDRegister()
            self._decSP()
            self._setAddressFromSP()
            print("M=D+M")
            self._incSP()
        elif command == "sub":
            self._decSP()
            self._writePopFromStackToDRegister()
            self._decSP()
            self._setAddressFromSP()
            print("M=M-D")
            self._incSP()
        elif command == "neg":
            self._decSP()
            self._setAddressFromSP()
            print("M=-M")
            self._incSP()
        elif command == "eq":
            self._decSP()
            self._writePopFromStackToDRegister()
            self._decSP()
            self._setAddressFromSP()
            print("D=M-D")
            print("M=-1")
            print("@TMP{}".format(self.njmp))
            print("D;JEQ")
            self._setAddressFromSP()
            print("M=0")
            print("(TMP{})".format(self.njmp))
            self._incSP()
            self.njmp += 1
        elif command == "gt":
            self._decSP()
            self._writePopFromStackToDRegister()
            self._decSP()
            self._setAddressFromSP()
            print("D=D-M")
            print("M=-1")
            print("@TMP{}".format(self.njmp))
            print("D;JGT")
            self._setAddressFromSP()
            print("M=0")
            print("(TMP{})".format(self.njmp))
            self._incSP()
            self.njmp += 1
        elif command == "lt":
            self._decSP()
            self._writePopFromStackToDRegister()
            self._decSP()
            self._setAddressFromSP()
            print("D=D-M")
            print("M=-1")
            print("@TMP{}".format(self.njmp))
            print("D;JGT")
            self._setAddressFromSP()
            print("M=0")
            print("(TMP{})".format(self.njmp))
            self._incSP()
            self.njmp += 1
        elif command == "and":
            self._decSP()
            self._writePopFromStackToDRegister()
            self._decSP()
            self._setAddressFromSP()
            print("M=D&M")
            self._incSP()
        elif command == "or":
            self._decSP()
            self._writePopFromStackToDRegister()
            self._decSP()
            self._setAddressFromSP()
            print("M=D|M")
            self._incSP()
        elif command == "not":
            self._decSP()
            self._writePopFromStackToDRegister()
            self._setAddressFromSP()
            print("M=!M")
            self._incSP()
        else:
            pass

    def _setIndexToDRegister(self,index):
        print("@{}".format(index))
        print("D=A")

    def _setAddressSegmentPlusIndex(self, ram_symbol):
        print("@{}".format(ram_symbol))
        print("A=D+M")

    def _popTo(self, where):
        self._decSP()
        self._setAddressSegmentPlusIndex(where)
        print("D=A")
        print("@POP")
        print("M=D")
        self._setAddressFromSP()
        print("D=M")
        print("@POP")
        print("A=M")
        print("M=D")
        
    def _setAddressDirect(self, segment):
        segment_address = self.direct_map[segment]
        print("@{}".format(segment_address))
        print("A=D+A")

    def _popToDirectMap(self, segment):
        self._decSP()
        self._setAddressDirect(segment)
        print("D=A")
        print("@{}_ACCESS_AD".format(segment))
        print("M=D")
        self._setAddressFromSP()
        print("D=M")
        print("@{}_ACCESS_AD".format(segment))
        print("A=M")
        print("M=D")

    def writePushPop(self, command, segment, index):
        self._setIndexToDRegister(index)
        if command == "C_PUSH":
            if segment == "constant":
                self._setAddressFromSP()
                print("M=D")
                self._incSP()
            elif segment == "local":
                self._setAddressSegmentPlusIndex("LCL")
                print("D=M")
                self._setAddressFromSP()
                print("M=D")
                self._incSP()
            elif segment == "argument":
                self._setAddressSegmentPlusIndex("ARG")
                print("D=M")
                self._setAddressFromSP()
                print("M=D")
                self._incSP()
            elif segment == "this":
                self._setAddressSegmentPlusIndex("THIS")
                print("D=M")
                self._setAddressFromSP()
                print("M=D")
                self._incSP()
            elif segment == "that":
                self._setAddressSegmentPlusIndex("THAT")
                print("D=M")
                self._setAddressFromSP()
                print("M=D")
                self._incSP()
            elif segment == "temp":
                print("@{}".format(self.direct_map["TEMP"]))
                print("A=D+A")
                print("D=M")
                self._setAddressFromSP()
                print("M=D")
                self._incSP()
            elif segment == "pointer":
                print("@{}".format(self.direct_map["POINTER"]))
                print("A=D+A")
                print("D=M")
                self._setAddressFromSP()
                print("M=D")
                self._incSP()
            elif segment == "static":
                print("@{}{}".format(self._fileSymbol, index))
                print("D=M")
                self._setAddressFromSP()
                print("M=D")
                self._incSP()
            else: 
                pass
        elif command == "C_POP":
            if segment == "constant":
                pass
            elif segment == "local":
                self._popTo("LCL")
            elif segment == "argument":
                self._popTo("ARG")
            elif segment == "this":
                self._popTo("THIS")
            elif segment == "that":
                self._popTo("THAT")
            elif segment == "temp":
                self._popToDirectMap("TEMP")
            elif segment == "pointer":
                self._popToDirectMap("POINTER")
            elif segment == "static":
                self._decSP()
                self._setAddressFromSP()
                print("D=M")
                print("@{}{}".format(self._fileSymbol, index))
                print("M=D")
            else: 
                pass

    def writeInit(self):
        print("@256")
        print("D=A")
        print("@SP")
        print("M=D")

    def writeLabel(self, label):
        print("({})".format(label))

    def writeGoto(self, label):
        print("@{}".format(label))
        print("0;JMP")

    def writeIF(self, label):
        self._decSP()
        self._setAddressFromSP()
        print("D=M")
        print("@{}".format(label))
        print("D;JNE")

    def writeCall(self, functionName, numArgs):
        pass

    def writeReturn(self):
        pass

    def writeFunction(self, functionName, numLocals):
        pass
