class Task1:
    def __init__(self, file):
        self.file = file
        self.n = int(self.file.readline())
        self.array = []
        self.array1 = []
        for i in range(self.n):
            self.array = self.file.readline().split()
            self.array[0], self.array[1] = int(self.array[0]), int(self.array[1])
            self.array1.append(self.array)

    def AssignmentSellection(self, array1, n, output):
        Select = []
        for i in range(n):
            for j in range(i + 1):
                if array1[i][1] < array1[j][1]:
                    array1[i], array1[j] = array1[j], array1[i]
        Select.append(array1[0])
        c = 1
        f = array1[0][1]
        for k in range(n):
            if array1[k][0] >= f:
                c += 1
                f = array1[k][1]
                Select.append(array1[k])

        output.write(f"{c}\n")
        for v in Select:
            output.write(f"{v[0]} {v[1]}\n")


# test1

file1 = open("task1_input1.txt", "r")
output1 = open("task1_output1.txt", "w")
test1 = Task1(file1)
array1 = test1.array1
n = test1.n
test1.AssignmentSellection(array1, n, output1)

# test2
file2 = open("task1_input2.txt", "r")
output2 = open("task1_output2.txt", "w")
test2 = Task1(file2)
array1 = test2.array1
n = test2.n
test2.AssignmentSellection(array1, n, output2)