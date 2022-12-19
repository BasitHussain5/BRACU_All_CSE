import math


class Task4:
    def __init__(self, f):
        self.f = f
        self.l = self.f.readlines()
        self.OutputList = []

    def fucnction(self, lines, output):
        for k in lines:
            a = 0
            k.strip()
            m = k.split()
            n = list(map(int, m))
            x, y = n[0], n[1]
            for l in range(x, y + 1):
                v = str(math.sqrt(l))
                Lastdigit = v[len(v) - 2:]
                if v != '0.0':
                    if '.0' in Lastdigit:
                        a += 1
            self.OutputList.append(a)
        for ind in self.OutputList:
            if ind == 0:
                self.OutputList.remove(ind)
        for ind in self.OutputList:
            output.write(f'{ind}\n')


file_in = open("task4_input.txt", "r")
file_out = open("task4_output.txt", "w")
test = Task4(file_in)
lines = test.l
test.fucnction(lines, file_out)
