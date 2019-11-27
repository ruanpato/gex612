import Line

# Example: cacheMemory = CacheMemory(1, 8, 4, 0)

class CacheMemory:
    def __init__(self, mapping, linesAmount, setsSize, replacementPolicy, writePolicy, blockSize, cellBits):
        self._mapping = mapping # 0 for direct, 1 for associative by sets.
        self._replacementPolicy = replacementPolicy # Code's to replacement policies
        self._writePolicy = writePolicy # Code to write policy
        self._setsSize = setsSize # Sets quantity is equal linesAmount/setSize

        # The needed part to represent a cache
        self._lines = []
        for _ in range(linesAmount):
            self._lines[_] = Line.Line(blockSize, cellBits)

#    def replacementPolicies(self, policy):
#        if policy == 0:                         # LRU (Least-Recently Used)
#            self.LRU()
#        elif policy == 1:                       # RR (Random Replacement)
#            self.RR()
#        elif policy == 2:                       # LFU (Least-Frequently Used)
#            self.LFU()
#        elif policy == 3:                       # FIFO (First-in First-Out)
#            self.FIFO()
#        elif policy == 4:                       # LIFO (Last-in First-Out)
#            self.LIFO()
#        elif policy == 5:                       # MRU (Most recently used)
#            self.MRU()
