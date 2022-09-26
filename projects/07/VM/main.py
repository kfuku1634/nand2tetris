from Parser import Parser
from CodeWriter import CodeWriter
import sys

def main():

    infile = sys.argv[1]
    with open(infile, mode='r') as f:
        parser = Parser(f)
    code_writer = CodeWriter()

    while parser.hasMoreCommands():
        parser.advance()
        current_commandType = parser.commandType()
        current_command_list = parser.command_list()
        if current_commandType == "C_POP" or current_commandType == "C_PUSH":
            segment = parser.arg1()
            index   = parser.arg2()
            code_writer.writePushPop( current_commandType, segment, index )
        elif current_commandType == "C_ARITHMETIC":
            code_writer.writeArithmetric(current_command_list[0])

if __name__ == "__main__":
    main()
