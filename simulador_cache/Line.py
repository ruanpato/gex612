from Cell import Cell
class Line:
    def __init__(self, blockSize, cellOffset, setOffset, cellBits):
        self._writeBit = "0"  # Initialize
        self._validBit = "0"  # Initialize
        self._label = "0"*(cellBits-cellOffset-setOffset) # Initialize
        self._cells = [] # Cell pos is CellOfSet

        for _ in range(blockSize):
            self._cells.append(Cell(cellBits))