class Statistics:
    def __init__(self):
        # READ
        self._readHits = 0
        self._readFaults = 0
        # WRITE
        self._writeHits = 0
        self._writeFaults = 0
        # CeilDigits
        self._ceilDigits = 0 # Just to print better


    # Function:
    # Ex:
    # |============STATISTICS============|
    # |--------------ACCESS--------------|
    # |            Total: 1233           |
    # |        Hits: 666 = 54.01%        |
    # |       Faults: 567 = 45.98%       |
    # |----------------------------------|
    # |==================================|
    # |---------------READ---------------|
    # |            Total: 666            |
    # |       Hits: 333 = 50.00%         |
    # |      Faults: 333 = 50.00%        |
    # |----------------------------------|
    # |==================================|
    # |--------------WRITE---------------|
    # |           Total: 567             |
    # |       Hits: 333 = 58.74%         |
    # |      Faults: 234 = 41.26%        |
    # |----------------------------------|
    # |==================================|
    def showStatistics(self):
        pass

    def refreshCeilDigits(self, value):
        if len(str(value)) > self._ceilDigits:
            self._ceilDigits = len(str(value))