class BFS:
    def __init__(self, file):
        self.file = file
        self.Visit = []
        self.Queue = []
        x = self.file.readline()
        x = x.split()
        m, n = int(x[0]), int(x[1])

        self.dic_graph = {}
        for i in range(1, m + 1):
            self.dic_graph[i] = []
        for j in range(n):
            l2 = self.file.readline()
            x, y = l2.split()
            x, y = int(x), int(y)
            if x in self.dic_graph.keys():
                self.dic_graph[x].append(y)
            if y in self.dic_graph.keys():
                self.dic_graph[y].append(x)

    def bfs(self, r, sample):
        if sample == 1:
            file_out = open("output2_1.txt", "w")
        elif sample == 2:
            file_out = open("output2_2.txt", "w")
        elif sample == 3:
            file_out = open("output2_3.txt", "w")
        elif sample == 4:
            file_out = open("output2_4.txt", "w")
        self.Visit.append(r)
        self.Queue.append(r)

        while self.Queue:
            m = self.Queue.pop(0)
            file_out.write(str(m) + " ")

            for neighbour in self.dic_graph[m]:
                if neighbour not in self.Visit:
                    self.Visit.append(neighbour)
                    self.Queue.append(neighbour)


f1 = open("input2_1.txt", "r")
f2 = open("input2_2.txt", "r")
f3 = open("input2_3.txt", "r")
f4 = open("input2_4.txt", "r")
g1 = BFS(f1)
s = g1.bfs(1, 1)
g2 = BFS(f2)
h = g2.bfs(1, 2)
g3 = BFS(f3)
j = g3.bfs(1, 3)
g4 = BFS(f4)
k = g4.bfs(1, 4)