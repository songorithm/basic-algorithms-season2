# -*- coding: utf8 -*-
# author: Sangbae Lim <itwizard1@gmail.com>


def Calculate_Min_Cost(nDay, nTeam, FestivalCostList):
    LowestCost=100
    tempAvgCost=[]
    for x in xrange(0,nDay - nTeam + 1):
        tempTotal=sum(FestivalCostList[x:nTeam+x-1]) * 1.0
        for y in xrange(nTeam + x-1, nDay):
            tempTotal += FestivalCostList[y]
            tempAvgCost.append(tempTotal/(y-x+1))
    LowestCost = min(tempAvgCost)

    return LowestCost

tc = int(raw_input())

for t in xrange(tc):
    nDay, nTeam = [int(x) for x in raw_input().split()]
    FestivalCostList = [int(x) for x in raw_input().split()]
    
    print '%.11f' % Calculate_Min_Cost(nDay, nTeam, FestivalCostList)