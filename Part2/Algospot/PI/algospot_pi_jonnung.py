# -*- coding: utf8 -*-


def func3(l):
    a, b, c = l
    if a == b and b == c:
        return 1
    df = b - a
    if df == c - b:
        return 2 if abs(df) == 1 else 5
    elif a == c:
        return 4
    return 10


def func4(l):
    a, b, c, d = l
    if a == b and b == c and c == d:
        return 1
    df = b - a
    if df == c - b and df == d - c:
        return 2 if abs(df) == 1 else 5
    elif a == c and b == d:
        return 4
    return 10


def func5(l):
    a, b, c, d, e = l
    if a == b and b == c and c == d and d == e:
        return 1
    df = b - a
    if df == c - b and df == d - c and df == e - d:
        return 2 if abs(df) == 1 else 5
    elif a == c and b == d and c == e:
        return 4
    return 10


def check_level(pi, i, j):
    if j is 3:
        return func3(pi[i-2:i+1])
    elif j is 4:
        return func4(pi[i-3:i+1])
    else:
        return func5(pi[i-4:i+1])


def calculate(pi):
    pi_len = len(pi)
    optimize_sub = [0] * pi_len
    i = 0
    slice_list = [3, 4, 5]

    while i < pi_len:
        min_sum = 10000 * 10
        if i < 2:
            optimize_sub[i] = 10
        else:
            for k, j in enumerate(slice_list):
                start = (i - j) + 1
                if start == 0:
                    current_sum = check_level(pi, i, j)
                elif start > 0:
                    current_sum = optimize_sub[start-1] + check_level(pi, i, j)
                else:
                    continue

                if current_sum < min_sum:
                    min_sum = current_sum
            optimize_sub[i] = min_sum
        i += 1
    return optimize_sub[pi_len-1]


if __name__ == "__main__":
    for c in xrange(int(raw_input())):
        t = [int(v) for v in list(raw_input())]
        print calculate([int(i) for i in list(t)])

