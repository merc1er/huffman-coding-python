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
    tree = _buildHuffmanTree(l,0)
    tree.key = ""
    return tree

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

def encodeTree(huffmanTree): # Working
    """
    Encodes a huffman tree to its binary representation
    """
    dic = codeDict(huffmanTree)
    code = ""
    for item in dic:
        code = code + remove1(item[1]) + "1" + letterToBin(item[0])
    return code

def remove1(string):
    """
    Removes all the 1s from a given string, but not just that ;)
    """
    string = str(string)
    ret = ""
    for x in string:
        if x == "1":
            ret = ""
        else:
            ret += "0"
    return ret

def letterToBin(letter):
    """
    Converts a letter into its binary representation
    """
    i = ord(letter)
    if i == 0:
        return "0"
    string = ""
    while i != 0:
        string = str(i % 2) + string
        i = i // 2
    if len(string) == 7:
        string = "0" + string
    return string

################################################################################

def toBinary(dataIN): # Working
    """
    Compresses a string containing binary code to its real binary value.
    """
    s = ""
    count = 0
    i = 0
    length = len(dataIN)
    while  count  < length:
    	mult = 1
    	number = 0
    	if count + 7 < length:
    		i = count + 7
    		while i>=count:
    			number = number + int(dataIN[i]) * mult
    			i = i - 1
    			mult = mult * 2
    	else:
    		i = length - 1
    		while i >= count:
    			number = number + int(dataIN[i]) * mult
    			i = i - 1
    			mult = mult * 2
    	s = s + chr(number)
    	count = count + 8
    return (s, count - length)

################################################################################

def compress(dataIn):
    """
    The main function that makes the whole compression process.
    """
    freq = buildFrequencyList(dataIn)
    tree = buildHuffmanTree(freq)
    encodedData = encodeData(string, tree)
    encodedTree = encodeTree(tree)
    return (toBinary(encodedData), toBinary(encodedTree))


################################################################################
## DECOMPRESSION

def decodeData(dataIN, huffmanTree): # Working
    """
    Decode a string using the corresponding huffman tree into something more readable.
    """
    code = codeDict(huffmanTree)
    part = ""
    ret = ""
    for thing in dataIN:
        part += thing
        for item in code:
            if part == item[1]:
                ret += item[0]
                part = ""
    return ret

################################################################################

def decodeTree(dataIN):
    """
    Decodes a huffman tree from its binary representation
    """
    # FIXME
    pass

################################################################################

def fromBinary(dataIN, align):
    """
    Retrieve a string containing binary code from its real binary value (inverse of :func:`toBinary`).
    """
    ret = ""
    for i in range(len(dataIN)):
        # if i == len(dataIN) - 1:
        #     pass
        # else:
        _bin = letterToBin(dataIN[i])
        ret += _bin
    return ret

def decompress(data, dataAlign, tree, treeAlign):
    """
    The whole decompression process.
    """
    pass

################################################################################
## TESTS


print("#####################")
print("")
string = input(" Please enter a string: ")
print("this is your string: " + bcolors.WARNING + string)

print(bcolors.RESET)
freq = buildFrequencyList(string)
print("frequency list:")
print(freq)
print("")

tree = buildHuffmanTree(freq)
toSVG(tree, "tree")

print()
print("This is the codeDict")
code = codeDict(tree)
print(code)

print()
print("EncodeData returns:")
encodedData = encodeData(string, tree)
print(encodedData)

print()
print("encodeTree returns:")
print(encodeTree(tree))

print()
print("Compress returns:" + bcolors.WARNING)
compressed = compress(string)
print(compressed)

print(bcolors.RESET)
print("decodeData returns:")
decoded = decodeData(encodedData, tree)
print(decoded)

print()
print("fromBinary returns" + bcolors.WARNING)
fromb = fromBinary(compressed[0][0], compressed[0][1])
print(fromb)

"""
0010111010010110001001011000010101100011101100101
0010111010010110001001011000010101100011101100101
"""
