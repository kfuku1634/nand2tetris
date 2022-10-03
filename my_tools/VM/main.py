from Parser import Parser
from CodeWriter import CodeWriter
import sys

def main():

    infile = sys.argv[1]
    with open(infile, mode='r') as f:
        parser = Parser(f)
    code_writer = CodeWriter()
    code_writer.setFileName(infile)

    code_writer.writeInit()
    while parser.hasMoreCommands():
        parser.advance()
        current_commandType = parser.commandType()
        current_command_list = parser.command_list()
        if current_commandType == "C_POP" or current_commandType == "C_PUSH":
            segment = parser.arg1()
            index   = parser.arg2()
            code_writer.writePushPop( current_commandType, segment, index )
        elif current_commandType == "C_GOTO":
            label = parser.arg1()
            code_writer.writeGoto(label)
        elif current_commandType == "C_IF":
            label = parser.arg1()
            code_writer.writeIF(label)
        elif current_commandType == "C_LABEL":
            label = parser.arg1()
            code_writer.writeLabel(label)
        elif current_commandType == "C_RETURN":
            code_writer.writeReturn()
        elif current_commandType == "C_FUNCTION":
            functionName = parser.arg1()
            numLocals = parser.arg2()
            code_writer.writeFunction(functionName, numLocals)

        elif current_commandType == "C_ARITHMETIC":
            code_writer.writeArithmetric(current_command_list[0])

if __name__ == "__main__":
    main()
