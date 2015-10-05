# -*- coding: utf-8 -*-

# 삽입 정렬을 써야 하는걸까???

__author__ = 'markers'

import sys
rl = lambda: sys.stdin.readline()

def find_array(length, move_array):
	list_of_number = [ x for x in xrange(length,0,-1) ] 
#	print "list_of_number ", list_of_number
	move_array.reverse()
#	print "move_array ", move_array
	
	for index, val in enumerate(move_array):
		list_of_number.insert(len(list_of_number)-1-index, list_of_number.pop(int(val)))   
	print ' '.join(map(str,list_of_number))	


if __name__ == "__main__":
	testcase =  int(rl())
	for tc in range(testcase):
		array_length = int(rl())
		move_array = rl().split()
		find_array(array_length, move_array)

