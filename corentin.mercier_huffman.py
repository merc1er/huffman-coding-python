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

def encodeData(dataIN, huffmanTree): # Not working
    """
    Encodes the input string to its binary string representation.
    """
    pass

def codeDict(tree, l = [], code = ""):
    """
    Returns a list of tuples (letter,corresponding code)
    """
    if tree != None:
        _tree = tree
        if tree.left != None:
            code += "0"
            codeDict(tree.left, l, code)
        elif tree.right != None:
            code += "1"
            codeDict(tree.right, l, code)
        else:
            l.append((tree.key, code))
        code += "1"
        return codeDict(_tree.right, l, code)
    return l

def _MappingTable (B):
  l=[]
  def dfsPrefix(B, s):
      if B != None:
          if B.left == None and B.right == None:
            l.append((B.key[0], s))
          dfsPrefix(B.left, s+'0')
          dfsPrefix(B.right, s+'1')
  ms = ''
  dfsPrefix(B, ms)
  return l

################################################################################

def encodeTree(huffmanTree):
    """
    Encodes a huffman tree to its binary representation
    """
    pass


def toBinary(dataIN):
    """
    Compresses a string containing binary code to its real binary value.
    """
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

################################################################################
## TESTS

#
#
#
# def encodeData(dataIN, huffmanTree):
#   MT = _MappingTable(huffmanTree)
#
#   MessInBinHuff = ""
#   for i in dataIN:
#     for n in range (len(MT)):
#       if i == MT[n][0]:
#         MessInBinHuff + MT[n][1]
#   return MessInBinHuff

freq = buildFrequencyList("apple pie")
# print(freq)
tree = buildHuffmanTree(freq)
# print(tree)
# toSVG(tree, "tree")
code = codeDict(tree)
code2 = _MappingTable(tree)
print("Gael")
print(code2)
print("Corentin")
print(code)
