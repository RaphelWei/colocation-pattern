from collections import defaultdict

class Helper():
    def CalculatePrefixSum(self, m_matrix, m_rowNumber, m_columnnumber):
        for i in range(m_rowNumber):
            for j in range(m_columnnumber):
                m_matrix[i, j] += m_matrix[i-1, j]
        for i in range(m_columnnumber):
            for j in range(m_rowNumber):
                m_matrix[j, i] += m_matrix[j, i-1]
    def GetCountInRangeFromPrefixSum(self, m_matrix, m_minRowIndex, m_minColumnIndex, m_maxRowIndex, m_maxColumnIndex):
        if (m_minRowIndex > m_maxRowIndex) or (m_minColumnIndex > m_maxColumnIndex):
            return 0
        return (m_matrix[m_maxRowIndex + 1, m_maxColumnIndex + 1] - m_matrix[m_maxRowIndex + 1, m_minColumnIndex]- m_matrix[m_minRowIndex, m_maxColumnIndex + 1] + m_matrix[m_minRowIndex, m_minColumnIndex])

class TwoDimensionalDictionary():
    def __init__(self):
        self.dict = defaultdict(dict)
    def ContainsKey(self, m_rowKey, m_columnKey):
        if not(m_rowKey in self.dict):
            return False
        if not(m_columnKey in self.dict[m_rowKey]):
            return False
        return True
    def Add(self, m_rowKey, m_columnKey, m_addValue):
        if not(m_rowKey in self.dict):
            self.dict[m_rowKey] = {}
            self.dict[m_rowKey][m_columnKey] = []
        elif not(m_columnKey in self.dict[m_rowKey]):
            self.dict[m_rowKey][m_columnKey] = []
        self.dict[m_rowKey][m_columnKey].append(m_addValue)