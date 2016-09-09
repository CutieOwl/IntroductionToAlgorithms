# HeapSort

import math

def parent(i):
    return math.floor((i-1)/2)

def left(i):
    return (2*i) + 1

def right(i):
    return (2*i) + 2

def max_heapify(A, i, heapsize):
    l = left(i)
    r = right(i)
    if l <= heapsize-1 and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heapsize-1 and A[r] > A[largest]:
        largest = r
    if largest != i:
        t = A[i]
        A[i] = A[largest]
        A[largest] = t
        max_heapify(A, largest, heapsize)

def max_heapify_overload(A,i):
    max_heapify(A,i,len(A))

test1 = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
max_heapify_overload(test1, 2)
assert test1==[27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0]

def min_heapify(A, i):
    l = left(i)
    r = right(i)
    if l <= len(A)-1 and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r <= len(A)-1 and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        t = A[i]
        A[i] = A[smallest]
        A[smallest] = t
        min_heapify(A, smallest)

test2 = [4, 3, 5, 2, 1, 6]
min_heapify(test2, 1)
assert test2==[4, 1, 5, 2, 3, 6]

def build_max_heap(A):
    for i in reversed(range(0, (math.floor((len(A)/2))))):
        max_heapify_overload(A, i)

test3 = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
build_max_heap(test3)
assert test3==[16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

def heapsort(A):
    build_max_heap(A)
    heaplength = len(A)
    for i in reversed(range(1, heaplength)):
        j = A[0]
        A[0] = A[i]
        A[i] = j
        heaplength -= 1 
        max_heapify(A, 0, heaplength)
        
test4 = [5, 13, 2, 25, 7, 17, 20, 8, 4]
heapsort(test4)
assert test4==[2, 4, 5, 7, 8, 13, 17, 20, 25]

def heap_maximum(A):
    return A[0]

def heap_extract_max(A):
    heaplength = len(A)
    if heaplength < 1:
        raise ValueError("heap underflow")
    max = A[0]
    A[0] = A[heaplength-1]
    A.pop()
    max_heapify(A, 0, len(A))
    return max

def heap_increase_key(A, i, key):
    if key < A[i]:
        raise ValueError("new key is smaller than current key")
    while i > 0 and A[parent(i)] < key:
        A[i] = A[parent(i)]
        i = parent(i)
    A[i] = key

test7 = [17, 14, 7, 2, 8, 1]
heap_increase_key(test7, 3, 18)
assert test7 == [18, 17, 7, 14, 8, 1]

def heap_increase_key_exchange(A, i, key):
    if key < A[i]:
        raise ValueError("new key is smaller than current key")
    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        e = A[i]
        A[i] = A[parent(i)]
        A[parent(i)] = e
        i = parent(i)

def max_heap_insert(A, key):
    heaplength = len(A)
    A.append(-1000000000)
    heap_increase_key(A, heaplength, key)

def heap_delete(A, i):
    # 3 steps.
    # First step: move deleted key to the root.
    # Second step: switch the root with the last element and delete the last element.
    # Third step: max heapify.
    while i > 0:
        A[i] = A[parent(i)]
        i = parent(i)
    A[0] = A[len(A)-1]
    A.pop()
    max_heapify_overload(A, 0)
    
test8 = [16, 15, 10, 14, 7, 9, 3, 2, 8, 1]
heap_delete(test8, 3)
assert test8 == [16, 15, 10, 8, 7, 9, 3, 2, 1]

test5 = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
print(heap_extract_max(test5))
print(heap_extract_max(test5))
print(heap_extract_max(test5))
print(heap_extract_max(test5))
print(heap_extract_max(test5))
print(heap_extract_max(test5))
print(heap_extract_max(test5))
print(heap_extract_max(test5))
print(heap_extract_max(test5))
print(heap_extract_max(test5))
print(heap_extract_max(test5))
print(heap_extract_max(test5))

test6 = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
max_heap_insert(test6, 10)
assert test6==[15, 13, 10, 5, 12, 9, 7, 4, 0, 6, 2, 1, 8]

def heap_minimum(A):
    return A[0]

def heap_extract_min(A):
    heaplength = len(A)
    if heaplength < 1:
        raise ValueError("heap underflow")
    min = A[0]
    A[0] = A[heaplength-1]
    A.pop()
    min_heapify(A, 0, len(A))
    return min

def heap_decrease_key(A, i, key):
    if key > A[i]:
        raise ValueError("new key is larger than current key")
    A[i] = key
    while i > 0 and A[parent(i)] > A[i]:
        e = A[i]
        A[i] = A[parent(i)]
        A[parent(i)] = e
        i = parent(i)

def min_heap_insert(A, key):
    heaplength = len(A)
    A.append(1000000000)
    heap_decrease_key(A, heaplength, key)