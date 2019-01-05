'''
    File name: Binary_Tree.py
    Author: Battista Francesco, Nicolò Merz
    Date created: 03/01/2019
    Date last modified: 03/01/2019
    Python Version: 3.5
'''

"""
Each BinaryTree instance may have a left BinaryTree instance and may have a right BinaryTree instance,
while absence of a branch is marked with None. This reflects the recursive nature of trees.
"""
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

    """
    Takes as input data and modifies current node this way:
    - First creates a new BinaryTree into which provided data is wrapped.
    - Then:
        - if there is no left node in self, new node B is attached to the left of self
        - if there already is a left node L, it is substituted by new node B, and L becomes the
          left node of B

    We can also attach only the left node without conditions self.left = B
    """
    def insert_left(self, data):
        B =  BinaryTree(data)
        if self.left == None:
            self.left = B
            B.parent = self
        else:
            B.left = self.left
            B.parent = self
            #self.parent = B
            self.left = B

    """
    Takes as input data and modifies current node this way:
    - First creates a new BinaryTree into which provided data is wrapped.
    - Then:
        - if there is no right node in self, new node B is attached to the right of self
        - if there already is a right node R, it is substituted by new node B, and R becomes the
          right node of B

    We can also attach only the right node without conditions self.right = B
    """
    def insert_right(self, data):
        B = BinaryTree(data)
        if self.right == None:
            self.right = B
        else:
            B.right = self.right
            self.right = B

    def insert(self, node):
        if random.random() <= 0.5:
            if self.left == None:
                self.left = node
                print('insert [' + node.data + '] left of [' + self.data + ']' )
            else:
                oldLeft = self.left
                node.insert(oldLeft)
                self.left = node
                print('pushing down [' + oldLeft.data + '] left of [' + node.data + ']', )
        else:
            if self.right == None:
                self.right = node
                print('insert [' + node.data + '] right of [' + self.data + ']' )
            else:
                oldRight = self.right
                node.insert(oldRight)
                self.right = node
                print('pushing down [' + oldRight.data + '] right of [' + node.data + ']', )
        node.parent = self
        print('attaching parent [' + self.data + '] to [' + node.data + ']')

    def records(self):
        if self.left != None:
            print(self.data, self.left.data)
            self.left.records()
        if self.right != None:
            print(self.data, self.right.data)
            self.right.records()

    """
    RETURN an integer which is the height of the tree
    - implement it as recursive call which does NOT modify the tree
      NOTE: with big trees a recursive solution would surely exceed the call stack,
            but here we don't mind
    - A tree with only one node has height zero.

    """
    def height_rec(self):
        if self.get_left() == None:
            h_left = 0
        else:
            h_left = self.get_left().height_rec() + 1

        if self.get_right() == None:
            h_right = 0
        else:
            h_right = self.get_right().height_rec() + 1

        return max(h_left, h_right)

    """
    TO DO
    - has_children()
    - ancestors() Return a list of parents
    - sibling()
    - clone()

    """


actions = ['A', 'B', 'C', 'D', 'E', 'F']

from random import shuffle
import random

shuffle(actions)
print(actions, "\n")

tree = BinaryTree(actions[0])
del actions[0]

for i in actions:
    node = BinaryTree(i)
    print("new node: ", node.data)
    tree.insert(node)

print(tree)
tree.records()
