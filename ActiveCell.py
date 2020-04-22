class ActiveCell(object):
    def __init__(self, m_id: int, m_rowIdx: int, m_columnIdx: int):
        self.id = m_id
        self.gridRowIndex = m_rowIdx
        self.gridColumnIndex = m_columnIdx
    def Equals(self, obj: object):
        if type(obj) is not ActiveCell:
            return False
        else:
            return (True if obj.id == self.id else False)
    def GetHashCode(self):
        return hash(self.id)