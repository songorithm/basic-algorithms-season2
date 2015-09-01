__author__ = 'zena'


def allSame(list):
    x = list[0]
    for y in list[1:]:
        if x != y :
            return False
    return True

def incNumber(list):
    delta = list[0] - list[1]
    if abs(delta) != 1:
        return False

    last = list[1]
    for y in list[2:]:
        if last - y != delta :
            return False
        last = y
    return True

def alterNumber(list):

    for i in range( 2,len(list)):
        if list[i] != list[i % 2]:
            return False
    return True


def incSomeNumber(list):
    delta = list[0] - list[1]
    last = list[1]
    for y in list[2:]:
        if last - y != delta :
            return False
        last = y
    return True




def getPoint(list):

    if list[0] == list[1]:
        if allSame(list):
            return 1
        return 10

    if list[0] == list[2]:
        if alterNumber(list):
            return 4
        return 10

    if list[0] - list[1] == list[1] - list[2]:
        if incNumber(list):
            return 2
        if incSomeNumber(list):
            return 5
    return 10


def getPointAll(list):

    p3 = getPoint(list[2:])
    if p3 == 10 :
        return p3, p3, p3

    p5 = getPoint(list)
    if p5 < 10:
        return p5,p5,p5


    return p3, getPoint(list[1:]), p5


def pi_rec(list,index,min_buffer):


    min_buffer[0] = getPoint(list[0:3])
    min_buffer[1] = getPoint(list[0:4])
    min_buffer[2] = getPoint(list[0:5])

    min_buffer[3] = min_buffer[0] + getPoint(list[3:6])
    min_buffer[4] = min(min_buffer[0] + getPoint(list[3:7]),min_buffer[1] + getPoint(list[4:7]))


    for i in xrange(0,len(list)-7) :

        sp3, sp4, sp5 = getPointAll(list[i+3:i+8])

        p5 = min_buffer[i] + sp5
        p4 = min_buffer[i+1] + sp4
        p3 = min_buffer[i+2] + sp3

        #p5 = min_buffer[i] + getPoint(list[i+4:i+9])
        #p4 = min_buffer[i+1] + getPoint(list[i+5:i+9])
        #p3 = min_buffer[i+2] + getPoint(list[i+6:i+9])


        min_buffer[i+5]  = min(p5,p4,p3)

    return min_buffer[len(list)- 3]





def pi(d):

    d_len = len(d)
    #print(d_len)
    min_buffer = [-1]*d_len
    list = [int(x) for x in d]
    #print(list)

    return  pi_rec(list,0, min_buffer)



if __name__ == '__main__':


    tc = int(raw_input())
    for i in xrange(tc):
        ln = raw_input()
        ln = ln.strip()
        #print(ln)
        print( pi(ln) )



