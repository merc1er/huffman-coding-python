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

def buildHuffmanTree(inputList):
    """
    Processes the frequency list into a Huffman tree according to the algorithm.
    """
    heap = newHeap()
    for i in range(len(inputList)):
        heapPush(heap, inputList[i])
        # puts the inputList in a heap

    tree = BinTree(None, None, None)
    if len(inputList) == 1: # if there is only one character in the string given
        tree.key = heapPop(heap)[1]
        return tree

    min1 = BinTree(heapPop(heap)[0], None, None)
    for i in range(len(inputList) // 2):
        min2 = heapPop(heap)
        tree.key = min1.key + min2[0]
        tree.right = min2
        tree.left = min1
        min1 = tree

    return tree

from AlgoPy.heap import *
from AlgoPy.binTree import *

# tests
string = "apple pie"
freq = buildFrequencyList(string)
print("frequence table:")
print(freq)
tree = buildHuffmanTree(freq)
print("tree:")
print(tree)
print("tree.key")
print(tree.key)
print("left")
print(tree.left)
print("right")
print(tree.right)
print("left left")
print(tree.left.left)
print("left right")
print(tree.left.right)
print(tree.left.key)

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
