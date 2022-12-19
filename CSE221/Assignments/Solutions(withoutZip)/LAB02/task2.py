import sys

sys.stdin = open("input2.txt", "r")
sys.stdout = open("output2.txt", "w")

size = int(input())
array = input().split()


def MergeFunction(array, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    left = [0] * n1
    right = [0] * n2

    for i in range(0, n1):
        left[i] = array[p + i]
    for j in range(0, n2):
        right[j] = array[q + 1 + j]

    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if int(left[i]) <= int(right[j]):
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = right[j]
        j += 1
        k += 1


def MergeSortFunction(array, p, r):
    if p < r:
        q = p + (r - p) // 2
        MergeSortFunction(array, p, q)
        MergeSortFunction(array, q + 1, r)
        MergeFunction(array, p, q, r)


MergeSortFunction(array, 0, size - 1)
for i in range(size):
    print(array[i], end = " ")


