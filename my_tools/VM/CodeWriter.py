class CodeWriter():
    def __init__(self):
        # with open("out.asm", mode="w") as f:
            # self.f = f
        self.njmp = 0
        self.direct_map = { "TEMP":   "5",
                            "POINTER": "3"    }
        self._Nret = 0

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

    def _setAddressSegmentPlusIndex(self, segment):
        print("@{}".format(segment))
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

    def _pushFrom(self, where, index):
        self._setIndexToDRegister(index)
        self._setAddressSegmentPlusIndex(where)
        print("D=M")
        self._setAddressFromSP()
        print("M=D")
        self._incSP()

    def writePushPop(self, command, segment, index):
        if command == "C_PUSH":
            if segment == "constant":
                self._setIndexToDRegister(index)
                self._setAddressFromSP()
                print("M=D")
                self._incSP()
            elif segment == "local":
                self._pushFrom("LCL", index)
            elif segment == "argument":
                self._pushFrom("ARG", index)
            elif segment == "this":
                self._setIndexToDRegister(index)
                self._setAddressSegmentPlusIndex("THIS")
                print("D=M")
                self._setAddressFromSP()
                print("M=D")
                self._incSP()
            elif segment == "that":
                self._setIndexToDRegister(index)
                self._setAddressSegmentPlusIndex("THAT")
                print("D=M")
                self._setAddressFromSP()
                print("M=D")
                self._incSP()
            elif segment == "temp":
                self._setIndexToDRegister(index)
                print("@{}".format(self.direct_map["TEMP"]))
                print("A=D+A")
                print("D=M")
                self._setAddressFromSP()
                print("M=D")
                self._incSP()
            elif segment == "pointer":
                self._setIndexToDRegister(index)
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
            self._setIndexToDRegister(index)
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
        pass

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
        ret_address_symbol = "RET{}".format(self._Nret)
        self._Nret += 1
        print("@{}".format(ret_address_symbol))
        print("D=A")
        self._setAddressFromSP()
        print("M=D")
        self._incSP()
        for segment in ["LCL", "ARG", "THIS", "THAT"]:
            print("@{}".format(segment))
            print("D=M")
            self._setAddressFromSP()
            print("M=D")
            self._incSP()
        print("@5")
        print("D=A")
        print("@SP")
        print("D=M-D")
        print("@{}".format(numArgs))
        print("D=D-A")
        print("@ARG")
        print("M=D")
        print("@SP")
        print("D=M")
        print("@LCL")
        print("M=D")
        print("@{}".format(functionName))
        print("0;JMP")
        print("({})".format(ret_address_symbol))

    def _setDataToAddressM(self, segment, data ):
        print("@{}".format(segment))
        print("M={}".format(data))

    def writeReturn(self):
        self._decSP()
        self._setAddressFromSP()
        print("D=M")
        print("@ARG")
        print("A=M")
        print("M=D")
        print("@ARG")
        print("D=M")
        print("@SP")
        print("M=D")
        self._incSP()
        for n in reversed(range(5)):
            print("@{}".format(n+1))
            print("D=A")
            print("@LCL")
            print("A=M")
            print("A=A-D")
            print("D=M")
            print("@SP")
            print("A=M")
            print("M=D")
            self._incSP()
        segment_order = ["THAT", "THIS", "ARG" , "LCL" ]
        for segment in segment_order:
            self._decSP()
            self._setAddressFromSP()
            print("D=M")
            print("@{}".format(segment))
            print("M=D")
        self._decSP()
        print("A=M")
        print("0;JMP")

    def writeFunction(self, functionName, numLocals):
        print("({})".format(functionName))
        for _ in range(int(numLocals)):
            self._setAddressFromSP()
            print("M=0")
            self._incSP()
