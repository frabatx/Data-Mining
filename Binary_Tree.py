import random
from random import shuffle

class BinaryTree:
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

    #Taking a value, less than 0.5 insert the value on left, otherwise on right
    def insertTraversal(self, value):
        if random.random() <= 0.5:
            self.__insertTraversalLeft(value)
        else: 
            self.__insertTraversalRight(value)

    #Private method
    #Taking a value and insert it on the left branch
    def __insertTraversalLeft(self, value):
        if self.left != None:
            #print('node found. Going down...')
            self.left.insertTraversal(value)
        else:
            #print('free edge found. Inserting node.')
            newNode = BinaryTree(value)
            self.left = newNode
            newNode.parent = self

    #Private method
    #Taking a value and insert it on the right branch
    def __insertTraversalRight(self, value):
        if self.right != None:
            #print('node found. Going down...')
            self.right.insertTraversal(value)
        else:
            #print('free edge found. Inserting node.')
            newNode = BinaryTree(value)
            self.right = newNode
            newNode.parent = self

    #Records
    #output tree in record format
    def records(self):
        if self.left != None:
            print(self.data, self.left.data)
            self.left.records()
        if self.right != None:
            print(self.data, self.right.data)
            self.right.records()

    #Overriding string method
    def __str__(self):
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
                        branches.append('│')
                    else:
                        branches.append(' ')

                    if current != None:
                        strings.append(str_branches(current, branches))
                    branches.pop()
                    i += 1
            return "".join(strings)

        return str_branches(self, [])


'''
actions = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

shuffle(actions)
print(actions, "\n")

tree = BinaryTree(actions[0])
del actions[0]

for i in actions:
    print("inserting new value: ", i)
    tree.insertTraversal(i)

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