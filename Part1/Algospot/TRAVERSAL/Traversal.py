# -*- coding: utf-8 -*-

###divide & conquer 문제인듯... ###
###하지만 재귀적으로 풀어야 될듯 input 최대치가 100개###

__author__ = 'markers'

import sys
rl = lambda: sys.stdin.readline()

class Node():
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
	def get_value(self):
		return self.value

	def insert_left(self, node):
		self.left = node

	def insert_right(self, node):
		self.right = node

def preorder(node):
	if node is not None:
		print node.value
		preorder(node.left)
		preorder(node.right)
		
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print node.value,
	

#def make_tree(preoder_node, inorder_node, order):
#	value = preorder_node[order]
#	print value
#	node = Node(value)
#	separate_index = 0
#	for index, inorder_value in enumerate(inorder_node):
#		if value == inorder_value:
#			separate_index = index
#			break
#	print separate_index
		
def make_tree(preorder_list, inorder_list):
    node = None
    if preorder_list and inorder_list:
        value = preorder_list[0]
        #print value
        #node = Node(value)
        separate_index = 0
        for index, inorder_value in enumerate(inorder_list):
            if value == inorder_value:
                separate_index = index
                break
        #print separate_index
        #print inorder_list[separate_index]
        node = Node(inorder_list[separate_index])
        # 왼쪽 노드방향
        node.insert_left(make_tree(preorder_list[1:], inorder_list[0:separate_index] ) )
        # 오른쪽 노드방향
        node.insert_right(make_tree(preorder_list[separate_index+1:], inorder_list[separate_index+1:] ) )

    return node

	
if __name__ == "__main__":
    testcase =  int(rl())
    for tc in range(testcase):
        nodes_number = rl().strip()
        preorder_node = rl().strip().split()
        inorder_node = rl().strip().split()
        #print preorder_node
        node = make_tree(preorder_node, inorder_node)
        postorder(node)
        print
        




#root = Node(12)
#second = Node(13)
#root.insert_left(second)
#print preorder(root)
