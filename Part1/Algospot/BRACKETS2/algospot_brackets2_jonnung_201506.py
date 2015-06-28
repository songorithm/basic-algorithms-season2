# -*- coding: utf8 -*-
# author: Eunwoo Cho <jonnung@gmail.com>

def validate_bracket(brackets):
    brackets_mapping = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    stack = []
    for c in brackets:
        if c in '({[':
            stack.append(brackets_mapping[c])
        else:
            if not stack:
                return False

            if c != stack.pop():
                return False
    if stack:
        return False
    return True

if __name__ == '__main__':
    test_num = int(raw_input())
    for tc in range(test_num):
        if validate_bracket(raw_input()):
            print("YES")
        else:
            print("NO")
