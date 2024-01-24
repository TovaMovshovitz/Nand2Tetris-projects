import sys

from Code import Code
from Parser import Parser
from SymbolTable import SymboleTable


class HackAssembler:
    def __init__(self, hack_filename):
        self.code = Code()
        self.symbolTable = SymboleTable()
        self.firstPass(hack_filename)
        self.secondPass(hack_filename)

        filename = hack_filename.split(".asm")[0]
        output_file = filename + ".hack"
        with open(output_file, "w") as file:
            for instruction in self.instructions[:-1]:
                file.write(instruction + "\n")
            file.write(self.instructions[-1])

    # First pass:
    # Reads the program lines, one by one focusing only on (label) declarations.
    # Adds the found labels to the symbol table
    def firstPass(self, hack_filename):
        parser = Parser(hack_filename)
        line = 0
        while parser.hasMoreLines():
            parser.advance()
            if parser.instructionType() == "L_INSTRUCTION":
                symbol = parser.symbol()
                self.symbolTable.addEntry(symbol, line)
            else:
                line += 1

    def secondPass(self, hack_filename):
        parser = Parser(hack_filename)
        self.lastNotUseAdress = 16
        self.instructions = []
        while parser.hasMoreLines():
            parser.advance()
            type = parser.instructionType()
            if type == "A_INSTRUCTION":
                self.instructions.append(self.translateAinstruction(parser))
            elif type == "C_INSTRUCTION":
                self.instructions.append(self.translateCinstruction(parser))

    def translateAinstruction(self, parser):
        symbol = parser.symbol()
        if symbol.isnumeric():  # is not symbol
            number = int(symbol)
        else:
            # use symbol
            if not self.symbolTable.contains(symbol):
                self.symbolTable.addEntry(symbol, self.lastNotUseAdress)
                self.lastNotUseAdress += 1
            number = self.symbolTable.getAddress(symbol)
        bin_num = bin(number)[2:]
        return bin_num.zfill(16)

    def translateCinstruction(self, parser):
        dest = parser.dest()
        comp = parser.comp()
        jump = parser.jump()
        return (
            "111" + self.code.comp(comp) + self.code.dest(dest) + self.code.jump(jump)
        )


if __name__ == "__main__":
    try:
        hack_filename = sys.argv[1]
    except IndexError:
        sys.exit("Please add a .asm file as an argument of the assembler")
    HackAssembler(hack_filename)
