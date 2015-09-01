# -*- coding: utf-8 -*-

__author__ = 'markers'

import sys
import operator
readline = lambda : sys.stdin.readline()


"""
'''
    return 값은 무엇으로??? 참 거짓...? 찾을 수 있는 경우의 수가 몇가지이냐를 찾는것..
'''
def find_couples_count(couples, students):

    sum = 0
    for _ in xrange(len(students)):
        if not students  :  # 만약 매칭될 애가 없으면 끝  , base
            return 1
        if not couples:
            return 0


        if couples[0][0] in students and couples[0][1] in students : # 그렇지 않다면...
            students.remove(couples[0][0])
            students.remove(couples[0][1])
        del couples[0]
    #del couples[0]

        sum += find_couples_count(couples[:], students[:])

    #print type(couples)
    #print couples
    #print students
    return sum
"""


def find_goal(couples, friends, students):

    import copy

    sum = 0
    for index in xrange(friends):
        temp_students = copy.deepcopy(students)

        temp_students.remove(couples[index][0])
        temp_students.remove(couples[index][1])

        if not temp_students:
            sum += 1
            break

        if not couples:
            break

        for inner_index in xrange(friends):

            if couples[inner_index][0] in temp_students and couples[inner_index][1] in temp_students:
                temp_students.remove(couples[inner_index][0])
                temp_students.remove(couples[inner_index][1])



            if not temp_students:
                sum += 1
                break

            if not couples:
                break

    return sum


for _ in xrange(int(readline())):
    number_of_students, friends = map(int, readline().split())
    couples = map(int, readline().split())
    list_of_couples = [ ]
    students = [ x for x in range(number_of_students) ]
    #print students
    for index in xrange(friends):

        list_of_couples.append( sorted( ( couples[ 2 * index], couples[ 2 * index + 1 ] ) ) )
        list_of_couples.sort(key = operator.itemgetter(0,1))
        #list_of_couples = sorted(list_of_couples, key = operator.itemgetter(0,1))
    #print list_of_couples

    #print find_couples_count(list_of_couples, students)
    print find_goal(list_of_couples, friends, students)




""""
import sys
rl = lambda: sys.stdin.readline()

n = int(rl())

def check(n, matched, matches, student_num):
    if n == student_num:
        return 1
    current_sum = 0
    if matched[n] != -1:
        return check(n+1, matched, matches, student_num)
    for target in matches[n]:
        if matched[target] != -1:
            continue
        matched[n] = target
        matched[target] = n
        current_sum += check(n+1, matched, matches, student_num)
        matched[n] = -1
        matched[target] = -1
    return current_sum

for i in range(n):
    student_num, match_num = [int(x) for x in rl().split()]
    current_sum = 0
    line = rl().split()
    matches = [[] for x in range(student_num)]
    print matches
    for k in range(match_num):
        m = [int(line[k*2]), int(line[k*2+1])]
        m.sort()
        matches[m[0]].append(m[1])
    matched = [-1] * student_num
    print matched
    current_sum += check(0, matched, matches, student_num)
    print current_sum
"""""