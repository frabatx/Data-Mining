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
datasetList = []
for i in range(1,1001):
    actions = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    shuffle(actions)
    tree = BinaryTree(actions[0])
    del actions[0]
    for j in actions:
        tree.insertTraversal(j)
    r_id = records2(tree, i, r_id, datasetList)
    r_id = r_id - 1

#write list to csv file
with open('dataset1k.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in datasetList:
        csvwriter.writerow(row)

'''
-------------OUTPUT-------------
(r_id;t_id;action)
1;1;AB
2;1;BI
3;1;IF
4;1;ID
5;1;DH
6;1;BE
7;1;EC
8;1;CG
9;2;GI
10;2;IC
11;2;IF
12;2;GH
13;2;HE
14;2;HD
15;2;DB
16;2;DA
17;3;DF
18;3;FA
19;3;FE
20;3;EH
21;3;HG
22;3;DB
23;3;BI
24;3;BC
'''
