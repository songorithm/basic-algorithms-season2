# -*- coding: utf8 -*-
# author: Eunwoo Cho <jonnung@gmail.com>

import cProfile
from random import randint


def solve_festival(l, c, t):
    min_avg = sum(l) / float(c)
    last_start_index = c - t + 1

    for start in range(last_start_index):
        end = start + t
        tmp_list = l[start:end]
        tmp_sum = sum(tmp_list)
        tmp_len = end - start
        tmp_avg = tmp_sum / float(tmp_len)

        if min_avg > tmp_avg:
            min_avg = tmp_avg

        while end < c:
            tmp_sum += l[end]
            tmp_len += 1
            tmp_avg = tmp_sum / float(tmp_len)
            if min_avg > tmp_avg:
                min_avg = tmp_avg
            end += 1
    return min_avg

if __name__ == '__main__':
    test_case = int(raw_input())
    for tc in xrange(test_case):
        days_count, team_count = [int(x) for x in raw_input().split()]
        days_list = [int(y) for y in raw_input().split()]
        print("%.12f" % solve_festival(days_list, days_count, team_count))
    # days_list = [randint(1, 100) for x in range(1000)]
    # # days_list = [int(x) for x in "9 9 4 9 2 4".split()]
    # days_count = 1000
    # team_count = 3
    # cProfile.run('solve_festival(days_list, days_count, team_count)')
    # print("%.12f" % solve_festival(days_list, days_count, team_count))
