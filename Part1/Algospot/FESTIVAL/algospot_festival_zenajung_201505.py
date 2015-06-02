#_*_ coding: utf8 _*_
# author: zenajung


def findMinValue(maxLendDay,minFestivalDay,*costList):

    sum = 0
    sumCostList = [sum]
    for i in costList:
        sum = sum + i
        sumCostList.append(sum)


    minValue = sumCostList[-1];

    for n in xrange(minFestivalDay,maxLendDay+1):
        minSum = sumCostList[-1]
        for start in xrange(maxLendDay-n+1):
            #print ("s=%d,n=%d" %(start,n))
            sumValue = sumCostList[start+n] -  sumCostList[start]
            #print ("s=%d,n=%d,sumValue=%d" %(start,n,sumValue))
            if sumValue < minSum :
                minSum = sumValue
        #print("minValue "
        cost = float(minSum) / n
        if minValue > cost :
            minValue =cost


    return minValue


if __name__ == '__main__':

    tc = int (raw_input())
    for i in xrange(tc):
        dayStr = raw_input()
        days = map(int,dayStr.split())
        costStr = raw_input()
        costs = map(int,costStr.split())
        print("%.10f" %  findMinValue(days[0],days[1],*costs))