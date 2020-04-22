from Point import PointBase

class ColocationInstance(PointBase):
    def __init__(self, m_id, m_eventIndices, m_basePointGrid):
        self.id = m_id
        self.eventIndices = m_eventIndices
        self.xCoordinate = 0
        self.yCoordinate = 0
        for pointIndex in m_eventIndices:
            self.xCoordinate += m_basePointGrid.Points[pointIndex].xCoordinate
            self.yCoordinate += m_basePointGrid.Points[pointIndex].yCoordinate
        self.xCoordinate /= len(m_eventIndices)
        self.yCoordinate /= len(m_eventIndices)
        super().GenerateGridIndex(m_basePointGrid.GridEdgeLength, m_basePointGrid.xMin, m_basePointGrid.yMin)