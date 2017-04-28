from os import *
from pygraphviz import AGraph
from collections import deque

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
        #system("display {}.svg".format(name))
    else:
        print("Give me a better tree")
