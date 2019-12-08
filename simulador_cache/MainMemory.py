import Cell
import random
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
    # Arguments: self(object), address(string[bin])
    # Return: block[Cell(),...]
    # Description: Using the address read a block from Main Memory, and return the block
    def getBlock(self, address):
        initialCell = int(address, 2)-int(address, 2)%self._blockSize
        block = []

        for _ in range(self._blockSize):
            block.append(self._cells[initialCell + _ ])
        #print("Initial cell", initialCell, " - Address", int(address, 2))
        return block

    # Function: writeBack
    # Arguments: self(object), oldBlock[Cell(), ...], label(string[bin])
    # Return: N/A
    # Description: Write a oldBlock in a position based on label on MainMemory
    def writeBack(self, oldBlock, address):
        print("WRITE BACK")
        initialCell = int(int(address, 2)-int(address, 2)%self._blockSize) # Address of the initial cell of the block
        # Fill The block in main memory with the values who was previously on cache
        for _ in range(self._blockSize):
            self._cells[initialCell+_]._bits = oldBlock[_]

    # Function: randomInsertInAllCells
    # Arguments: self(object)
    # Return: N/A
    # Description: Write a random value in all cells in main memory
    def randomInsertInAllCells(self):
        for _ in range(len(self._cells)):
            self._cells[_]._bits = bin(random.randrange(0, 255))[2:].zfill(8)

    # Function: putZeroInsertInAllCells
    # Arguments: self(object)
    # Return: N/A
    # Description: Write a random value in all cells in main memory
    def putZeroInsertInAllCells(self):
        for _ in range(len(self._cells)):
            self._cells[_]._bits = "00000000"