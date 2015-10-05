# -*- coding: utf-8 -*-

###문제의 힌트는 뒤로 인덱스 검색 ###


__author__ = 'markers'

import sys
rl = lambda: sys.stdin.readline()


def seperator(string_list):
	return [ string_list[ x : x+1 ] for x in range(0, len(string_list) ) ]	

def judge_level(piece_list):
	### piece_list is like [1, 2, 3] 
	sum = 0
	piece_list = map(int, seperator(piece_list))
	## level 1
	#if piece[1:] == piece[:-1]:
	if len(piece_list) == 0:
		return 0
	if len(piece_list) < 3:
		return 1000000
	#print 'piece ', piece_list

	if all( x == piece_list[0] for x in piece_list ):
		#print 'level 1'
		sum += 1
	## level 2
	elif all( x-y == 1 for x, y in zip( piece_list, piece_list[1:] ) ) or all( x-y == -1 for x, y in zip( piece_list, piece_list[1:] )):
		#print 'level 2'
		sum += 2 
	## level 3
	elif ( piece_list[0:] != piece_list[1:] ) and all( x == piece_list[0] for x in piece_list[::2] ) and all( x == piece_list[1] for x in piece_list[1::2]):
		#print 'level 3'
		sum += 4
	## level 4
	elif all( x-y == y-z for x, y, z in zip( piece_list, piece_list[1:], piece_list[2:] ) ):
		#print 'level 4'
		sum += 5
	## level 5
	else:
		#print 'level 5'
		sum += 10
	#print sum
	return sum

def decode(piece_list):

	



	#piece_list = seperator(string_list)
	#return judge_level(piece_list)
	length = len(piece_list) 
	#print 'piece_list is ', piece_list
	if length > 4:
		return min( judge_level(piece_list[length-3:]) + decode( piece_list[:length-3] ), \
				judge_level(piece_list[length-4:] ) + decode( piece_list[:length-4] ) , \
				judge_level(piece_list[length-5:] ) + decode( piece_list[:length-5] )  )
	elif length > 3:
		return min( judge_level(piece_list[length-3:]) + decode( piece_list[:length-3] ), \
				judge_level(piece_list[length-4:] ) + decode( piece_list[:length-4] ) )
	elif length > 2:
		return judge_level(piece_list[length-3:]) + decode( piece_list[:length-3] ) 
	else:
		#print 'last element ', piece_list
		return 0 



if __name__ == "__main__":
	testcase =  int(rl())
	string_list = [] 
	for tc in range(testcase):
		string_list = rl().strip()
		print decode(string_list)

