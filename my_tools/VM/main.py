from Parser import Parser
from CodeWriter import CodeWriter
import sys
import glob

def main():
    input_arg = sys.argv[1]
    if isVMfile(input_arg) == True:
        files = [input_arg]
    else:
        files = get_VMfileInDir(input_arg)

    code_writer = CodeWriter()
    code_writer.writeInit()
    for file in files:
        with open(file, mode='r') as f:
            parser = Parser(f)
        code_writer.setFileName(file)
        vm2asm(parser, code_writer)

def isVMfile(file):
    if file.split(".")[-1] == "vm":
        return True
    else:
        return False

def get_VMfileInDir(target_dir):
    files = []
    for file in glob.glob(target_dir + "/*.vm", recursive=True):
        files.append(file)
    return files

def vm2asm(parser, code_writer):
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
        elif current_commandType == "C_CALL":
            functionName = parser.arg1()
            numArgs = parser.arg2()
            code_writer.writeCall(functionName, numArgs)
        elif current_commandType == "C_ARITHMETIC":
            code_writer.writeArithmetric(current_command_list[0])

if __name__ == "__main__":
    main()
