#_*_ coding: utf8 _*_

def checkBracket(bracketStr):



    stack = []
    openStr = "{[("
    pair = {'{':'}','[':']','(':')' }
    #pair = {'}':'{',']':'[',')':'(' }


    for c in bracketStr:
        if c in openStr:
            stack.append(pair[c])
        else:
            if not stack:
                return "NO"
            if c != stack.pop():
                return "NO"
    if stack:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':

    tc = int (raw_input())
    for i in xrange(tc):
        bracketStr = raw_input()
        print( checkBracket(bracketStr))
