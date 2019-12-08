import Cell
import Line
import math

# Example: cacheMemory = CacheMemory(1, 8, 4, 0)

class CacheMemory:
    def __init__(self, linesAmount, setsSize, blockSize, cellBits):
        #self._setsAmount = int(linesAmount//setsSize) # Sets amount is equal linesAmount/setSize
        #self._blockSize = blockSize # blockSize = cellsPerBlock
        #self._linesCache = int(linesAmount) # linesCache = linesAmount
        #self._cellBits = cellBits # Just to print

        # LRU
        self._lru = [] # Create a list of bits to LRU for each set
        for _ in range(int(linesAmount//setsSize)):
            self._lru.append("0".zfill( len(bin(linesAmount//int(linesAmount//setsSize))[2:])-1 ) )

        # The needed part to represent a cache
        self._lines = []
        for _ in range(linesAmount):
            self._lines.append(Line.Line(blockSize, int(math.log2(blockSize)), int(math.log((linesAmount//setsSize))), cellBits ))
    #            8bits      = 5 bits +   1 bit   +    2 bits
    #       [memoryAddress] = [label]+[setOffSet]+[blockOffset]
    #       Cell == blockOffset = log2(cellsPerBlock) == 2 bits
    #       Set: setOffset = log2(setAmount) == 1 bit
    #       labelBits = memoryAddress.bits()-setOffset.bits()-blockOffset.bits() = 5 bits
    #       |============================================================================|
    #       |                           SET ASSOCIATIVE CACHE                            |
    #       |============================================================================|
    #       |           Set: 0 LRU: 00            ||           Set: 1 LRU: 00            |
    #       |============================================================================|
    #       |         Frame: A (Line: 0)          ||         Frame: B (Line: 1)          |
    #       | W | V |  Label  | Cell |   Value    || W | V |  Label  | Cell |   Value    |
    #       | 0 | 0 |    ?    |  00  |     ?      || 0 | 0 |    ?    |  00  |     ?      |
    #       |                 |  01  |     ?      ||                 |  01  |     ?      |
    #       |                 |  10  |     ?      ||                 |  10  |     ?      |
    #       |                 |  11  |     ?      ||                 |  11  |     ?      |
    #       |----------------------------------------------------------------------------|
    #       |         Frame: C (Line: 2)          ||         Frame: D (Line: 3)          |
    #       | W | V |  Label  | Cell |   Value    || W | V |  Label  | Cell |   Value    |
    #       | 0 | 0 |    ?    |  00  |     ?      || 0 | 0 |    ?    |  00  |     ?      |
    #       |                 |  01  |     ?      ||                 |  01  |     ?      |
    #       |                 |  10  |     ?      ||                 |  10  |     ?      |
    #       |                 |  11  |     ?      ||                 |  11  |     ?      |
    #       |----------------------------------------------------------------------------|
    #       |         Frame: E (Line: 4)          ||         Frame: F (Line: 5)          |
    #       | W | V |  Label  | Cell |   Value    || W | V |  Label  | Cell |   Value    |
    #       | 0 | 0 |    ?    |  00  |     ?      || 0 | 0 |    ?    |  00  |     ?      |
    #       |                 |  01  |     ?      ||                 |  01  |     ?      |
    #       |                 |  10  |     ?      ||                 |  10  |     ?      |
    #       |                 |  11  |     ?      ||                 |  11  |     ?      |
    #       |----------------------------------------------------------------------------|
    #       |         Frame: G (Line: 6)          ||         Frame: H (Line: 7)          |
    #       | W | V |  Label  | Cell |   Value    || W | V |  Label  | Cell |   Value    |
    #       | 0 | 0 |    ?    |  00  |     ?      || 0 | 0 |    ?    |  00  |     ?      |
    #       |                 |  01  |     ?      ||                 |  01  |     ?      |
    #       |                 |  10  |     ?      ||                 |  10  |     ?      |
    #       |                 |  11  |     ?      ||                 |  11  |     ?      |
    #       |----------------------------------------------------------------------------|
    #       |============================================================================|
    def printAllCache(self, setsAmount):
        div0="|============================================================================|"
        print("    "+div0+"\n"+"    "+("|{: ^"+str(len(div0)-2)+"s}|\n").format("SET ASSOCIATIVE CACHE")+"    "+div0)
        print("    "+ ("|{: ^" + str(len(div0)//2-2) + "s}||{: ^" + str(len(div0)//2-2) + "s}|\n").format( ("Set: 0 LRU: "+self._lru[0]), ("Set: 1 LRU: "+self._lru[1]))+"    "+div0)
        frame = "A"
        for i in range(len(self._lines)//setsAmount):
            print("    |{: ^37s}||{: ^37s}|".format( str("Frame: "+frame+" (Line: "+str(i+i)+")"), str("Frame: "+chr(ord(frame)+1)+" (Line: "+str(i+i+1)+")") ) )
            print("    |{: ^37s}||{: ^37s}|".format( (" W | V |  Label  | Cell |   Value    ") , (" W | V |  Label  | Cell |   Value    ") ))
            print("    |{: ^3s}|{: ^3s}|{: ^9s}|{: ^6s}|{: ^12s}||{: ^3s}|{: ^3s}|{: ^9s}|{: ^6s}|{: ^12s}|".format(self._lines[i+i]._writeBit, self._lines[i+i]._validBit, self._lines[i+i]._label if self._lines[i+i]._validBit == "1" else "?", "00", self._lines[i+i]._cells[0]._bits  if self._lines[i+i]._validBit == "1" else "?", self._lines[i+i+1]._writeBit, self._lines[i+i+1]._validBit, self._lines[i+i+1]._label if self._lines[i+i+1]._validBit == "1" else "?", "00", self._lines[i+i+1]._cells[0]._bits if self._lines[i+i+1]._validBit == "1" else "?"))
            print("    |{: ^17s}|{: ^6s}|{: ^12s}||{: ^17s}|{: ^6s}|{: ^12s}|".format("", "01", self._lines[i+i]._cells[1]._bits if self._lines[i+i]._validBit == "1" else "?", "", "01", self._lines[i+i+1]._cells[1]._bits if self._lines[i+i+1]._validBit == "1" else "?"))
            print("    |{: ^17s}|{: ^6s}|{: ^12s}||{: ^17s}|{: ^6s}|{: ^12s}|".format("", "10", self._lines[i+i]._cells[2]._bits if self._lines[i+i]._validBit == "1" else "?", "", "10", self._lines[i+i+1]._cells[2]._bits if self._lines[i+i+1]._validBit == "1" else "?"))
            print("    |{: ^17s}|{: ^6s}|{: ^12s}||{: ^17s}|{: ^6s}|{: ^12s}|".format("", "11", self._lines[i+i]._cells[3]._bits if self._lines[i+i]._validBit == "1" else "?", "", "11", self._lines[i+i+1]._cells[3]._bits if self._lines[i+i+1]._validBit == "1" else "?"))
            print("    |{:-^76s}|".format(""))
            i = i + 2
            frame = chr(ord(frame)+2)
        print("    |{:=^76s}|".format(""))

    # Function: putBlock(self, address, block)
    # Arguments: self(object), address(string[bin])
    # Return: block[Cell(),...]
    # Description: Using the address read a block from Main Memory, and return the block
    def putBlock(self, address, block):
        setIndex = address[-3]
        label = address[:-3]
        linePosition = int(self._lru[int(setIndex)], 2)
        if (self._lines[linePosition+int(setIndex, 2)+linePosition]._validBit == "0") or (self._lines[linePosition+int(setIndex, 2)+linePosition]._writeBit == "0"): # If have a blank space in set or don't need writeback
            self._lines[linePosition+int(setIndex, 2)+linePosition]._label = label # put the label in line cache
            self._lines[linePosition+int(setIndex, 2)+linePosition]._validBit = "1" # Set the validBit to 1
            for _ in range(len(block)):
                self._lines[linePosition+int(setIndex, 2)+linePosition]._cells[_]._bits = block[_]._bits # Put the block on the line
            # Increment LRU
            if linePosition == 3:
                self._lru[int(setIndex)] = "00"
            else:
                self._lru[int(setIndex)] = bin(linePosition+1)[2:].zfill(2) # Increment LRU
            return None, None
        # WriteBack
        elif self._lines[linePosition+int(setIndex, 2)+linePosition]._writeBit == "1": # If need write the value on mainMemory before put the new block on cache
            mainMemoryBlock = []

            for _ in range(len(self._lines[linePosition+int(setIndex, 2)+linePosition]._cells)):
                mainMemoryBlock.append(self._lines[linePosition+int(setIndex, 2)+linePosition]._cells[_]._bits) # Save the block "Dirty" to return and put on main memory
            mainMemoryInitialAddress = ((self._lines[linePosition+int(setIndex, 2)+linePosition]._label)+setIndex+"00") # Return the address of initial cell of the block
            self._lines[linePosition+int(setIndex, 2)+linePosition]._label = label # put the new label in line cache
            self._lines[linePosition+int(setIndex, 2)+linePosition]._writeBit = "0" # Set the validBit to 1

            for _ in range(len(block)):
                self._lines[linePosition+int(setIndex, 2)+linePosition]._cells[_]._bits = block[_]._bits # Put the block on the line

            # Increment LRU
            if linePosition == 3:
                self._lru[int(setIndex)] = "00"
            else:
                self._lru[int(setIndex)] = bin(linePosition+1)[2:].zfill(2)
            return mainMemoryInitialAddress, mainMemoryBlock

    def blockIsInCache(self, address):
        setIndex = address[-3]
        label = address[:-3]
        #linePosition = self._lru[int(setIndex)]
        if setIndex == "0":
            for _ in range(8//2):
                if self._lines[_+_]._label == label: # if value already is in cache
                    return 1 # Means a hit
        elif setIndex == "1":
            for _ in range(8//2):
                if self._lines[_+_+1]._label == label:
                    return 1 # Means a hit
        return 0 # Means Fault

    def getLineInCache(self, address):
        setIndex = address[-3]
        label = address[:-3]
        #linePosition = self._lru[int(setIndex)]
        if setIndex == "0":
            for _ in range(8//2):
                if self._lines[_+_]._label == label: # if value already is in cache
                    return _+_
        elif setIndex == "1":
            for _ in range(8//2):
                if self._lines[_+_+1]._label == label:
                    return _+_+1
        return -1 # Block Isn't in cache

    def writeCellInCache(self, value, address):
        setIndex = address[-3]
        label = address[:-3]
        pass