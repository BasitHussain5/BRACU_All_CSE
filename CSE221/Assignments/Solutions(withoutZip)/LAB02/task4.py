# a)

import sys
sys.stdin = open("input4.txt", "r")
sys.stdout = open("output4(a).txt", "w")
array = []
for i in range(12):
    a = input()
    array.append(a)

class ArrayQueue:
    q = []
    front = 0
    rear = -1

    def enqueue(self, val):
        self.q.append(val)
        self.rear += 1
        return self.q

    def dequeue(self):
        self.q = self.q[self.front + 1:self.rear + 1]
        self.rear -= 1
        return self.q

    def bubbleSort(self, array):
        arr = []
        for i in range(len(array)):
            arr.append(array[i][4])

        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                if int(arr[j]) > int(arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    array[j], array[j + 1] = array[j + 1], array[j]
        print(array)


obj = ArrayQueue()
print("Q 4 (a)")
for i in array:
    if i != "see doctor":
        obj.bubbleSort(obj.enqueue(i))

    else:
        print(obj.dequeue())



# b)


sys.stdin = open("input4.txt", "r")
sys.stdout = open("output4(b).txt", "w")
array = []
for i in range(12):
    a = input()
    array.append(a)


class HeapSort:
    q = []
    front = 0
    rear = -1

    def enqueue(self, val):
        self.q.append(val)
        self.rear += 1
        return self.q

    def dequeue(self):
        self.q = self.q[self.front + 1:self.rear + 1]
        self.rear -= 1
        return self.q

    def heapify(self, arr, n, i):
        array = []
        for i in range(len(arr)):
            a = int(arr[i][-1])
            array.append(a)

        large = i
        l = 2 * i + 1
        r = (2 * i) + 2
        if l < n and array[i] < array[l]:
            large = l
        if r < n and array[large] < array[r]:
            large = r
        if large != i:
            array[i], array[large] = array[large], array[i]
            arr[i], arr[large] = arr[large], arr[i]
            heapify(arr, n, large)

    def heapsort(self, array):
        n = len(array)
        for i in range(n, -1, -1):
            self.heapify(array, n, i)
        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self.heapify(array, i, 0)
        return array


ob = HeapSort()
print("Q4 (b)")
for i in array:
    if i != "see doctor":
        print(ob.heapsort(ob.enqueue(i)))

    else:
        print(ob.dequeue())


# (d)


import time
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt


def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if (arr[j]) > (arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def heapify(array, n, i):
    large = i
    l = 2 * i + 1
    r = (2 * i) + 2
    if l < n and array[i] < array[l]:
        large = l
    if r < n and array[large] < array[r]:
        large = r
    if large != i:
        array[i], array[large] = array[large], array[i]
        heapify(array, n, large)


def heapsort(array):
    n = len(array)
    for i in range(n, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        heapify(array, i, 0)
        array[i], array[0] = array[0], array[i]


e = list()
t = list()
for i in range(1, 10):
    a = randint(0, 1000 * i, 100 * i)
    st = time.time()
    bubbleSort(a)
    end = time.time()
    print(len(a), "Elements Sorted by bubble sort-start")

    e.append(len(a))
    t.append(end - st)

plt.xlabel('List Length')
plt.ylabel('Time Complexity')
plt.plot(e, t, label='Bubble')
plt.grid()
plt.legend()
plt.show()

ee = list()
tt = list()
for i in range(1, 10):
    a = randint(0, 1000 * i, 100 * i)
    st = time.time()
    heapsort(a)
    end = time.time()
    print(len(a), "Elements Sorted by bubble sort-start")

    ee.append(len(a))
    tt.append(end - st)

plt.xlabel('List Length')
plt.ylabel('Time Complexity')
plt.plot(ee, tt, label='Heap Sort')
plt.grid()
plt.legend()
plt.show()

