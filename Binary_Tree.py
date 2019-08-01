# - * - coding: utf-8 - * - 
"""Binary Tree
This module creates simple binary trees.
"""
import random
from random import shuffle

class BinaryTree:
    """Class Bynary tree
        Methods:
            * get_data()
            * get_parent()
            * get_left()
            * get_right()
            * insertTraversal(self, value)
            * __insertTraversalLeft(self, value) ** Private method
            * __insertTraversalRight(self, value) ** Private method
            * records(self)
    """
    #INITIALIZER
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    #GETTER
    def get_data(self):
        return self.data

    def get_parent(self):
        return self.parent

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    #METHODS
    def __str__(self):
        """Overriding string method
        """
        def str_branches(node, branches):
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
                        branches.append('|')
                    else:
                        branches.append(' ')

                    if current != None:
                        strings.append(str_branches(current, branches))
                    branches.pop()
                    i += 1
            return "".join(strings)

        return str_branches(self, [])

    def insertTraversal(self, value):
        """Taking a value, less than 0.5 insert the value on left, otherwise on right
        
        Arguments:
            value {[int]} -- [Value inside the node]
        """
        if random.random() <= 0.5:
            self.__insertTraversalLeft(value)
        else: 
            self.__insertTraversalRight(value)

    def __insertTraversalLeft(self, value):
        """Taking a value and insert it on the left branch 
        
        Arguments:
            value {[int]} -- [Value inside the node]
        """
        if self.left != None:
            #print('node found. Going down...')
            self.left.insertTraversal(value)
        else:
            #print('free edge found. Inserting node.')
            newNode = BinaryTree(value)
            self.left = newNode
            newNode.parent = self

    def __insertTraversalRight(self, value):
        """Taking a value and insert it on the right branch 
        
        Arguments:
            value {[int]} -- [Value inside the node]
        """
        if self.right != None:
            #print('node found. Going down...')
            self.right.insertTraversal(value)
        else:
            #print('free edge found. Inserting node.')
            newNode = BinaryTree(value)
            self.right = newNode
            newNode.parent = self

    def insertBottom(self, value):
        """Taking a value and insert it after the last leaf
        
        Arguments:
            value {[int]} -- [Value inside the node]
        """
        if(self.left != None):
            self.left.insertBottom(value)
        if(self.right != None):
            self.right.insertBottom(value)
        if(self.right == None and self.left == None):
            newNode = BinaryTree(value)
            if random.random() > 0.5:
                self.right = newNode
                newNode.parent = self
            else:
                self.left = newNode
                newNode.parent = self

        
    


'''
actions = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

shuffle(actions) #si mischiano i nodi
print(actions, "\n")

tree = BinaryTree(actions[0]) #si setta il nodo principale
del actions[0] #si cancella dalla lista

for i in actions: #per ogni nodo
    print("inserting new value: ", i)
    tree.insertTraversal(i) #inseriamolo nell'albero

print(tree)
tree.records()
'''


'''
-------------OUTPUT-------------

['G', 'I', 'C', 'F', 'D', 'A', 'B', 'E', 'H']

inserting new value:  I
free edge found. Inserting node.
inserting new value:  C
node found. Going down...
free edge found. Inserting node.
inserting new value:  F
free edge found. Inserting node.
inserting new value:  D
node found. Going down...
free edge found. Inserting node.
inserting new value:  A
node found. Going down...
free edge found. Inserting node.
inserting new value:  B
node found. Going down...
node found. Going down...
free edge found. Inserting node.
inserting new value:  E
node found. Going down...
node found. Going down...
free edge found. Inserting node.
inserting new value:  H
node found. Going down...
node found. Going down...
node found. Going down...
free edge found. Inserting node.

tree pretty printed:
G
├F
│├A
││├
││└E
││ ├H
││ └
│└D
└I
 ├C
 │├B
 │└
 └

tree in record form:
G F
F A
A E
E H
F D
G I
I C
C B
'''