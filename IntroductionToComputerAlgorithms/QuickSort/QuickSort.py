# QuickSort

import random

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            y = A[i]
            A[i] = A[j]
            A[j] = y
    z = A[i+1]
    A[i+1] = A[r]
    A[r] = z
    return i+1

test1 = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
print(partition(test1, 0, 11))

test2 = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
quicksort(test2, 0, 11)
print(test2)

def randomized_partition(A, p, r):
    i = random.randint(p, r)
    y = A[r]
    A[r] = A[i]
    A[i] = y
    return partition(A, p, r)

def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q-1)
        randomized_quicksort(A, q+1, r)

test3 = [2, 8, 7, 1, 3, 5, 6, 4]
randomized_quicksort(test3, 0, 7)
print(test3)

test4 = list(range(10000))
#quicksort(test4, 0, 9999)
#print("done")

def hoare_partition(A, p, r):
    x = A[p]
    i = p-1
    j = r+1
    while True:
        j -= 1
        while A[j] > x:
            j -= 1
        i += 1
        while A[i] < x:
            i += 1
        if i < j:
            y = A[i]
            A[i] = A[j]
            A[j] = y
        else:
            return j

def hoare_quicksort(A, p, r):
    if p < r:
        split = hoare_partition(A, p, r)
        hoare_quicksort(A, p, split)
        hoare_quicksort(A, split+1, r)

test5 = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
print(hoare_partition(test5, 0, 11))
print(test5)

test6 = [8, 8, 8, 8, 8, 8, 8, 8]
print(hoare_partition(test6, 0, 7))

test7 = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
hoare_quicksort(test7, 0, 11)
print("Test7: ", test7)

def tail_recursive_quicksort(A, p, r):
    while p < r:
        # partition and sort left subarry
        q = partition(A, p, r)
        tail_recursive_quicksort(A, p, q-1)
        p = q + 1