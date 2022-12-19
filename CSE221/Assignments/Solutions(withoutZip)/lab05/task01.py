import heapq
import math


class Task01:
    def __init__(self, file):
        self.f = file
        self.line = self.f.readlines()
        self.dict = {}
        for i in range(len(self.line)):
            line1 = self.line[i]
            a = line1.strip()
            b = line1.split()
            cost_num = int(b[2])
            c1 = []
            c2 = []
            k1 = b[0]
            k2 = b[1]
            c1 += [cost_num, k2]
            c2 += [cost_num, k1]

            if k1 in self.dict.keys():
                self.dict[k1].append(c1)
            else:
                self.dict[k1] = [c1]

            if k2 in self.dict.keys():
                self.dict[k2].append(c2)
            else:
                self.dict[k2] = [c2]
        self.p1 = []
        self.queue = []
        self.dist = {}
        self.prev = {}

    def Dijkstra(self, graph, source):
        for i in graph:
            self.dist[i] = float(math.inf)
            self.prev[i] = None
        self.dist[source] = 0
        sett = set()
        self.queue = [[0, source]]
        while self.queue:
            x = heapq.heappop(self.queue)
            y = x[1]
            if y not in sett:
                sett.add(y)
                if y in self.dict.keys():
                    for cost_num, neigh in self.dict.get(y):
                        alt = self.dist[y] + cost_num
                        if self.dist[neigh] > alt and neigh not in sett:
                            self.dist[neigh] = alt
                            self.prev[neigh] = y
                            for i in self.queue:
                                if neigh in i[1]:
                                    self.queue.remove(i)
                            heapq.heappush(self.queue, [alt, neigh])
                            heapq.heapify(self.queue)

    def path(self, p, source, n, list1):
        if n == source:
            self.p1.append(list1)
        else:
            i = p[n]
            list1.append(i)
            self.path(p, source, i, list1)

    def print_f(self, f1):
        self.f1 = f1
        out = []
        x1 = f"{self.dist['MOGHBAZAR']}\n"
        out.append(x1)
        r = self.p1[0]
        r.reverse()
        stro = ""
        for i in r:
            stro += str(i)
            stro += "->"
        s1 = stro[:-2]

        x2 = f"{s1}\n"
        out.append(x2)
        for i in out:
            self.f1.write(str(i))


f = open('input1.txt', 'r')
f1 = open('output1.txt', 'w')
a = Task01(f)
graph = a.dict
s = a.Dijkstra(graph, "Motijheel")
prev = a.prev
d = a.path(prev, "Motijheel", "MOGHBAZAR", list1=["MOGHBAZAR"])
a.print_f(f1)