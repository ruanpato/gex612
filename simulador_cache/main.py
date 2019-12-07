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
                print("Read Hit")
                statistics._readHits += 1
            elif result == 0:
                print("Read Fault")
                statistics._readFaults += 1
                block = mainMemory.getBlock(memoryAddress) # Pega o bloco da memória principal
                print(block[0]._bits, block[1]._bits, block[2]._bits, block[3]._bits) # Retirar

                oldBlock = cacheMemory.putBlock(memoryAddress.zfill(7), block) # Coloca o bloco na cache
                # Write back in action
                if oldBlock[0] != None and oldBlock[1] != None:
                    mainMemory._cells[int(oldBlock[0], 2)+0]._bits = oldBlock[1][0]._bits
                    mainMemory._cells[int(oldBlock[0], 2)+1]._bits = oldBlock[1][1]._bits
                    mainMemory._cells[int(oldBlock[0], 2)+2]._bits = oldBlock[1][2]._bits
                    mainMemory._cells[int(oldBlock[0], 2)+3]._bits = oldBlock[1][3]._bits
    except:
        print("Error")

def writeContentInMemory():
    memoryAddress = input("Type a binary value in range [" + ("0"*(len(bin(cellAmountMM)[2:])-1)) + ", " + ("1"*(len(bin(cellAmountMM)[2:])-1)) +"]: ")
    value = input( ("Type a binary value in range [" + bin(0)[2:].zfill(cellBits) +", " + ("1"*cellBits) +"]: ") )
    try:
        if int(memoryAddress, 2) >= 0  and int(memoryAddress, 2) < cellAmountMM and int(value, 2) >= 0 and int(value, 2) <= 255:
            result = cacheMemory.blockIsInCache(memoryAddress.zfill(7))
            if result == 1:
                print("Write Hit")
                statistics._writeHits += 1
                # Change value in cache

            elif result == 0:
                print("Write Fault")
                statistics._writeFaults += 1
                block = mainMemory.getBlock(memoryAddress) # Pega o bloco da memória principal
                print(block[0]._bits, block[1]._bits, block[2]._bits, block[3]._bits) # Retirar

                oldBlock = cacheMemory.putBlock(memoryAddress.zfill(7), block) # Coloca o bloco na cache

                # Write back in action
                if oldBlock[0] != None and oldBlock[1] != None:
                    mainMemory._cells[int(oldBlock[0], 2)+0]._bits = oldBlock[1][0]._bits
                    mainMemory._cells[int(oldBlock[0], 2)+1]._bits = oldBlock[1][1]._bits
                    mainMemory._cells[int(oldBlock[0], 2)+2]._bits = oldBlock[1][2]._bits
                    mainMemory._cells[int(oldBlock[0], 2)+3]._bits = oldBlock[1][3]._bits

    except:
        pass
    #if block == None:
        #bloco = memoryCache.readBlockFromMemory(memoryAddress, mainMemory)
        #statistics._accessFaults += 1 # Increment access faults
       # statistics._writeFaults += 1 # Increment write faults
   # else:
        #statistics._accessHits += 1 # Increment access Hits
      #  statistics._writeHits += 1 # Increment Write Hits

    # Write data on cache
    #cacheMemory.writeData(memoryAddress, value)

# Menu
while(True):
    option = int(input("1. Read a memory address.\n2. Write on memory.\n3. Show statistics.\n4. Show all Main Memory.\n5. Show all Cache Memory.\n6. Insert random values in all cells of Main Memory.\n7. Set zero to all bits of cells in main memory.\n0. Exit\n"))
    if option ==  1: # Read a memory Address
        readMemoryAddress()
    elif option == 2: # Write on memory
        pass
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