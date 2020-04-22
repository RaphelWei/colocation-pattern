from BinaryColocationPattern import BinaryColocationPattern
from GeneralColocationPattern import GeneralColocationPattern

class ColocationPatternGroup():
    def __init__(self, m_basePointGrid, m_piThreshold, m_basePatternGroup = None):
        if m_basePatternGroup is None:
            self.patterns = {}
            eventTypes = list(m_basePointGrid.pointIndex.keys())
            for i in range(len(eventTypes)-1):
                for j in range(i+1, len(eventTypes)):
                    colocationPattern = BinaryColocationPattern(list([eventTypes[i], eventTypes[j]]),
                                                            m_basePointGrid,
                                                            m_piThreshold)
                    if len(colocationPattern.MBR) > 0:
                        self.patterns[colocationPattern.TypeLabel] = colocationPattern

        else:
            patternLabels = list([m_basePatternGroup.Patterns.keys()])
            for i in range(len(patternLabels)-1):
                for j in range(i + 1, len(patternLabels)):
                    colocationPattern = GeneralColocationPattern(m_basePointGrid,
                                                                 m_basePatternGroup.Patterns[patternLabels[i]],
                                                                 m_basePatternGroup.Patterns[patternLabels[j]],
                                                                 m_piThreshold)
                    if (colocationPattern.TypeNumber == 0):
                        continue

                    if (len(colocationPattern.MBR) > 0):

                        self.patterns[colocationPattern.TypeLabel] = colocationPattern

