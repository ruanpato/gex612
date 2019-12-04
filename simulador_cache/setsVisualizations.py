import math

sets = {}

# Values informed
cellsInMainMemory = 128 # Cells
blockSize = 4 # Cells
cacheLines = 8 # Lines == blocks
cellSize = 8 # 8 Bits
setLines = 4 # Implies each set will had 4 lines

# Calculated values
setAmount = cacheLines//setLines # SetAmount
bitsToRepresentAddress = len(bin(cellsInMainMemory)[2:])-1 # 7 bits
indexSize = int(math.log2(setAmount)) # 1 bit
blockOffset = len(bin(blockSize)[2:])-1 # 2 bits
labelSize = bitsToRepresentAddress-indexSize-blockOffset # 4 bits

# blockAddress = (cellAddress//blockSize)
# blockSet = BlockAddress%setAmount
# digitsToRepresentCacheLineAddress = len(bin(CacheLines)[2:])-1
# blockOffset = cellAddress[digitsToRepresentCacheLineAddress:]
# The last cacheLines digits of MainMemoryAddress is offset in block
#print(setIndex)
# |
# len(bin(amountCellsMain))-1 == len(bin(128))-1 == len(10000000)-1 == 8-1 == 7 bits == bitsToRepresentAddressInMain
# T = Tag() = bitsToRepresentAddressInMain-Index-blockOffset
# I = Index(Set) = log2(setAmount). Ex: log2(2) == 1 bit
# O = BlockOffset = (4 cells per block) == len(bin(4))-1 == len(100)-1 == 3-1 == 2 bits
# TTTT I OO

print("|{:=^46s}|".format(""))
print("| {:>28s}: {:<14s} |".format("Cells in main memory", (str(cellsInMainMemory) + " bits")) )
print("| {:>28s}: {:<14s} |".format("Block size", (str(blockSize) + " cells")) )
print("| {:>28s}: {:<14s} |".format("Cache", (str(cacheLines) + " lines")) )
print("| {:>28s}: {:<14s} |".format("Cells size", (str(cellSize) + " bits")) )
print("| {:>28s}: {:<14s} |".format("Cache sets size", (str(setLines) + " lines")) )
print("|{:-^46s}|".format(""))
print("| {:>28s}: {:<14s} |".format("Main memory representation", (str(bitsToRepresentAddress) + " bits")) )
print("| {:>28s}: {:<14s} |".format("Set amount", (str(setAmount) + " sets") ))
print("| {:>28s}: {:<14s} |".format("Block amount", (str(cellsInMainMemory//blockSize) + " blocks") ))
print("|{:=^46s}|".format(""))

mainMemory = []
# Fill memory
for _ in range(cellsInMainMemory):
    mainMemory.append(bin(_)[2:].zfill(bitsToRepresentAddress))
    print(_, ": ", bin(_)[2:].zfill(bitsToRepresentAddress)[:-(indexSize+blockOffset)] + " " + bin(_)[2:].zfill(bitsToRepresentAddress)[labelSize]+" "+bin(_)[2:].zfill(bitsToRepresentAddress)[-blockOffset:])
    # Initialize sets
    for i in range(setAmount):
        if not i in sets:
            sets[i] = []
        if int(mainMemory[_][labelSize]) == i:
            if not mainMemory[_] in sets[i]:
                sets[i].append(mainMemory[_])
#
for _ in sorted(sets.keys()):
    print("Set{"+str(_)+"}: ")
    for i in range(0, len(sets[_])):
        if i%blockSize == 0:
            print("Line in Cache[" + str( (int(sets[_][i], 2)//blockSize)%cacheLines) + "] = ", end="")
            print("Block in MM(" + str( (int(sets[_][i], 2)//blockSize)).zfill(len(bin(cacheLines//blockSize)[2:])) + "): ")
        print( sets[_][i][:-(indexSize+blockOffset)]+" "+sets[_][i][labelSize]+" "+sets[_][i][-blockOffset:], end="")
        #print(str(bin(sets[_][i])[2:].zfill( addressSize) ) + "(label[" + str(bin(sets[_][i])[2:].zfill( len(bin(cacheLines)[2:])-1 ) )[-3:] +"])", end="")
        if((i+1)%blockSize == 0 and i != 0):
            print()
        else:
            print(end=' || ')
    print()