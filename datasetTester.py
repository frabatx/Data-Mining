import random
import copy
import csv
from random import shuffle, randint
from Binary_Tree import BinaryTree

def createList():
    firstNum = randint(1,10)
    secNum = randint(1,10)
    thirdNum = randint(1,10)
    return [firstNum,secNum,thirdNum]

def records2(tree, t_id, r_id, aList):
    r_id = r_id + 1
    if tree.left != None:
        #print output to screen
        print(str(r_id) + ';' + str(t_id) + ';' , tree.data , tree.left.data)
        #save output in a list
        aList.append([r_id,t_id,tree.data, tree.left.data])
        r_id = records2(tree.left, t_id, r_id, aList)
    if tree.right != None:
        #print output to screen
        print(str(r_id) + ';' + str(t_id) + ';' , tree.data , tree.right.data)
        #save output in a list
        aList.append([r_id,t_id,tree.data, tree.right.data])
        r_id = records2(tree.right, t_id, r_id, aList)
    return r_id

#1 or 2 elements
#[[4],[7],[1]]
#[[1,8],[5],[3,9]]
#[[4],[5,6],[8]]
def createSequence():
    aSeq = []
    for i in range(1,4):
        if random.random() < 0.5:
            aSeq.append([randint(0,9)])
        else:
            aSeq.append([randint(0,9), randint(0,9)])
    return aSeq

def seqFiller(seq):
    seqfilled = copy.deepcopy(seq) #deep copy original list and modify only the copy
    for i in seqfilled:
        while len(i) < 3:
            i.append(randint(1,10))
    return seqfilled #return copy list - original list "seq" untouched

def seqTreeBuilder(aSeq):
    tree = BinaryTree(aSeq[0])
    randNum = randint(1,4)
    if randNum == 1:
        tree.left = BinaryTree(aSeq[1])
        tree.left.left = BinaryTree(aSeq[2])
    if randNum == 2: 
        tree.left = BinaryTree(aSeq[1])
        tree.left.right = BinaryTree(aSeq[2])
    if randNum == 3:
        tree.right = BinaryTree(aSeq[1])
        tree.right.right = BinaryTree(aSeq[2])
    if randNum == 4:
        tree.right = BinaryTree(aSeq[1])
        tree.right.left = BinaryTree(aSeq[2])
    return tree

def addNodesTree(tree): #insert 4 random nodes
    for i in range(1,5):
        aList = createList()
        tree.insertTraversal(aList)



seq = createSequence() #create starting sequence
print("\n Sequence created: ", seq)
seqfilled = seqFiller(seq) #add noise to the sequence (original sequence doesnt change)
print("\n Sequence filled: ", seqfilled, "\n")
tree = seqTreeBuilder(seqfilled) #populate tree with the sequence
addNodesTree(tree) #add random nodes to the tree
print(tree)

print("\n")

r_id = 0
treeList = []

seq1 = createSequence()
print("\n Seq1: ", seq1, "\n")
for i in range(1, 5):
    seqfilled = seqFiller(seq1)
    tree = seqTreeBuilder(seqfilled)
    addNodesTree(tree)
    r_id = records2(tree, i, r_id, treeList)
    r_id = r_id - 1


seq2 = createSequence()
print("\n Seq2: ", seq2, "\n")
for i in range(5, 10):
    seqfilled = seqFiller(seq2)
    tree = seqTreeBuilder(seqfilled)
    addNodesTree(tree)
    r_id = records2(tree, i, r_id, treeList)
    r_id = r_id - 1

seq3 = createSequence()
print("\n Seq3: ", seq3, "\n")
for i in range(10, 15):
    seqfilled = seqFiller(seq3)
    tree = seqTreeBuilder(seqfilled)
    addNodesTree(tree)
    r_id = records2(tree, i, r_id, treeList)
    r_id = r_id - 1



#write list to csv file
with open('datasetTest.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in treeList:
        csvwriter.writerow(row)

