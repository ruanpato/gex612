class Statistics:
    def __init__(self):
        # READ
        self._readHits = 0
        self._readFaults = 0
        # WRITE
        self._writeHits = 0
        self._writeFaults = 0
        # CeilDigits
        #self._ceilDigits = 0 # Just to print better


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
        print("    |============STATISTICS============|\n    |--------------ACCESS--------------|")
        print("    |{: ^34s}|".format("Total: " + str(self._readHits+self._writeHits+self._readFaults+self._writeFaults)))
        print("    |{: ^34s}|".format( "Hits: "+str(self._readHits+self._writeHits)+" = " + ("0.00" if (self._readHits == 0 and self._writeHits == 0) else str(round(((self._readHits+self._writeHits)/(self._readFaults+self._readHits+self._writeHits+self._writeFaults))*100, 2)) )+"%"))
        print("    |{: ^34s}|".format( "Faults: "+str(self._readFaults+self._writeFaults)+" = " + ("0.00" if (self._readFaults == 0 and self._writeFaults == 0) else str(round(((self._readFaults+self._writeFaults)/(self._readFaults+self._readHits+self._writeHits+self._writeFaults))*100, 2)) )+"%"))
        print("    |----------------------------------|\n    |==================================|\n    |---------------READ---------------|")
        print("    |{: ^34s}|".format("Total: " + str(self._readHits+self._readFaults)))
        print("    |{: ^34s}|".format( "Hits: "+str(self._readHits)+" = " + ("0.00" if (self._readHits == 0) else str(round(((self._readHits)/(self._readFaults+self._readHits))*100, 2)) )+"%"))
        print("    |{: ^34s}|".format( "Faults: "+str(self._readFaults)+" = " + ("0.00" if (self._readFaults == 0) else str(round(((self._readFaults)/(self._readFaults+self._readHits))*100, 2)) )+"%"))
        print("    |----------------------------------|\n    |==================================|\n    |--------------WRITE---------------|")
        print("    |{: ^34s}|".format("Total: " + str(self._writeHits+self._writeFaults)))
        print("    |{: ^34s}|".format( "Hits: "+str(self._writeHits)+" = " + ("0.00" if (self._writeHits == 0) else str(round(((self._writeHits)/(self._writeFaults+self._writeHits))*100, 2)) )+"%"))
        print("    |{: ^34s}|".format( "Faults: "+str(self._writeFaults)+" = " + ("0.00" if (self._writeFaults == 0) else str(round(((self._writeFaults)/(self._writeFaults+self._writeHits))*100, 2)) )+"%"))
        print("    |----------------------------------|\n    |==================================|")

#    def refreshCeilDigits(self, value):
#        if len(str(value)) > self._ceilDigits:
#            self._ceilDigits = len(str(value))