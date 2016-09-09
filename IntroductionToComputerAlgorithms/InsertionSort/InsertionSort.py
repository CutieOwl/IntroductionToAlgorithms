# Insertion Sort

def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key

test = [5, 2, 4, 7, 6, 1, 3]
insertionSort(test)
assert test == [1, 2, 3, 4, 5, 6, 7]
print(test)

