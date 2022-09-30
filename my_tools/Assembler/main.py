from Parser import Parser
from Code import Code
from SymbolTable import SymbolTable
import sys
import argparse 
import re

def main():
    argparser = argparse.ArgumentParser("Hack Assembler")
    argparser.add_argument("infile", type=str)
    args = argparser.parse_args()

    with open(args.infile) as f:
        parser = Parser(f)

    with open(args.infile) as f:
        parser_for_table = Parser(f)

    code = Code()
    symbol_table = SymbolTable()

    hack_idx = 0
    while ( parser_for_table.hasMoreCommands() ):
        parser_for_table.advance()
        current_type = parser_for_table.commandType()
        if current_type == "L_COMMAND":
            current_symbol = parser_for_table.symbol()
            symbol_table.addEntry(current_symbol, hack_idx) 
        else:
            hack_idx += 1

    var_symbol_adress = 16
    while ( parser.hasMoreCommands() ):
        parser.advance()
        current_type = parser.commandType()
        if current_type == "C_COMMAND":
            dest = code.dest(parser.dest())
            jump = code.jump(parser.jump())
            comp = code.comp(parser.comp())
            print("111" + comp + dest + jump )
        elif current_type == "A_COMMAND":
            symbol = parser.symbol()
            if re.match("\d+", symbol) is None:
                if symbol_table.contains(symbol) == False:
                    symbol_table.addEntry(symbol, var_symbol_adress)
                    var_symbol_adress += 1
                adress = symbol_table.getAddress(symbol)
            else:
                adress = int(symbol)
            print("0" + format(adress,"015b"))
        else:
            pass

if __name__ == "__main__":
    main()
