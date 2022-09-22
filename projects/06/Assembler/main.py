from Parser import Parser
from Code import Code
import sys
import argparse 

def main():
    argparser = argparse.ArgumentParser("Hack Assembler")
    argparser.add_argument("infile", type=argparse.FileType("r"))
    args = argparser.parse_args()

    parser = Parser(args.infile)
    code = Code()

    while ( parser.hasMoreCommands() ):
        parser.advance()
        current_type = parser.commandType()
        if current_type == "C_COMMAND":
            dest = code.dest(parser.dest())
            jump = code.jump(parser.jump())
            comp = code.comp(parser.comp())
            print("111" + comp + dest + jump )
        else:
            symbol = parser.symbol()
            symbol = int(symbol)
            print("0" + format(symbol,"015b"))


if __name__ == "__main__":
    main()
