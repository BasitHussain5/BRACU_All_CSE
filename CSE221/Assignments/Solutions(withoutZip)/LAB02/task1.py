import sys

sys.stdin = open("input1.txt", "r")
sys.stdout = open("output1.txt", "w")

size = int(input())
array = input().split()
marks= input().split()

for i in range(size-1):
    temp = marks[i+1]
    j = i
    while j>= 0:
        if int(marks[j]) < int(temp):
            marks[j+1], marks[j] = marks[j], marks[j+1]
            array[j+1], array[j] = array[j], array[j+1]
        else:
            break
        j -= 1
marks[j+1] = temp
for i in range(size):
    print(array[i], end=" ")
