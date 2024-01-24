# Constructor / initializer: Creates and initializes a SymbolTable
# addEntry(symbol (string), address (int)): Adds <symbol, address> to the table (void)
# contains(symbol (string)): Checks if symbol exists in the table (boolean)
# getAddress(symbol (string)): Returns the address (int) associated with symbol


class SymboleTable:
    table = {
        "R0": 0,
        "R1": 1,
        "R2": 2,
        "R3": 3,
        "R4": 4,
        "R5": 5,
        "R6": 6,
        "R7": 7,
        "R8": 8,
        "R9": 9,
        "R10": 10,
        "R11": 11,
        "R12": 12,
        "R13": 13,
        "R14": 14,
        "R15": 15,
        "SCREEN": 16384,
        "KBD": 24576,
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
    }

    def getAddress(self, symbol):
        return self.table[symbol]

    def addEntry(self, symbole, address):
        self.table[symbole] = address

    def contains(self, symbol):
        return symbol in self.table.keys()
