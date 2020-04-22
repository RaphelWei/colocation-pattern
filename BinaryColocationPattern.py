from ColocationPattern import ColocationPattern

class BinaryColocationPattern(ColocationPattern):
    def __init__(self, m_patternTypes, m_basePointGrid, m_piThreshold):
        self.patternTypes = m_patternTypes
        for type in self.patternTypes:
            self.participationPointPrefixSum[type] = list([m_basePointGrid.rowGridCount + 1, 
                                                           m_basePointGrid.columnGridCount + 1])
        self.patternPrefixSum = list([m_basePointGrid.rowGridCount + 1, 
                                      m_basePointGrid.columnGridCount + 1])
        BuildInstances(m_basePointGrid)
        GenerateHotspot(m_basePointGrid, m_piThreshold)
    def BuildInstances(self, m_basePointGrid):
        for type in self.patternTypes:
            self.participatingPoints[type] = []
        for aPoint in m_basePointGrid.points