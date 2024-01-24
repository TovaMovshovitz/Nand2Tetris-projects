# Deals only with C-instructions: dest = comp ; jump
# Routines:
# dest(string): Returns the binary representation of the parsed dest field (string)
# comp(string): Returns the binary representation of the parsed comp field (string)
# jump(string): Returns the binary representation of the parsed jump field (string)


class Code:
    def dest(self, dest_string):
        binary_dest = ["0", "0", "0"]
        for index, letter in enumerate("ADM"):
            if letter in dest_string:
                binary_dest[index] = "1"
        return "".join(binary_dest)

    def comp(self, comp_string):
        comp_dict = {
            "0": "101010",
            "1": "111111",
            "-1": "111010",
            "D": "001100",
            "A": "110000",
            "!D": "001101",
            "!A": "110001",
            "-D": "001111",
            "-A": "110011",
            "D+1": "011111",
            "A+1": "110111",
            "D-1": "001110",
            "A-1": "110010",
            "D+A": "000010",
            "D-A": "010011",
            "A-D": "000111",
            "D&A": "000000",
            "D|A": "010101",
        }
        a_bit = "1" if "M" in comp_string else "0"
        return a_bit + comp_dict[comp_string.replace("M", "A")]

    def jump(self, jump_string):
        return {
            "JGT": "001",
            "JEQ": "010",
            "JGE": "011",
            "JLT": "100",
            "JNE": "101",
            "JLE": "110",
            "JMP": "111",
        }.get(jump_string, "000")
