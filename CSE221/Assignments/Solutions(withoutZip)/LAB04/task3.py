class DFS:
    def __init__(self, file, sample):
        self.file = file
        self.sample = sample
        self.Visit = set()

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
        if self.sample == 1:
            self.file_out = open("output3_1.txt", "w")
        elif self.sample == 2:
            self.file_out = open("output3_2.txt", "w")
        elif self.sample == 3:
            self.file_out = open("output3_3.txt", "w")
        elif self.sample == 4:
            self.file_out = open("output3_4.txt", "w")

    def dfs(self, n):
        if n not in self.Visit:
            self.file_out.write(str(n) + " ")
            self.Visit.add(n)
            for neighbour in self.dic_graph[n]:
                self.dfs(neighbour)


f1 = open("input3_1.txt", "r")
f2 = open("input3_2.txt", "r")
f3 = open("input3_3.txt", "r")
f4 = open("input3_4.txt", "r")
g1 = DFS(f1, 1)
s = g1.dfs(1)
g2 = DFS(f2, 2)
h = g2.dfs(1)
g3 = DFS(f3, 3)
j = g3.dfs(1)
g4 = DFS(f4, 4)
k = g4.dfs(1)