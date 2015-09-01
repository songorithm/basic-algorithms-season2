
def encrypt(string):
    string = string.strip()
    firstList = []
    secondList = []
    for index in xrange(len(string)):
        if index % 2 == 0:
            firstList.append(string[index])
        else:
           secondList.append(string[index])

    print(''.join(firstList+secondList))

if __name__ == '__main__':
    tc = int(raw_input())
    for t in xrange(tc):
        string = raw_input()
        encrypt(string)


