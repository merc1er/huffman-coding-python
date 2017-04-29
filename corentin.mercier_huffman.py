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

def buildHuffmanTree(inputList): # Working
    """
    Processes the frequency list into a Huffman tree according to the algorithm.
    """
    inputList = _ListTupletoBinTree(inputList)
    return _buildHuffmanTree(inputList,0)

def quickSort(L):
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

def _ListTupletoBinTree(L):
    l=[]
    for i in L:
        T = BinTree(i,None,None)
        l.append(T)
    return l

def _buildHuffmanTree(L,x):
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

# freq = buildFrequencyList("apple pie")
# print(freq)
# tree = buildHuffmanTree(freq)
# print(tree)
# toSVG(tree, "tree")

################################################################################

def encodeData(dataIN, huffmanTree):
    """
    Encodes the input string to its binary string representation.
    """

    # FIXME
    pass

################################################################################

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
