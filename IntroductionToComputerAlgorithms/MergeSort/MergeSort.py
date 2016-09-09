#MergeSort

import math


def merge(A, p, q, r):
    n1 = q-p
    n2 = r-q
    L = []
    for i in range(0, n1):
        L.append(A[p+i])
    R = []
    for j in range(0, n2):
        R.append(A[q+j])
    #L.append(1000000)#
    #R.append(1000000)#
    x = 0
    y = 0
    for k in range(p, r):
        if x == len(L) and y == len(R):   #
            break         #
        elif x == len(L) and y < len(R):#
            A[k] = R[y]#
            y += 1#
        elif y == len(R) and x < len(L):#
            A[k] = L[x]#
            x +=1#
        elif L[x] <= R[y]:
            A[k] = L[x]
            x += 1
        else:
            A[k] = R[y]
            y = y+1
    p=0

def merge1(A, p, q, r):
    n1 = q-p
    n2 = r-q
    L = []
    for i in range(0, n1):
        L.append(A[p+i])
    R = []
    for j in range(0, n2):
        R.append(A[q+j])
    #L.append(1000000)#
    #R.append(1000000)#
    x = 0
    y = 0
    for k in range(p, r):
        if y == len(R) or ( x < len(L) and L[x] <= R[y] ):
            A[k] = L[x]
            x += 1
        else:
            A[k] = R[y]
            y = y+1
    p=0   

def merge_sort(A, p, r):
    if p < r:
        q = math.floor((p+r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)


def sort(A):
    merge_sort(A, 0, len(A)-1)
    return A

B=[1, 3, 4, 6, 2, 3, 5, 8]
merge(B, 2, 4, 6)
print(B) # expect 1, 3, 2, 3, 4, 6, 5, 8
print(sort([1, 3, 4, 6, 2, 3, 5, 8]))
print(sort([1, 3, 6, 4, 2, 3, 5, 8]))