# -*- coding: utf-8 -*-
"""
Heap homework
April 2016
@author: Nathalie
"""

def newHeap():
    """
    returns a fresh new empty heap
    """
    return [None]
    
def isEmpty(H):
    """
    test if H is empty
    """
    return len(H) == 1

def heapPush(H, x):
    """
    adds x to heap H and returns the heap modified
    """
    H.append(x)
    i = len(H)-1
    while (i > 1) and x[0] < H[i//2][0]:
        (H[i], H[i//2]) = (H[i//2], H[i])
        i = i // 2
    return H
    
def heapPop(H):
    """
    returns and deletes the element of smallest value
    """
    e = H[1]
    H[1] = H[len(H)-1]
    H.pop()
    n = len(H)-1
    ok = False
    i = 1    
    while (i <= n // 2) and not ok:
        j = 2 * i
        if (j + 1 <= n) and (H[j+1][0] < H[j][0]):
            j = j + 1
        if H[i][0] > H[j][0]:
            (H[i], H[j]) = (H[j], H[i])
            i = j
        else:
            ok = True
    return e


def heapify(H):
    """
    makes H a heap (in place) - returns H modified
    """ 
    n = len(H)    
    for pos in range(n//2, 0, -1):
        i = pos
        while i <= (n-1)//2:
            j = 2 * i
            if (j + 1 < len(H)-1) and (H[j+1][0] < H[j][0]):
                j = j + 1
            if H[i][0] > H[j][0]:
                (H[i], H[j]) = (H[j], H[i])
                i = j
            else:
                i = n
    return H
