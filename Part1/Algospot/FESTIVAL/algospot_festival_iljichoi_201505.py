# -*- coding: utf8 -*-
# author: 최일지


def get_minimum_costset(cost_list, l):
    d = []
    min = 0
    for i in xrange(len(cost_list)-l+1):
        if i == 0:
            first = sum(cost_list[:l])
            min = first/l
            d.append(first)
            for j in xrange(l, len(cost_list)):
                app = d[-1]+cost_list[j]
                div = app/(j+1)
                d.append(app)
                if min > div:
                    min = div
        else:
            for j in xrange(i, len(d)):
                d[j] -= cost_list[i-1]
                div = d[j]/(l+j-i)
                if min > div:
                    min = div
    return min



def run():
    for _ in xrange(int(raw_input())):
        l = int(raw_input().split()[1])
        costli = map(float, raw_input().split())
        print '%.10f' % get_minimum_costset(costli, l)

if __name__=='__main__':
    run()