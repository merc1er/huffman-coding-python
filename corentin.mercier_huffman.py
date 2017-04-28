__license__ = 'GolluM & Junior (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: huffman.py 2017-04-04'

"""
Huffman homework
2017
@author: corentin.mercier
"""


##################################################
# Warning:
# This file has been cleared from long doctrings
# See the complete specifications online.


# from AlgoPy import binTree
# from AlgoPy import heap
from AlgoPy.heap import *
from AlgoPy.binTree import *
import os
import pygraphviz


def toDot(BTree):
        dot_string = "graph {\n" + 'graph [ordering="out"]\n'
        BST_q = deque()
        if BTree:
            BST_q.append(BTree)
        while not len(BST_q) == 0:
            BTree = BST_q.pop()
            if BTree.left:
                dot_string += "   \"" + str(BTree.key) + "\" -- \"" + str(BTree.left.key) + "\"\n"
                BST_q.append(BTree.left)
            if BTree.right:
                dot_string += "   \"" + str(BTree.key) + "\" -- \"" + str(BTree.right.key) + "\"\n"
                BST_q.append(BTree.right)
        dot_string += "}"
        return dot_string

def toSVG(B, name):
    if B:
        graph = AGraph(toDot(B))
        layout = graph.layout(prog="dot")
        draw = graph.draw("{}.svg".format(name))
        system("display {}.svg".format(name))
    else:
        print("Give me a better tree")


################################################################################
## COMPRESSION

def buildFrequencyList(dataIN): # Working
    """
    Builds a tuple list of the character frequencies in the input.
    """
    table = []
    _table = []
    for letter in dataIN:
        if letter not in _table:
            _table.append(letter)
            count = 0
            for i in range(len(dataIN)):
                if dataIN[i] == letter:
                    count += 1
            table.append((count, letter))
    return table

################################################################################

# def buildHuffmanTree(inputList):
#     """
#     Processes the frequency list into a Huffman tree according to the algorithm.
#     """
#     heap = newHeap()
#     for i in range(len(inputList)):
#         heapPush(heap, inputList[i])
#         # puts the inputList in a heap
#
#     tree = BinTree(None, None, None)
#     if len(inputList) == 1: # if there is only one character in the string given
#         tree.key = heapPop(heap)[1]
#         return tree
#
#     min1 = BinTree(heapPop(heap)[0], None, None)
#     for i in range(len(inputList) // 2):
#         min2 = heapPop(heap)
#         tree.key = min1.key + min2[0]
#         tree.right = min2
#         tree.left = min1
#         min1 = tree
#
#     return tree

def _quickSort(L):
    less = []
    pivotList = []
    more = []
    if (L==[]):
        return L
    else:
        pivot = L[0].key[0]
        for i in L:
            print(i.key[0])
            if i.key[0] > pivot:
                more.append(i)
            elif i.key[0] < pivot:
                less.append(i)
            else:
                pivotList.append(i)
        less = _quickSort(less)
        more = _quickSort(more)
        return more + pivotList + less

def _ListTupletoBinTree(L):
    l=[]
    for i in L:
        T = BinTree(i,None,None)
        l.append(T)
    return l

def _buildHuffmanTree(inputList):
    if(len(inputList)==1):
        return inputList[0]
    elif(inputList==[]):
        return None
    L=_quickSort(inputList)
    right = L.pop()
    left = L.pop()
    T = BinTree((right.key[0]+left.key[0],'.'),left,right)
    T.left.key = left.key[1]
    T.right.key = right.key[1]
    #toSVG(T, "mytree.svg")
    L.append(T)
    _buildHuffmanTree(L)

def buildHuffmanTree(inputList):
    """
    Processes the frequency list into a Huffman tree according to the algorithm.
    """
    inputList = _ListTupletoBinTree(inputList)
    return _buildHuffmanTree(inputList)


freq = buildFrequencyList("apple pie")
print(freq)
tree = buildHuffmanTree(freq)
print(tree)
toSVG(tree, "tree.svg")

################################################################################

def encodeData(dataIN, huffmanTree):
    """
    Encodes the input string to its binary string representation.
    """

    # FIXME
    pass


def encodeTree(huffmanTree):
    """
    Encodes a huffman tree to its binary representation
    """

    # FIXME
    pass


def toBinary(dataIN):
    """
    Compresses a string containing binary code to its real binary value.
    """

    # FIXME
    pass


def compress(dataIn):
    """
    The main function that makes the whole compression process.
    """

    # FIXME
    pass


################################################################################
## DECOMPRESSION

def decodeData(dataIN, huffmanTree):
    """
    Decode a string using the corresponding huffman tree into something more readable.
    """

    # FIXME
    pass


def decodeTree(dataIN):
    """
    Decodes a huffman tree from its binary representation
    """

    # FIXME
    pass


def fromBinary(dataIN, align):
    """
    Retrieve a string containing binary code from its real binary value (inverse of :func:`toBinary`).
    """

    # FIXME
    pass


def decompress(data, dataAlign, tree, treeAlign):
    """
    The whole decompression process.
    """

    # FIXME
    pass
