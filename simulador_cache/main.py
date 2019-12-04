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

# Menu
while(True):
    option = int(input("1. Read a memory address.\n2. Write on memory.\n3. Show statistics.\n4. Show all Main Memory.\n5. Show all Cache Memory.\n0. Exit\n"))
    if option ==  1: # Read a memory Address
        pass
    elif option == 2: # Write on memory
        pass
    elif option == 3: # Show statistics
        pass
    elif option == 4: # Show all Main Memory
        mainMemory.printAllCells()
    elif option == 5: # Show all Cache Memory
        cacheMemory.printAllCache()
    elif option == 0: # Exit execution
        exit()
    else: # Inválid Option
        clearConsole()
        print("Inválid Option")


def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def readContentFromMemory():
    memoryAddress = verifyAddress( input( "Type a binary value in range [" + ("0"*(len(bin(cellAmountMM)[2:])-1)) + ", " + ("1"*(len(bin(cellAmountMM)[2:])-1)) +"]: " ), 0 )

def verifyAddress(address, flag):
    if(flag==1):
        clearConsole()
        address = input( ("Inválid address!\nType a binary value in range [" + ("0"*(len(bin(cellAmountMM)[2:])-1)) + ", " + ("1"*(len(bin(cellAmountMM)[2:])-1)) +"]: ") )
    try:
        if int(address, 2) >= 0  and int(address, 2) < cellAmountMM:
            return address
        else:
            verifyAddress(address, 1) # Inválid address range
    except:
        verifyAddress(address, 1) # Inválid address range

def verifyValue(value, flag):
    if(flag==1):
        clearConsole()
        value = input( ("Inválid value!\nType a binary value in range [" + bin(0)[2:].zfill(cellBits) +", " + ("1"*cellBits) +"]: ") )
    try:
        if int(value, 2) >= 0 and int(value, 2) <= int(("1"*cellBits), 2):
            return value
        else:
            verifyValue(value, 1) # Inválid value range
    except:
        verifyValue(value, 1) # Inválid value range

def writeContentInMemory():
    #statistics._accessAmount += 1;
    memoryAddress = verifyAddress( ("Inválid address!\nType a binary value in range [" + ("0"*(len(bin(cellAmountMM)[2:])-1)) + ", " + ("1"*(len(bin(cellAmountMM)[2:])-1)) +"]: "), 0 )
    value = verifyValue(input( ("Inválid value!\nType a binary value in range [" + bin(0)[2:].zfill(cellBits) +", " + ("1"*cellBits) +"]: ") ), 0)

    block = cacheMemory.blockIsInCache(memoryAddress)

    if block == None:
        #bloco = memoryCache.readBlockFromMemory(memoryAddress, mainMemory)
        #statistics._accessFaults += 1 # Increment access faults
        statistics._writeFaults += 1 # Increment write faults
    else:
        #statistics._accessHits += 1 # Increment access Hits
        statistics._writeHits += 1 # Increment Write Hits

    # Write data on cache
    cacheMemory.writeData(memoryAddress, value)