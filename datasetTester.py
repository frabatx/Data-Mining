import random
import copy
from random import shuffle, randint
from Binary_Tree import BinaryTree

def createList():
    firstNum = randint(1,10)
    secNum = randint(1,10)
    thirdNum = randint(1,10)
    return [firstNum,secNum, thirdNum]

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





'''
r_id = 0
datasetList = []

#sequence X --> Y --> Z
for i in range(1,4): 
    tree = BinaryTree(['X',randint(1,10)])
    tree.left = BinaryTree(['Y',randint(1,10)])
    tree.left.left = BinaryTree([randint(1,10),'Z'])
    #insert random nodes in the sequence
    for j in range(1,4):
        tree.insertTraversal(createList())
    r_id = records2(tree, i, r_id, datasetList)
    r_id = r_id - 1

#for f in datasetList:
#    print(f)
'''
'''
#Create sequence
seq1 = createSequence()
print("Sequence created: ", seq1)

#Fill sequence with noise untile each list has 3 element
seqFiller(seq1)
print("Sequence filled: ", seq1)


tree = seqTreeBuilder(seq1)
addNodesTree(tree)

print(tree)
'''


#creates 5 trees with same seq inside
seq = createSequence()
print("Sequence created: ", seq)
for i in range(1,5):
    print("TREE: ", i)
    print("seq: ", seq)
    seqfilled = seqFiller(seq) #add noise to the sequence (original sequence doesnt change)
    print("Sequence filled: ", seqfilled)
    print("")
    tree = seqTreeBuilder(seqfilled)
    addNodesTree(tree)
    print(tree)



