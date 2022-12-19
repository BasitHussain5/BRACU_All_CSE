class Task3:
    def __init__(self, file):
        self.file = file
        self.l = int(self.file.readline())
        self.array = self.file.readline().split()
        self.array1 = []
        for i in self.array:
            self.array1.append(int(i))
        self.c = self.file.readline()

    def ChoresSellection(self, array1, cl, output):
        array1.sort()
        chsn = []
        indx = 0
        Jack = 0
        Jill = 0
        seq = ""
        for i in cl:
            if i == "J":
                v = array1[indx]
                chsn.append(v)
                seq += str(v)
                indx += 1
                Jack += v
            elif i == "j":
                chsn.sort()
                a = chsn.pop()
                seq += str(a)
                Jill += a

        output.write(f'{seq}\n')
        output.write(f'Jack will work for {Jack} hours\n')
        output.write(f'Jill will work for {Jill} hours\n')


# test1

file1 = open("task3_input1.txt", "r")
output1 = open("task3_output1.txt", "w")
test1 = Task3(file1)
array1 = test1.array1
cl = test1.c
test1.ChoresSellection(array1, cl, output1)

# test2
file2 = open("task3_input2.txt", "r")
output2 = open("task3_output2.txt", "w")
test2 = Task3(file2)
array1 = test2.array1
cl = test2.c
test1.ChoresSellection(array1, cl, output2)