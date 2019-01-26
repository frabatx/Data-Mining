'''
    File name: dataset.py
    Author: Battista Francesco, Merzi Nicolò
    Python Version: 3.5
'''

import random
import csv
from random import shuffle
from Binary_Tree import BinaryTree


def records2(tree, t_id, r_id, aList):
    r_id = r_id + 1
    if tree.left != None:
        #print output to screen
        print(str(r_id) + ';' + str(t_id) + ';' +tree.data + tree.left.data)
        #save output in a list
        aList.append([r_id,t_id,tree.data + tree.left.data])
        r_id = records2(tree.left, t_id, r_id, aList)
    if tree.right != None:
        #print output to screen
        print(str(r_id) + ';' + str(t_id) + ';' +tree.data + tree.right.data)
        #save output in a list
        aList.append([r_id,t_id,tree.data + tree.right.data])
        r_id = records2(tree.right, t_id, r_id, aList)
    return r_id


#create tree from list of actions
r_id = 0
datasetList = [[]]
for i in range(1,1001):
    actions = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    shuffle(actions)
    tree = BinaryTree(actions[0])
    del actions[0]
    for j in actions:
        tree.insertTraversal(j)
    r_id = records2(tree, i, r_id, datasetList)


#write list to csv file
#with open('dataset1k.csv', 'w') as csvfile:
#    csvwriter = csv.writer(csvfile)
#    for row in datasetList:
#        csvwriter.writerow(row)

'''
-------------OUTPUT-------------
(r_id;t_id;action)
1;1;FI
2;1;IA
3;1;AH
4;1;IB
5;1;BE
6;1;FG
7;1;GD
8;1;GC
10;2;IH
11;2;HD
12;2;DA
13;2;AE
14;2;DC
15;2;CB
16;2;HG
17;2;GF
19;3;IG
20;3;GD
21;3;DH
22;3;HA
23;3;IF
24;3;FB
25;3;FE
26;3;EC
'''
