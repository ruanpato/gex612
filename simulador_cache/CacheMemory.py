import Line

class CacheMemory:
    def __init__(self, mapping, lines, sets):
        self.mapping = mapping                  # 0 for direct, 1 for assoaciative by sets.
        self.lines = lines                      # Lines
        self.sets = sets                        # Sets
        pass

    def replacementPolicies(self, policy):
        if policy == 0:                         # LRU (Least-Recently Used)
            self.LRU()
        elif policy == 1:                       # RR (Random Replacement)
            self.RR()
        elif policy == 2:                       # LFU (Least-Frequently Used)
            self.LFU()
        elif policy == 3:                       # FIFO (First-in First-Out)
            self.FIFO()
        elif policy == 4:                       # LIFO (Last-in First-Out)
            self.LIFO()
        elif policy == 5:                       # MRU (Most recently used)
            self.MRU()
        elif policy == 6:                       # Belady's
            self.belady()

