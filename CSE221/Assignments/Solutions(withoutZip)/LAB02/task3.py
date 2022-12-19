import sys

sys.stdin = open("input3.txt", "r")
sys.stdout = open("output3.txt", "w")

size = int(input())
array = input().split()

def partition_fumction(array, l, h):
    pivot = int(array[h])
    i = l - 1
    for j in range(l, h):
        if int(array[j]) <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[h] = array[h], array[i + 1]
    return (i + 1)

def QuickSort(array, l, h):
    if l < h:
        parti = partition_fumction(array, l, h)
        QuickSort(array, l, parti-1)
        QuickSort(array, parti+1, h)


# Q3(ii)
def findk(array, l, h, k):
    if k > 0 and k <= h - l + 1:
        parti = findk_parti(array, l, h)
        if parti - l == k - 1:
            return array[parti]
        elif parti - l > k - 1:
            return findk(array, l, parti - 1, k)
        return findk(array, parti + 1, h, k - parti + l - 1)
    print("out of range")


def findk_parti(array, l, h):
    pivot = int(array[h])
    i = l - 1
    for j in range(l, h):
        if int(array[j]) <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[h] = array[h], array[i + 1]
    return (i + 1)


QuickSort(array, 0, size-1)
print("Q3(i)")
for i in range(size):
    print(array[i], end = " ")

k = 4
a = findk(array, 0, len(array) - 1, k)

print("\nQ3(ii)")
print("kth (smallest) element from an array without sorting is K = 5 ---->",a)

