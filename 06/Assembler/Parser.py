# Constructor / initializer: Creates a Parser and opens the source text file
# • Getting the current instruction:
# hasMoreLines(): Checks if there is more work to do
# advance(): Gets the next instruction and makes it the current instruction
# • Parsing the current instruction:
# instructionType(): Returns the instruction type L_INSTRUCTION, A_INSTRUCTION, C_INSTRUCTION
# symbol(): Returns the instruction’s symbol (string)
# dest(): Returns the instruction’s dest field (string)
# comp(): Returns the instruction’s comp field (string)
# jump(): Returns the instruction’s jump field (string)

class Parser:
    def __init__(self, sourceTextFilePath):
        with open(sourceTextFilePath, "r") as file:
            self.hack_text = file.read().split("\n")
            self.instructions = [
                line.strip()
                for line in self.hack_text
                if len(line.strip()) > 0 and not line.lstrip().startswith("//")
            ]
        self.currentLine = 0

    def hasMoreLines(self):
        return self.currentLine < len(self.instructions)

    def advance(self):
        self.currentInstruction = self.instructions[self.currentLine]
        self.currentLine += 1

    def instructionType(self):
        if self.currentInstruction.startswith("@"):
            return "A_INSTRUCTION"
        if self.currentInstruction.startswith("("):
            return "L_INSTRUCTION"
        return "C_INSTRUCTION"

    def symbol(self):
        if self.currentInstruction.startswith("@"):
            return self.currentInstruction[1:]
        else:
            return self.currentInstruction[1:-1]

    def dest(self):
        if "=" in self.currentInstruction:
            return self.currentInstruction.split("=")[0]
        return ""

    def comp(self):
        if "=" in self.currentInstruction:
            return self.currentInstruction.split("=")[1].split(";")[0]
        else:
            return self.currentInstruction.split(";")[0]

    def jump(self):
        if ";" in self.currentInstruction:
            return self.currentInstruction.split(";")[1]
        return ""
