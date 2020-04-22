class PreciseMBR():
    def __init__(self, m_minX, m_minY, m_maxX, m_maxY):
        self.minX = m_minX
        self.minY = m_minY
        self.maxX = m_maxX
        self.maxY = m_maxY
        self.totalPointNumberIn = {} #<str, int>
        self.truePointNumberIn = {} #<str, int>
        self.participationIndex = None
    def CalculateParticipationIndex(self):
        self.participationIndex = float("inf")
        if len(self.totalPointNumberIn.keys()) == 0:
            self.participationIndex = 0
            return
        for evtType in self.totalPointNumberIn.keys():
            if (self.truePointNumberIn[evtType] < 2) or (self.totalPointNumberIn[evtType] == 0):
                self.participationIndex = 0
                break
            tmp = float(self.truePointNumberIn[evtType]) / float(self.totalPointNumberIn[evtType])
            if tmp < self.participationIndex:
                self.participationIndex = tmp
    def ToString(self):
        totalPointStr = ""
        truePointStr = ""
        for evtType in self.TotalPointNumberIn.keys():
            totalPointStr += " {0}: {1}".format(evtType, self.totalPointNumberIn[evtType])
            truePointStr += " {0}: {1}".format(evtType, self.truePointNumberIn[evtType])
        return "[PreciseMBR: MinX={0}, MaxX={1}, MinY={2}, MaxY={3}, \nTotalPointNumberIn= {4}, \nTruePointNumberIn= {5}, \nParticipationIndex={6}]".format(
            self.minX, self.maxX, self.minY, self.maxY, totalPointStr, truePointStr, self.participationIndex)