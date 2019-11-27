from Cell import Cell
class Line:
    def __init__(self, blockSize, cellBits):
        self._cells = []
        for _ in range(blockSize):
            self._cells[_] = Cell(cellBits)
        ## aaaa
        self._dirtyBit = 0 # Receives 1 if value in cache is changed
        self._label = -1 # label = (a bits to represent a block of Main Memory Address)
        self._valid = False # Direct mapping
        self._recentlyUsed = -1 # Initialized
