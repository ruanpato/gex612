import Line
import CacheMemory
import MainMemory
import Statistics
import os # Just to clear console

blockSize = 4 # 4 cells
cellBits = 8 # Amount of bits in a cell
cellAmountMM = 128 # 128 is the Amount of cells in Main memory
linesInCache = 8 # Amount of lines in cache
mapping = 1 # Set Associative
replacementPolicy = 0 # LRU
setSizeCache = 4 # Amount of lines by set in Cache
writePolicy = 0 # Write-back

mainMemory = MainMemory.MainMemory(blockSize, cellAmountMM, cellBits) # Create and initialize main memory
cacheMemory = CacheMemory.CacheMemory(linesInCache, setSizeCache, blockSize, cellBits) # Create and initialize Cache Memory
statistics = Statistics.Statistics() # create Statistics object

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def readMemoryAddress():
    memoryAddress = str(input( ("Type a binary value in range [" + ("0"*(len(bin(cellAmountMM)[2:])-1)) + ", " + ("1"*(len(bin(cellAmountMM)[2:])-1)) +"]: ") ))
    try:
        if int(memoryAddress, 2) >= 0  and int(memoryAddress, 2) < cellAmountMM:
            result = cacheMemory.blockIsInCache(memoryAddress.zfill(7))
            if result == 1:
                print("READ HIT")
                statistics._readHits += 1
            elif result == 0:
                print("READ FAULT")
                statistics._readFaults += 1
                block = mainMemory.getBlock(memoryAddress) # Pega o bloco da memória principal

                oldBlock = cacheMemory.putBlock(memoryAddress.zfill(7), block) # Coloca o bloco na cache
                # Write back in action
                if oldBlock[0] != None and oldBlock[1] != None: # oldBlock[0] == Address, # oldBlock[1] == "Block"
                    mainMemory.writeBack(oldBlock[1], oldBlock[0])
        line = cacheMemory.getLineInCache(memoryAddress.zfill(7))
        print("|{: ^30s}|".format("Block on Main Memory: "+str(int(memoryAddress, 2)//blockSize)))
        print("|{: ^30s}|".format("Cache Line destination: "+str(line)) )
        print("|{: ^30s}|".format("Set Destination: "+memoryAddress.zfill(7)[-3]))
    except:
        print("ERROR IN readMemoryAddress")

def writeContentInMemory():
    memoryAddress = input("Type a binary value in range [" + ("0"*(len(bin(cellAmountMM)[2:])-1)) + ", " + ("1"*(len(bin(cellAmountMM)[2:])-1)) +"]: ")
    value = input( ("Type a binary value in range [" + bin(0)[2:].zfill(cellBits) +", " + ("1"*cellBits) +"]: ") )
    try:
        if int(memoryAddress, 2) >= 0  and int(memoryAddress, 2) < cellAmountMM and int(value, 2) >= 0 and int(value, 2) <= 255:
            result = cacheMemory.getLineInCache(memoryAddress.zfill(7)) # Return -1 if isn't in cache
            if result != -1: # Is in cache
                print("WRITE HIT")
                statistics._writeHits += 1
                # Change value in cache, don't change in mainMemory
            elif result == -1: # Isn't in cache, so is needed get in main memory, put in cache and change in cache
                print("WRITE FAULT")
                statistics._writeFaults += 1
                block = mainMemory.getBlock(memoryAddress) # Get the block of Specified cell by address, and return it

                oldBlock = cacheMemory.putBlock(memoryAddress.zfill(7), block) # Put the new Block in cache, and return Address of the previously block, and a list with the value of his cells (if had, else return none, none)

                # Write back in action
                if oldBlock[0] != None and oldBlock[1] != None:
                    mainMemory.writeBack(oldBlock[1], oldBlock[0])
        blockOffset = int(memoryAddress[-2:], 2)
        line = cacheMemory.getLineInCache(memoryAddress.zfill(7)) # Return -1 if isn't in cache
        print("|{: ^30s}|".format("Block on Main Memory: "+str(int(memoryAddress, 2)//blockSize)))
        print("|{: ^30s}|".format("Cache Line destination: "+str(line)) )
        print("|{: ^30s}|".format("Set Destination: "+memoryAddress.zfill(7)[-3]))
        cacheMemory._lines[line]._writeBit = "1" # Sets the "Dirty bit" to 1 (Means when this block will be replaced need refresh in main memory [Write Back])
        cacheMemory._lines[line]._cells[blockOffset]._bits = value.zfill(8) # Value Writed

    except:
        print("ERROR IN writeContentInMemory")

# Menu
while(True):
    option = int(input("1. Read a memory address.\n2. Write on memory.\n3. Show statistics.\n4. Show all Main Memory.\n5. Show all Cache Memory.\n6. Insert random values in all cells of Main Memory.\n7. Set zero to all bits of cells in main memory.\n0. Exit\n"))
    if option ==  1: # Read a memory Address
        readMemoryAddress()
    elif option == 2: # Write on memory
        writeContentInMemory()
    elif option == 3: # Show statistics
        statistics.showStatistics()
    elif option == 4: # Show all Main Memory
        mainMemory.printAllCells()
    elif option == 5: # Show all Cache Memory
        cacheMemory.printAllCache(int(linesInCache//setSizeCache))
    elif option == 6: # Insert random values in all cells of Main Memory
        mainMemory.randomInsertInAllCells()
    elif option == 7: # Set zero to all bits of cells in main memory.
        mainMemory.putZeroInsertInAllCells()
    elif option == 0: # Exit execution
        exit()
    else: # Inválid Option
        clearConsole()
        print("Inválid Option")