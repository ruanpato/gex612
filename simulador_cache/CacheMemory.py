import Line
import math

# Example: cacheMemory = CacheMemory(1, 8, 4, 0)

class CacheMemory:
    def __init__(self, linesAmount, setsSize, blockSize, cellBits):
        self._setsAmount = linesAmount/setsSize # Sets amount is equal linesAmount/setSize
        self._blockSize = blockSize # blockSize = cellsPerBlock
        self._linesCache = linesAmount # linesCache = linesAmount
        self._cellBits = cellBits # Just to print

        # The needed part to represent a cache
        self._lines = []
        for _ in range(linesAmount):
            self._lines.append(Line.Line(blockSize, int(math.log2(blockSize)), int(math.log((linesAmount//setsSize))), cellBits ))

    #            8bits      = 5 bits +   1 bit   +    2 bits
    #       [memoryAddress] = [label]+[setOffSet]+[blockOffset]
    #       Cell == blockOffset = log2(cellsPerBlock) == 2 bits
    #       Set: setOffset = log2(setAmount) == 1 bit
    #       labelBits = memoryAddress.bits()-setOffset.bits()-blockOffset.bits() = 5 bits
    #       |=======================================================================================|
    #       |                                  SET ASSOCIATIVE CACHE                                |
    #       |=======================================================================================|
    #       |               Set: 0                      |             Set: 1                        |
    #       |=======================================================================================|
    #       |           Frame: A (line: 0)              |         Frame: A (line: 1)                |
    #       | LRU | W | V |  Label  | Cell |   Value    | LRU | W | V |  Label  | Cell |   Value    |
    #       |  1  | 0 | 1 |  00000  |  00  |  00000000  |  0  | 0 | 0 |         |  ?   |     ?      |
    #       |     |   |   |         |  01  |  00000000  |     |   |   |         |  ?   |     ?      |
    #       |     |   |   |         |  10  |  00000000  |     |   |   |         |  ?   |     ?      |
    #       |     |   |   |         |  11  |  00000000  |     |   |   |         |  ?   |     ?      |
    #       |---------------------------------------------------------------------------------------|
    #       |           Frame: B (line: 2)              |         Frame: B (line: 3)                |
    #       | LRU | W | V |  Label  | Cell |   Value    | LRU | W | V |  Label  | Cell |   Value    |
    #       |  0  | 0 | 0 |    ?    |  ?   |     ?      |  0  | 0 | 0 |    ?    |  ?   |     ?      |
    #       |     |   |   |         |  ?   |     ?      |     |   |   |         |  ?   |     ?      |
    #       |     |   |   |         |  ?   |     ?      |     |   |   |         |  ?   |     ?      |
    #       |     |   |   |         |  ?   |     ?      |     |   |   |         |  ?   |     ?      |
    #       |---------------------------------------------------------------------------------------|
    #       |           Frame: C (line: 4)              |         Frame: C (line: 5)                |
    #       | LRU | W | V |  Label  | Cell |   Value    | LRU | W | V |  Label  | Cell |   Value    |
    #       |  0  | 0 | 0 |    ?    |  ?   |     ?      |  0  | 0 | 0 |    ?    |  ?   |     ?      |
    #       |     |   |   |         |  ?   |     ?      |     |   |   |         |  ?   |     ?      |
    #       |     |   |   |         |  ?   |     ?      |     |   |   |         |  ?   |     ?      |
    #       |     |   |   |         |  ?   |     ?      |     |   |   |         |  ?   |     ?      |
    #       |---------------------------------------------------------------------------------------|
    #       |           Frame: D (line: 6)              |         Frame: D (line: 7)                |
    #       | LRU | W | V |  Label  | Cell |   Value    | LRU | W | V |  Label  | Cell |   Value    |
    #       |  0  | 0 | 0 |    ?    |  ?   |     ?      |  0  | 0 | 0 |    ?    |  ?   |     ?      |
    #       |     |   |   |         |  ?   |     ?      |     |   |   |         |  ?   |     ?      |
    #       |     |   |   |         |  ?   |     ?      |     |   |   |         |  ?   |     ?      |
    #       |     |   |   |         |  ?   |     ?      |     |   |   |         |  ?   |     ?      |
    #       |---------------------------------------------------------------------------------------|
    #       |=======================================================================================|
    def printAllCache(self):
        div0="|=======================================================================================|"
        print(div0+"\n"+("|{: ^"+str(len(div0)-2)+"s}|\n").format("SET ASSOCIATIVE CACHE")+div0)
        print( ("|{: ^" + str(len(div0)//2-1) + "s}|{: ^" + str(len(div0)//2-1) + "s}|\n").format("Set: 0", "Set: 1")+div0+"\n")
        frame = "A"
        for _ in range(self._lines):
            print("|{: 43^s}|{: 43^s}|".format(("Frame: "+frame+" (Line: "+_+")"), ("Frame: "+frame+" (Line: "+_+")")) )
    def blockIsInCache(self, cellAddressMM):
        