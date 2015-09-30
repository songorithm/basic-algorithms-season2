# -*- coding: utf8 -*-

if __name__ == '__main__':
    #  입력 1: Test case (test_case)
    #  입력 2: 배열의 길이 (unsorted_list_length)
    #  입력 3: 원본 배열의 각 요소가 왼쪽으로 움직인 회수를 저장한 리스트 (moving_count_list)
    test_case = int(raw_input())
    for test in xrange(test_case):
        unsorted_list_length = int(raw_input())
        moving_count_list = [int(a) for a in raw_input().split()]

        sorted_list = range(1, unsorted_list_length + 1)
        unsorted_list = [0] * unsorted_list_length

        for x in reversed(xrange(unsorted_list_length)):
            insertion_back = x - moving_count_list[x]
            unsorted_list[x] = str(sorted_list[insertion_back])
            del sorted_list[insertion_back]

        print(' '.join(unsorted_list))
