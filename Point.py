import numpy as np
from HelpLib import TwoDimensionalDictionary

class PointBase(object):
    def __init__(self):
        self.id = None
        self.xCoordinate = None
        self.yCoordinate = None
        self.gridColumnIndex  =None
        self.gridRowIndex = None
    def GenerateGridIndex(self, m_gridSize, m_gridXmin, m_gridYmin):
        self.gridColumnIndex = int(np.floor((self.xCoordinate - m_gridXmin) / m_gridSize))
        self.gridRowIndex = int(np.floor((self.yCoordinate - m_gridYmin) / m_gridSize))

    def DistanceTo(self, m_another):
        dist = np.sqrt((self.xCoordinate - m_another.xCoordinate) ** 2 + (self.yCoordinate - m_another.yCoordinate) ** 2)
        return dist
    def DistanceBetween(self, m_pointA, m_pointB):
        return m_pointA.DistanceTo(m_pointB)

class PointEvent(PointBase):
    def __init__(self, m_id, m_x, m_y, m_type):
        self.id = m_id
        self.xCoordinate = m_x
        self.yCoordinate = m_y
        self.typeLabel = m_type
        self.neighborPointIds = {} # a dictionary, {string, list<int>}
    def AddNeighbor(self, new_evt):
        if not(new_evt.typeLabel in self.neighborPointIds):
            self.neighborPointIds[new_evt.typeLabel] = new_evt.Id

class PointGrid(object):
    def __init__(self, m_distance):
        self.gridEdgeLength = m_distance
        self.xMin = float("inf")
        self.xMax = float("-inf")
        self.yMin = float("inf")
        self.yMax = float("-inf")
        self.rowGridCount = None
        self.columnGridCount = None
        self.points = [] # list<pointevent>
        self.pointIndex = TwoDimensionalDictionary() # nested dict, for type T, {T: {T: List<int>}}
        self.prefixCountMatrices = {} #dict, {str: int[,]}

    def QuerypointNumberofType(self, m_type):
        return self.prefixCountMatrices[m_type][self.rowGridCount, self.columnGridCount]

