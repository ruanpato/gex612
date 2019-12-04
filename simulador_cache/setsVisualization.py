sets = {}

cellSize = 8 #8 Bits
cellsInMainMemory = 128 # Cells
blockSize = 4 # Cells
cacheLines = 8 # Lines == blocks
setLines = 4 # Implies each set will had 4 lines
setIndex = cacheLines//setLines # SetAmount
addressSize = 7
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
# TTTTIOO
address = 127
print("setIndex="+str(setIndex))
print("Block amount = "+str(address//blockSize))
print("BlockOffSet = "+str(address%blockSize))
for _ in range(cellsInMainMemory):
    sett = (_//blockSize)%setIndex
    if not sett in sets:
        sets[sett] = []
    sets[sett].append(_)

for _ in sorted(sets.keys()):
    print("Set["+str(_)+"]: ")
    for i in range(0, len(sets[_])):
        if i%blockSize == 0:
            print("Line[" + str((sets[_][i]//blockSize)%cacheLines) + "] Block("+str(sets[_][i]//blockSize).zfill(len(str(cellsInMainMemory//blockSize)))+"): ", end="")
        print(str(bin(sets[_][i])[2:].zfill( addressSize) ) + "(label[" + str(bin(sets[_][i])[2:].zfill( len(bin(cacheLines)[2:])-1 ) )[-3:] +"])", end="")
        if((i+1)%blockSize == 0 and i != 0):
            print()
        else:
            print(end=' - ')
    print()