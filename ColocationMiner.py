from ColocationPatternGroup import ColocationPatternGroup

class ColocationMiner():
    def __init__(self, m_basePointGrid, m_piThreshold):
        self.patternGroups = {} 
        binaryPatternGroup = ColocationPatternGroup(m_basePointGrid, m_piThreshold)
        if len(binaryPatternGroup.patterns) > 0:
            self.patternGroups[2] = binaryPatternGroup
        if len(binaryPatternGroup.patterns) < 2:
            return
        typeNUmber = 3
        while True:
            patternGroup = ColocationPatternGroup(m_basePointGrid, 
                                                  m_piThreshold, 
                                                  self.patternGroups[typeNUmber - 1])
            if len(patternGroup.patterns) > 0:
                self.patternGroups[typeNUmber] = patternGroup
                typeNUmber += 1
            if len(patternGroup.patterns) < 2:
                break
    def WriteToFile(self, m_fileName, m_args, m_timestr):
        f = open(m_fileName, "a")
        f.write(" ".join(m_args))
        f.write("\n{0}".format(m_timestr))
        for groupKey in self.patternGroups.keys():
            f.write(groupKey)
            for pattern in self.patternGroups[groupKey].patterns.values():
                f.write(pattern.ToString())
            f.write("\n*********************************************************************************\n\n\n")
        f.close()

