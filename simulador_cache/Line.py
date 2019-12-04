from Cell import Cell
class Line:
    def __init__(self, blockSize, cellOffset, setOffset, cellBits):
        self._lru = "0"*setOffset # Initialize
        self._writeBit = False  # Initialize
        self._validBit = False  # Initialize
        self._label = "0"*(cellBits-cellOffset-setOffset) # Initialize
        self._cells = [] # Cell pos is CellOfSet

        for _ in range(blockSize):
            self._cells.append(Cell(cellBits))