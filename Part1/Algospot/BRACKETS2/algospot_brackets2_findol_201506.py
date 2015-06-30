pairs = {
		"(": ")",
		"[": "]",
		"{": "}"
	}
open_brackets = pairs.keys()

def validate(brackets):
	stack = []	
	for bracket in brackets:
		if bracket in open_brackets:
			stack.append(bracket)
		else:
			if stack:
				if pairs[stack.pop()] != bracket:
					return False
			else:
				return False
	return len(stack) == 0


import sys
rl = lambda: sys.stdin.readline()
n = int(rl())
for _ in xrange(n):
	brackets = rl().strip()
	if validate(brackets):
		print 'YES'
	else:
		print 'NO'
