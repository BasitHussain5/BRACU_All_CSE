class BFS:
    def __init__(self, file, m, n):
        self.file = file
        self.m = m
        self.n = n

        self.dic_graph = {}
        for i in range(1, self.m + 1):
            self.dic_graph[i] = []
        for j in range(self.n):
            l2 = self.file.readline()
            x, y = l2.split()
            x, y = int(x), int(y)
            if x in self.dic_graph.keys():
                self.dic_graph[x].append(y)
            if y in self.dic_graph.keys():
                self.dic_graph[y].append(x)
        for k, v in self.dic_graph.items():
            self.dic_graph[k] = set(v)

    def bfs(self, a, b):
        Queue = [(a, [a])]
        while Queue:
            (v, p) = Queue.pop(0)
            for next in self.dic_graph[v] - set(p):
                if next == b:
                    yield p + [next]
                else:
                    Queue.append((next, p + [next]))

    def shortest(self, a, b):
        try:
            return next(self.bfs(a, b))
        except StopIteration:
            return None


# input1
f1 = open("input5_1.txt", "r")
file_out = open("output5_1.txt", "w")
x = f1.readline()
x = x.split()
g1 = BFS(f1, int(x[0]), int(x[1]))
g = g1.bfs(1, int(x[2]))
g1 = g1.shortest(1, int(x[2]))
file_out.write("Time: " + str(len(g1) - 1) + "\n")
file_out.write("Shortest Path: ")
for i in g1:
    file_out.write(str(i) + " ")

# input2
f2 = open("input5_2.txt", "r")
file_out2 = open("output5_2.txt", "w")
x = f2.readline()
x = x.split()
g2 = BFS(f2, int(x[0]), int(x[1]))
g = g2.bfs(1, int(x[2]))
g2 = g2.shortest(1, int(x[2]))
file_out2.write("Time: " + str(len(g2) - 1) + "\n")
file_out2.write("Shortest Path: ")
for i in g2:
    file_out2.write(str(i) + " ")

# input3
f3 = open("input5_3.txt", "r")
file_out3 = open("output5_3.txt", "w")
x = f3.readline()
x = x.split()
g3 = BFS(f3, int(x[0]), int(x[1]))
g = g3.bfs(1, int(x[2]))
g3 = g3.shortest(1, int(x[2]))
file_out3.write("Time: " + str(len(g3) - 1) + "\n")
file_out3.write("Shortest Path: ")
for i in g3:
    file_out3.write(str(i) + " ")

# input4
f4 = open("input5_4.txt", "r")
file_out4 = open("output5_4.txt", "w")
x = f4.readline()
x = x.split()
g4 = BFS(f4, int(x[0]), int(x[1]))
g = g4.bfs(1, int(x[2]))
g4 = g4.shortest(1, int(x[2]))
file_out4.write("Time: " + str(len(g4) - 1) + "\n")
file_out4.write("Shortest Path: ")
for i in g4:
    file_out4.write(str(i) + " ")