# -*- coding: utf8 -*-


def matches(top, i):
    open = "({["
    close = ")}]"
    return open.index(top) == close.index(i)

if __name__ == "__main__":
    tc = int(raw_input())
    for t in range(tc):
        bracket = raw_input()
        balanced = True
        left = []
        right = []
        for i in bracket:
            if i in '({[':
                left.append(i)
            else:
                if left == []:
                    balanced = False
                else:
                    top = left.pop()
                    if not matches(top, i):
                        balanced = False

        if left == [] and balanced:
            print 'YES'
        else:
            print 'NO'

