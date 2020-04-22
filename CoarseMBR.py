from HelpLib import Helper
class CoarseMBR():
    def __init__(self, 
                 m_id: int, 
                 m_minRowIndex: int, m_minColumnIndex: int, 
                 m_maxRowIndex: int, m_maxColumnIndex: int, 
                 m_patternTypes, m_basePointGrid,
                 m_participationPointPrefixSum               
                ): 
        self.id = m_id
        self.minRowIndex = m_minRowIndex
        self.minColumnIndex = m_minColumnIndex
        self.maxRowIndex = m_maxRowIndex
        self.maxColumnIndex = m_maxColumnIndex
        self.patternTypes = m_patternTypes
        self.checkedMBR = None
        self.preciseMBRList = []
        self.maxPI = float("inf")
        self.maxParticipationIndex = self.maxPI

        for evtType in m_patternTypes: 
            maxTotalPointCount = Helper.GetCountInRangeFromPrefixSum(m_basePointGrid.PrefixCountMatrices[evtType], 
                                                                     m_minRowIndex,
                                                                     m_minColumnIndex, 
                                                                     m_maxRowIndex, 
                                                                     m_maxColumnIndex)
            maxTruePointCount = Helper.GetCountInRangeFromPrefixSum(m_participationPointPrefixSum[evtType], 
                                                                     m_minRowIndex,
                                                                     m_minColumnIndex, 
                                                                     m_maxRowIndex, 
                                                                     m_maxColumnIndex)
            minTotalPointCount = Helper.GetCountInRangeFromPrefixSum(m_basePointGrid.PrefixCountMatrices[evtType], 
                                                                     m_minRowIndex + 1,
                                                                     m_minColumnIndex + 1, 
                                                                     m_maxRowIndex - 1, 
                                                                     m_maxColumnIndex - 1)
            minTruePointCount = Helper.GetCountInRangeFromPrefixSum(m_participationPointPrefixSum[evtType], 
                                                                     m_minRowIndex + 1,
                                                                     m_minColumnIndex + 1, 
                                                                     m_maxRowIndex - 1, 
                                                                     m_maxColumnIndex - 1)
            self.minTotalPointNumberIn[evtType] = minTotalPointCount
            self.minTruePointNumberIn[evtType] = minTruePointCount
            self.maxTotalPointNumberIn[evtType] = maxTotalPointCount
            self.maxTruePointNumberIn[evtType] = maxTruePointCount

            if maxTruePointCount < 3: 
                self.maxPI = 0
                break
            
            tmpPI = float(maxTruePointCount) / float(minTotalPointCount - minTruePointCount)
            if self.MaxParticipationIndex > tmpPI:
                self.maxPI = tmpPI

    def PreciseSearch(self, m_patternIndex: TwoDimensionalDictionary, m_colocationInstances, 
                      m_basePointGrid, m_piThreshold,
                      m_activeCellIdxes, m_activeCellList, m_participatingPoints): 
        minX = None
        minY = None
        maxX = None
        maxY = None
        if len(m_activeCellIdxes) == 1:
            activeCell0PatternIdList = m_patternIndex.dict[m_activeCellList[m_activeCellIdxes[0]].GridRowIndex][m_activeCellList[m_activeCellIdxes[0]].GridColumnIndex]
            n = len(activeCell0PatternIdList)
            for activeInstance0IdIdx in range(n):
                activeInstance0Id = activeCell0PatternIdList[activeInstance0IdIdx]
                for activeInstance1IdIdx in range(activeInstance0IdIdx + 1, n):
                    activeInstance1Id = activeCell0PatternIdList[activeInstance1IdIdx]
                    _GetPreciseMBR(list([ activeInstance0Id, activeInstance1Id ]),
                                       m_colocationInstances,
                                       m_patternIndex,
                                       m_basePointGrid,
                                       m_piThreshold, m_participatingPoints)
                    for activeInstance2IdIdx in range(activeInstance1IdIdx + 1, n):
                        activeInstance2Id = activeCell0PatternIdList[activeInstance2IdIdx]
                        if not(_GetPreciseMBR(list([activeInstance0Id, activeInstance1Id, activeInstance2Id]),
                                                m_colocationInstances,
                                                m_patternIndex,
                                                m_basePointGrid,
                                                m_piThreshold, m_participatingPoints)):
                            continue
                        for activeInstance3IdIdx in range(activeInstance2IdIdx + 1, n):
                            activeInstance3Id = activeCell0PatternIdList[activeInstance3IdIdx]
                            _GetPreciseMBR(list([activeInstance0Id, activeInstance1Id, activeInstance2Id, activeInstance3Id]),
                                               m_colocationInstances,
                                               m_patternIndex,
                                               m_basePointGrid,
                                               m_piThreshold, m_participatingPoints)
        elif len(m_activeCellIdxes) == 2:
            activeCell0PatternIdList = m_patternIndex.dict[m_activeCellList[m_activeCellIdxes[0]].GridRowIndex][m_activeCellList[m_activeCellIdxes[0]].GridColumnIndex]
            activeCell1PatternIdList = m_patternIndex.dict[m_activeCellList[m_activeCellIdxes[1]].GridRowIndex][m_activeCellList[m_activeCellIdxes[1]].GridColumnIndex]
            for activeInstance0IdIdx in range(len(activeCell0PatternIdList)):
                activeInstance0Id = activeCell0PatternIdList[activeInstance0IdIdx]
                for activeInstance1IdIdx in range(len(activeCell1PatternIdList)):
                    activeInstance1Id = activeCell1PatternIdList[activeInstance1IdIdx]
                    _GetPreciseMBR(list([activeInstance0Id, activeInstance1Id]),
                                        m_colocationInstances,
                                        m_patternIndex,
                                        m_basePointGrid,
                                        m_piThreshold, m_participatingPoints)

                    for activeInstance2IdIdx in range(activeInstance0IdIdx + 1, len(activeCell0PatternIdList)):
                        activeInstance2Id = activeCell0PatternIdList[activeInstance2IdIdx]
                        if not(_GetPreciseMBR(list([activeInstance0Id, activeInstance1Id, activeInstance2Id]),
                                               m_colocationInstances,
                                               m_patternIndex,
                                               m_basePointGrid,
                                               m_piThreshold, m_participatingPoints)):
                            continue
                        for activeInstance3IdIdx in range(activeInstance2IdIdx + 1, len(activeCell0PatternIdList)):
                            activeInstance3Id = activeCell0PatternIdList[activeInstance3IdIdx]
                            _GetPreciseMBR(list([activeInstance0Id, activeInstance1Id, activeInstance2Id, activeInstance3Id]),
                                              m_colocationInstances,
                                              m_patternIndex,
                                              m_basePointGrid,
                                              m_piThreshold, m_participatingPoints)

                        for activeInstance3IdIdx in range(activeInstance1IdIdx + 1, len(activeCell1PatternIdList)):
                            activeInstance3Id = activeCell1PatternIdList[activeInstance3IdIdx]
                            _GetPreciseMBR(list([activeInstance0Id, activeInstance1Id, activeInstance2Id, activeInstance3Id]),
                                              m_colocationInstances,
                                              m_patternIndex,
                                              m_basePointGrid,
                                              m_piThreshold, m_participatingPoints)



                    for activeInstance2IdIdx in range(activeInstance1IdIdx + 1, len(activeCell1PatternIdList)):
                        activeInstance2Id = activeCell1PatternIdList[activeInstance2IdIdx];
                        if not(_GetPreciseMBR(list([activeInstance0Id, activeInstance1Id, activeInstance2Id]),
                                               m_colocationInstances,
                                               m_patternIndex,
                                               m_basePointGrid,
                                               m_piThreshold, m_participatingPoints)):
                            continue

                        for activeInstance3IdIdx in range(activeInstance2IdIdx + 1, len(activeCell1PatternIdList)):
                            activeInstance3Id = activeCell1PatternIdList[activeInstance3IdIdx]
                            _GetPreciseMBR(list([activeInstance0Id, activeInstance1Id, activeInstance2Id, activeInstance3Id]),
                                              m_colocationInstances,
                                              m_patternIndex,
                                              m_basePointGrid,
                                              m_piThreshold, m_participatingPoints)
        elif len(m_activeCellIdxes) == 3:
            activeCell0PatternIdList = m_patternIndex.dict[m_activeCellList[m_activeCellIdxes[0]].GridRowIndex][m_activeCellList[m_activeCellIdxes[0]].GridColumnIndex]
            activeCell1PatternIdList = m_patternIndex.dict[m_activeCellList[m_activeCellIdxes[1]].GridRowIndex][m_activeCellList[m_activeCellIdxes[1]].GridColumnIndex]
            activeCell2PatternIdList = m_patternIndex.dict[m_activeCellList[m_activeCellIdxes[2]].GridRowIndex][m_activeCellList[m_activeCellIdxes[2]].GridColumnIndex]
            for activeInstance0IdIdx in range(len(activeCell0PatternIdList)): 
                activeInstance0Id = activeCell0PatternIdList[activeInstance0IdIdx]
                for activeInstance1IdIdx in range(len(activeCell1PatternIdList)):
                    activeInstance1Id = activeCell1PatternIdList[activeInstance1IdIdx]
                    for activeInstance2IdIdx in range(len(activeCell2PatternIdList)):
                        activeInstance2Id = activeCell2PatternIdList[activeInstance2IdIdx]
                        if not(_GetPreciseMBR(list([activeInstance0Id, activeInstance1Id, activeInstance2Id]),
                                               m_colocationInstances,
                                               m_patternIndex,
                                               m_basePointGrid,
                                               m_piThreshold, m_participatingPoints)):
                            continue

                        for activeInstance3IdIdx in range(activeInstance0IdIdx + 1, len(activeCell0PatternIdList)):
                            activeInstance3Id = activeCell0PatternIdList[activeInstance3IdIdx]
                            _GetPreciseMBR(list([activeInstance0Id, activeInstance1Id, activeInstance2Id, activeInstance3Id]),
                                              m_colocationInstances,
                                              m_patternIndex,
                                              m_basePointGrid,
                                              m_piThreshold, m_participatingPoints)

                        for activeInstance3IdIdx in range(activeInstance1IdIdx + 1, len(activeCell1PatternIdList)):
                            activeInstance3Id = activeCell1PatternIdList[activeInstance3IdIdx]
                            _GetPreciseMBR(list([activeInstance0Id, activeInstance1Id, activeInstance2Id, activeInstance3Id]),
                                              m_colocationInstances,
                                              m_patternIndex,
                                              m_basePointGrid,
                                              m_piThreshold, m_participatingPoints)

                        for activeInstance3IdIdx in range(activeInstance2IdIdx + 1, len(activeCell2PatternIdList)):
                            activeInstance3Id = activeCell2PatternIdList[activeInstance3IdIdx]
                            _GetPreciseMBR(list([activeInstance0Id, activeInstance1Id, activeInstance2Id, activeInstance3Id]),
                                              m_colocationInstances,
                                              m_patternIndex,
                                              m_basePointGrid,
                                              m_piThreshold, m_participatingPoints)
        elif len(m_activeCellIdxes) == 4:
            activeCell0PatternIdList = m_patternIndex.dict[m_activeCellList[m_activeCellIdxes[0]].GridRowIndex][m_activeCellList[m_activeCellIdxes[0]].GridColumnIndex]
            activeCell1PatternIdList = m_patternIndex.dict[m_activeCellList[m_activeCellIdxes[1]].GridRowIndex][m_activeCellList[m_activeCellIdxes[1]].GridColumnIndex]
            activeCell2PatternIdList = m_patternIndex.dict[m_activeCellList[m_activeCellIdxes[2]].GridRowIndex][m_activeCellList[m_activeCellIdxes[2]].GridColumnIndex]
            activeCell3PatternIdList = m_patternIndex.dict[m_activeCellList[m_activeCellIdxes[3]].GridRowIndex][m_activeCellList[m_activeCellIdxes[3]].GridColumnIndex]
            for activeInstance0IdIdx in range(len(activeCell0PatternIdList)):
                activeInstance0Id = activeCell0PatternIdList[activeInstance0IdIdx]
                for activeInstance1IdIdx in range(len(activeCell1PatternIdList)):
                    activeInstance1Id = activeCell1PatternIdList[activeInstance1IdIdx]
                    for activeInstance2IdIdx in range(len(activeCell2PatternIdList)):
                        activeInstance2Id = activeCell2PatternIdList[activeInstance2IdIdx]
                        status, minX, minY, maxX, maxY = _GetBoundaryIndex(list([activeInstance0Id, activeInstance1Id, activeInstance2Id]), 
                                                 m_colocationInstances,
                                                 minX, 
                                                 minY, 
                                                 maxX, 
                                                 maxY)
                        if not(status):
                            continue

                        for activeInstance3IdIdx in range(len(activeCell3PatternIdList)):
                            activeInstance3Id = activeCell3PatternIdList[activeInstance3IdIdx]
                            _GetPreciseMBR(list([activeInstance0Id, activeInstance1Id, activeInstance2Id, activeInstance3Id]),
                                              m_colocationInstances,
                                              m_patternIndex,
                                              m_basePointGrid,
                                              m_piThreshold, m_participatingPoints)
    
    def _GetBoundaryIndex(self, m_activeInstanceIdxes, m_colocationInstances, m_minX, m_minY, m_maxX, m_maxY):
        m_minX = m_colocationInstances[m_activeInstanceIdxes[0]].xCoordinate
        m_maxX = m_colocationInstances[m_activeInstanceIdxes[0]].xCoordinate
        m_minY = m_colocationInstances[m_activeInstanceIdxes[0]].yCoordinate
        m_maxY = m_colocationInstances[m_activeInstanceIdxes[0]].yCoordinate
        for instanceId in m_activeInstanceIdxes:
            if m_minX > m_colocationInstances[instanceId].xCoordinate:
                m_minX = m_colocationInstances[instanceId].xCoordinate
            elif m_maxX < m_colocationInstances[instanceId].xCoordinate:
                m_maxX = m_colocationInstances[instanceId].xCoordinate
            if m_minY > m_colocationInstances[instanceId].yCoordinate:
                m_minY = m_colocationInstances[instanceId].yCoordinate
            elif m_maxY < m_colocationInstances[instanceId].yCoordinate:
                m_maxY = m_colocationInstances[instanceId].yCoordinate

        if len(m_activeInstanceIdxes) > 2:
            cellEffectiveBoundary = {}
            for instanceIdx in m_activeInstanceIdxes:
                cellEffectiveBoundary[instanceIdx] = []
                if abs(m_minX - m_colocationInstances[instanceIdx].xCoordinate) < 1e-2:
                    cellEffectiveBoundary[instanceIdx].append(1)
                if abs(m_maxX - m_colocationInstances[instanceIdx].xCoordinate) < 1e-2:
                    cellEffectiveBoundary[instanceIdx].append(2)
                if abs(m_minY - m_colocationInstances[instanceIdx].yCoordinate) < 1e-2:
                    cellEffectiveBoundary[instanceIdx].append(3)
                if abs(m_maxY - m_colocationInstances[instanceIdx].yCoordinate) < 1e-2:
                    cellEffectiveBoundary[instanceIdx].append(4)
            d3 = {k:v for k,v in cellEffectiveBoundary.items() if len(v) == 90}
            if len(d3) > 0:
                status = False
            else:
                status = True
        status = True
        return status, m_minX, m_minY, m_maxX, m_maxY

    def _GetPreciseMBR(self, activeInstanceIds, m_colocationInstances, 
                        m_patternIndex, m_basePointGrid, m_piThreshold,
                        m_participatingPoints):
        minX = None
        minY = None
        maxX = None
        maxY = None
        status, minX, minY, maxX, maxY = _GetBoundaryIndex(activeInstanceIds, 
                                                            m_colocationInstances, minX, minY, maxX, maxY)
        if not(status):      
            return False
            
        for oldMBR in self.preciseMBRList:
            if (oldMBR.MinX <= minX) and (oldMBR.MinY <= minY) and (oldMBR.MaxX >= maxX) and (oldMBR.MaxY >= maxY):
                return True

            PreciseMBR mbrInstance = new PreciseMBR(minX, minY, maxX, maxY);

            for (int columnIdx = MinColumnIndex; columnIdx <= MaxColumnIndex; columnIdx++)
            {
                _GetPointsCount(m_participatingPoints, m_basePointGrid, mbrInstance, MinRowIndex, columnIdx);

                if (MaxRowIndex != MinRowIndex)
                {
                    _GetPointsCount(m_participatingPoints, m_basePointGrid, mbrInstance, MaxRowIndex, columnIdx);
                }
            }

            for (int rowIdx = MinRowIndex + 1; rowIdx <= MaxRowIndex - 1; rowIdx++)
            {
                _GetPointsCount(m_participatingPoints, m_basePointGrid, mbrInstance, rowIdx, MinColumnIndex);

                if (MaxColumnIndex != MinColumnIndex)
                {
                    _GetPointsCount(m_participatingPoints, m_basePointGrid, mbrInstance, rowIdx, MaxColumnIndex);
                }
            }


            foreach (var evtType in _patternTypes)
            {
                if (!mbrInstance.TotalPointNumberIn.ContainsKey(evtType))
                {
                    mbrInstance.TotalPointNumberIn.Add(evtType, _minTotalPointNumberIn[evtType]);
                }
                else
                {
                    mbrInstance.TotalPointNumberIn[evtType] += _minTotalPointNumberIn[evtType];
                }

                if (!mbrInstance.TruePointNumberIn.ContainsKey(evtType))
                {
                    mbrInstance.TruePointNumberIn.Add(evtType, _minTruePointNumberIn[evtType]);
                }
                else
                {
                    mbrInstance.TruePointNumberIn[evtType] += _minTruePointNumberIn[evtType];
                }
            }

            mbrInstance.CalculateParticipationIndex();

            if (mbrInstance.ParticipationIndex >= m_piThreshold)
            {
                for (int mbrIdx = PreciseMBRList.Count - 1; mbrIdx >= 0; mbrIdx--)
                {
                    // if this new mbr is larger than any old mbr, remove old one
                    var oldMBR = PreciseMBRList[mbrIdx];
                    if (oldMBR.MinX >= minX && oldMBR.MinY >= minY && oldMBR.MaxX <= maxX && oldMBR.MaxY <= maxY)
                    {
                        PreciseMBRList.RemoveAt(mbrIdx);
                    }
                }
                PreciseMBRList.Add(mbrInstance);
            }

            return true;
        }