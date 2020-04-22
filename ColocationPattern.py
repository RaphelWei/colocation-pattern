from Point import PointGrid
from CoarseMBR import CoarseMBR
from HelpLib import TwoDimensionalDictionary

class ColocationPattern():
    def __init__(self):
        self.patternTypes = []
        self.typeLabel = "!@#".join(self.patternTypes)
        self.typeNumber = len(self.patternTypes)
        self.instances = []
        self.patternIndex = TwoDimensionalDictionary()
        self.patternPrefixSum = []
        self.participatingPoints = {} # <str, list<int>>
        self.participationPointPrefixSum = {} # <str, [,]>
        self.mbr = {} # <int, CoarseMBR>
        self.mbrNum = 0
        self.mbrIndex = TwoDimensionalDictionary() # {int:{int:list<int>}}
    def AddHotspot(self, m_basePointGrid: PointGrid,
                    m_minRowIndex: int, m_minColumnIndex: int,
                    m_maxRowIndex: int, m_maxColumnIndex: int, 
                    m_piThreshold: float,
                    m_activeCellIdxes: list, m_activeCellList, m_checkedNum: int): 
        mbrInstance = CoarseMBR()
        if self.mbrIndex.ContainsKey(m_minRowIndex, m_minColumnIndex): 
            for mbrId in self.mbrIndex.dict[m_minRowIndex][m_minColumnIndex]: #mbrId -> int
                if (self.mbr[mbrId].maxRowIndex == m_maxRowIndex) and (self.mbr[mbrId].maxColumnIndex == m_maxColumnIndex):
                    if (self.mbr[mbrId].checkedMBR == m_checkedNum) and (len(self.mbr[mbrId].preciseMBRList) != 0):
                        mbrInstance = self.mbr[mbrId]
                        mbrInstance.PreciseSearch(self.patternIndex, self.instances, m_basePointGrid,
                                                  m_piThreshold, m_activeCellIdxes, m_activeCellList, self.participatingPoints)
                    else:
                        return
        if mbrInstance is None:
            mbrInstance = CoarseMBR(self.mbrNum, 
                                    m_minRowIndex, m_minColumnIndex,
                                    m_maxRowIndex, m_maxColumnIndex, 
                                    self.patternTypes, m_basePointGrid, 
                                    self.participationPointPrefixSum
                                    )
            if mbrInstance.maxParticipationIndex >= m_piThreshold:
                mbrInstance.PreciseSearch(self.patternIndex, self.instances, m_basePointGrid,
                                          m_piThreshold, m_activeCellIdxes, m_activeCellList, self.participatingPoints)
                if len(mbrInstance.preciseMBRList) > 0:
                    for otherMinRow in 