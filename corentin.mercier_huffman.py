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

from AlgoPy.prettytree import *


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
## BUILD THE TREE

def buildHuffmanTree(inputList): # Working
    """
    Processes the frequency list into a Huffman tree according to the algorithm.
    This is the hat function
    """
    l=[]
    for i in inputList:
        T = BinTree(i,None,None)
        l.append(T)
    return _buildHuffmanTree(l,0)

def quickSort(L):
    """
    Reversed quickSort
    """
    less = []
    pivotList = []
    more = []
    if (L==[]):
        return L
    else:
        pivot = L[0].key[0]
        for i in L:
            if i.key[0] > pivot:
                more.append(i)
            elif i.key[0] < pivot:
                less.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return more + pivotList + less

def _buildHuffmanTree(L,x):
    """
    Processes the frequency list into a Huffman tree according to the algorithm.
    """
    if(len(L)<=1):
        return L[0]
    elif(L==[0]):
        return None
    L = quickSort(L)
    right = L.pop()
    left = L.pop()
    x += 1
    T = BinTree((right.key[0]+left.key[0],x),left,right)
    T.left.key = left.key[1]
    T.right.key = right.key[1]
    L.append(T)
    return _buildHuffmanTree(L, x)

################################################################################
## ENCODE DATA USING THE TREE

def encodeData(dataIN, huffmanTree): # Working
    """
    Encodes the input string to its binary string representation.
    """
    dic = codeDict(huffmanTree)
    string = ""
    for i in dataIN:
        for n in range(len(dic)):
            if i == dic[n][0]:
                string += dic[n][1]
    return string

def codeDict(tree):
    """
    Returns a list of tuples (letter,corresponding code)
    """
    l = []
    def dfsInfix(tree, string):
        '''
        Depth-first traversal
        Prints keys in inorder
        '''
        if tree != None:
            dfsInfix(tree.left, string + '0')
            if tree.left == None and tree.right == None:
              l.append((tree.key, string))
            dfsInfix(tree.right, string + '1')
    dfsInfix(tree, "")
    return l

################################################################################

def encodeTree(huffmanTree):
    """
    Encodes a huffman tree to its binary representation
    """
    pass

def predorder(tree, l = []):
    '''
    Depth-first traversal
    Prints keys in preorder
    '''
    if tree != None:
        if tree.left == None and tree.right == None:
            l.append(bin(tree.key))
        predorder(tree.left, l)
        predorder(tree.right, l)
    return l


def toBinary(dataIN):
    """
    Compresses a string containing binary code to its real binary value.
    """
    binary = ""
    for letter in dataIN:
        pass
    return ' '.join(format(ord(x), 'b') for x in dataIN)


def compress(dataIn):
    """
    The main function that makes the whole compression process.
    """
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

################################################################################
## TESTS

freq = buildFrequencyList("apple pie")
# print(freq)
tree = buildHuffmanTree(freq)
# print(tree)
# toSVG(tree, "tree")
code = codeDict(tree)
#print(code)
#
print(encodeData("apple pie", tree))
print(predorder(tree))
