import Cell
# [2:] to cut 0b and zfill to padronize bits size
class MainMemory:
    def __init__(self, blockSize, cellAmount, cellBits):
        self._addressBits = len(bin(cellAmount)[2:])-1 # Just to print easier
        self._blockBits = len(bin(cellAmount//blockSize)[2:])-1 # Just to print easier
        self._cellBits = cellBits # Just to print easier
        self._cells = [] # Cells List
        self._blockSize = blockSize # How many cells have in a block
        for _ in range(cellAmount):
            self._cells.append(Cell.Cell(cellBits))

    # Function: printAllCells
    # Arguments: self(object)
    # Return: N/A
    # Description: Show all cells content, by address(position on list of cells) and block(position on list of cells//blockSize)
    # Ex:   |--------------MAIN MEMORY---------------|
    #       |   Block   |   Address   |    Value     |
    #       |   00000   |   0000000   |   00000000   |
    #       |     .     |      .      |      .       |
    #       |     .     |      .      |      .       |
    #       |     .     |      .      |      .       |
    #       |   11111   |   1111111   |   00000000   |
    #       |----------------------------------------|
    def printAllCells(self):
        print(self._blockBits, self._addressBits, self._cellBits)
        padding = 5 if self._cellBits%2!=0 else 6 # Padding based if cellBits is or isn't odd
        helper = "|{:-^"+str(self._blockBits+self._addressBits+self._cellBits+padding*3+2)+"s}|\n|{: ^"+str(self._blockBits+padding)+"s}|{: ^"+str(self._addressBits+padding)+"s}|{: ^"+str(self._cellBits+padding)+"s}|" # Receive format to print string
        print(helper.format("MAIN MEMORY", "Block", "Address", "Value")) # Print Header
        helper = helper.split("\n")[1] # Exclude "MAIN MEMORY" from helper

        for _ in range(len(self._cells)):
            print(helper.format( bin(_//self._blockSize)[2:].zfill(self._blockBits) , bin(_)[2:].zfill(self._addressBits), self._cells[_]._bits.zfill(self._cellBits)))

        helper = "|{:-^"+str(self._blockBits+self._addressBits+self._cellBits+padding*3+2)+"s}|"
        print(helper.format(""))

    # Function: printBlock
    # Arguments: self(object), label(string[bin])
    # Return: N/A
    # Description: Using the label print a block from Main Memory
    def printBlock(self, label):
        block = self.getBlock(label)

        for _ in (self._blockSize):
            print(block[_])

    # Function: getBlock
    # Arguments: self(object), label(string[bin])
    # Return: block[Cell(),...]
    # Description: Using the label read a block from Main Memory, and return the block
    def getBlock(self, label):
        initialBlock = label*self._blockSize
        block = []

        for _ in range(self._blockSize):
            block.append(self._cells[initialBlock + _])

        return block

    # Function: writeBlock
    # Arguments: self(object), newBlock[Cell(), ...], label(string[bin])
    # Return: N/A
    # Description: Write a newBlock in a position based on label on MainMemory
    def writeBlock(self, newBlock, label):
        block = self.getBlock(label)

        for _ in range(self._blockSize):
            block[_]._bits = newBlock[_]._bits