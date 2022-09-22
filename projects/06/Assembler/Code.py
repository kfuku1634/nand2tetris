class Code():
    def __init__(self):
        pass

    def dest(self, dest_mnemonic: str ) -> str:
        dest_mnemonic_map = { "M" : 0b001,
                              "D" : 0b010,
                              "A" : 0b100 }

        dest_int = 0
        for dest_str, num in dest_mnemonic_map.items():
            if dest_str in dest_mnemonic:
                dest_int += num
        return format(dest_int, "03b")

    def comp(self, comp_mnemonic: str ) -> str:
        comp_mnemonic_map  = { "0"   : "0101010" ,
                               "1"   : "0111111" ,
                               "-1"  : "0111010" ,
                               "D"   : "0001100" ,
                               "A"   : "0110000" ,
                               "M"   : "1110000" ,
                               "!D"  : "0001101" ,
                               "!A"  : "0110001" ,
                               "!M"  : "1110001" ,
                               "-D"  : "0001111" ,
                               "-A"  : "0110011" ,
                               "-M"  : "1110011" ,
                               "D+1" : "0011111" ,
                               "A+1" : "0110111" ,
                               "M+1" : "1110111" ,
                               "D-1" : "0001110" ,
                               "A-1" : "0110010" ,
                               "M-1" : "1110010" ,
                               "D+A" : "0000010" ,
                               "D+M" : "1000010" ,
                               "D-A" : "0010011" ,
                               "D-M" : "1010011" ,
                               "A-D" : "0000111" ,
                               "M-D" : "1000111" ,
                               "D&A" : "0000000" ,
                               "D&M" : "1000000" ,
                               "D|A" : "0010101" ,
                               "D|M" : "1010101" }

        return comp_mnemonic_map[comp_mnemonic]

    def jump(self, jump_mnemonic: str) -> str:
        jump_mnemonic_map = {  ""    : "000" ,
                               "JGT" : "001" ,
                               "JEQ" : "010" ,
                               "JGE" : "011" ,
                               "JLT" : "100" ,
                               "JNE" : "101" ,
                               "JLE" : "110" ,
                               "JMP" : "111"}

        return jump_mnemonic_map[jump_mnemonic]

