# CountingSort

def counting_sort(A, B, k):
    C = [0] * (k+1)
    for j in range(0, len(A)):
        C[A[j]] += 1
    # C[i] now contains the number of elements equal to i.
    for i in range(1, k+1):
        C[i] += C[i-1]
    # C[i] now contains the number of elements less than or equal to i.
    for j in reversed(range(0, len(A))):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1

test1 = [2, 5, 3, 0, 2, 3, 0, 3]
B = [0] * len(test1)
counting_sort(test1, B, 5)
assert B == [0, 0, 2, 2, 3, 3, 3, 5]