'''
    File name: Binary_Tree.py
    Author: Battista Francesco, Merzi Nicolò
    Date created: 03/01/2019
    Python Version: 3.5
'''

import random
from random import shuffle

class BinaryTree:
    """INITIALIZER"""
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    """GETTER"""
    def get_data(self):
        return self.data

    def get_parent(self):
        return self.parent

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    """ Returns a string of the tree """
    def __str__(self):
        def str_branches(node, branches):
            """ Returns a string with the tree pretty printed.

                branches: a list of characters representing the parent branches.
                Characters can be either ` ` or '│'
            """
            strings = [str(node.data)]

            i = 0
            if node.left != None or node.right != None:
                for current in [node.left, node.right]:
                    if i == 0:
                        joint = '├'
                    else:
                        joint = '└'

                    strings.append('\n')
                    for b in branches:
                        strings.append(b)
                    strings.append(joint)
                    if i == 0:
                        branches.append('│')
                    else:
                        branches.append(' ')

                    if current != None:
                        strings.append(str_branches(current, branches))
                    branches.pop()
                    i += 1
            return "".join(strings)

        return str_branches(self, [])

    def insertTraversal(self, value):
        if random.random() <= 0.5:
            self.insertTraversalLeft(value)
        else: 
            self.insertTraversalRight(value)

    def insertTraversalLeft(self, value):
        if self.left != None:
            #print('node found. Going down...')
            self.left.insertTraversal(value)
        else:
            #print('free edge found. Inserting node.')
            newNode = BinaryTree(value)
            self.left = newNode
            newNode.parent = self

    def insertTraversalRight(self, value):
        if self.right != None:
            #print('node found. Going down...')
            self.right.insertTraversal(value)
        else:
            #print('free edge found. Inserting node.')
            newNode = BinaryTree(value)
            self.right = newNode
            newNode.parent = self
   
    def records(self):
        if self.left != None:
            print(self.data, self.left.data)
            self.left.records()
        if self.right != None:
            print(self.data, self.right.data)
            self.right.records()



#actions = ['A', 'B', 'C', 'D', 'E', 'F']

#shuffle(actions)
#print(actions, "\n")

#tree = BinaryTree(actions[0])
#del actions[0]

#for i in actions:
#    print("inserting new value: ", i)
#    tree.insertTraversal(i)

#print(tree)
#tree.records()


#-------------OUTPUT-------------
#['F', 'A', 'E', 'C', 'B', 'D']

#inserting new value:  A
#free edge found. Inserting node.
#inserting new value:  E
#node found. Going down...
#free edge found. Inserting node.
#inserting new value:  C
#node found. Going down...
#free edge found. Inserting node.
#inserting new value:  B
#free edge found. Inserting node.
#inserting new value:  D
#node found. Going down...
#node found. Going down...
#free edge found. Inserting node.
#F
#├B
#└A
# ├E
# │├
# │└D
# └C
#F B
#F A
#A E
#E D
#A C