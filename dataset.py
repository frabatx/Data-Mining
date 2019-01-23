import random
from random import shuffle
from Binary_Tree import BinaryTree


def records2(tree, t_id, r_id):
    r_id = r_id + 1
    if tree.left != None:
        print(str(r_id) + ';' + str(t_id) + ';' +tree.data + tree.left.data)
        r_id = records2(tree.left, t_id, r_id)
    if tree.right != None:
        print(str(r_id) + ';' + str(t_id) + ';' +tree.data + tree.right.data)
        r_id = records2(tree.right, t_id, r_id)
    return r_id


r_id = 0
for i in range(1,20):
    actions = ['A', 'B', 'C', 'D', 'E', 'F']
    shuffle(actions)
    tree = BinaryTree(actions[0])
    del actions[0]
    for j in actions:
        tree.insertTraversal(j)
    r_id = records2(tree, i, r_id)



#-------------OUTPUT-------------
#(r_id;t_id;action)
#(1;1;EF)
#(2;1;FB)
#(3;1;EC)
#(4;1;CA)
#(5;1;AD)
#(6;2;AC)
#(7;2;CE)
#(8;2;ED)
#(9;2;CF)
#(10;2;FB)

