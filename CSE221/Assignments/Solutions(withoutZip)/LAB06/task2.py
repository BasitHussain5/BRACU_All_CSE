class Task2:
    def __init__(self, file):
        self.file = file
        self.l = self.file.readline().split()
        self.n = int(self.l[0])
        self.m = int(self.l[1])
        self.array = []
        self.array1 = []
        for i in range(self.n):
            self.array = self.file.readline().split()
            self.array[0], self.array[1] = int(self.array[0]), int(self.array[1])
            self.array1.append(self.array)

    def AssignmentSellection(self, array1, n, m, output):
        Select = []
        for i in range(n):
            for j in range(i + 1):
                if array1[i][1] < array1[j][1]:
                    array1[i], array1[j] = array1[j], array1[i]

        for i in range(m):
            nw = []
            Select.append(array1[0])
            f = array1[0][1]

            for k in range(len(array1)):
                if array1[k][0] >= f:
                    f = array1[k][1]
                    Select.append(array1[k])

            for i in array1:
                if i not in Select:
                    nw.append(i)
            array1 = nw
        c = len(Select)
        output.write(f"{c}\n")


# test1

file1 = open("task2_input1.txt", "r")
output1 = open("task2_output1.txt", "w")
test1 = Task2(file1)
array1 = test1.array1
n = test1.n
m = test1.m
test1.AssignmentSellection(array1, n, m, output1)

# test2
file2 = open("task2_input2.txt", "r")
output2 = open("task2_output2.txt", "w")
test2 = Task2(file2)
array1 = test2.array1
n = test2.n
m = test2.m
test2.AssignmentSellection(array1, n, m, output2)