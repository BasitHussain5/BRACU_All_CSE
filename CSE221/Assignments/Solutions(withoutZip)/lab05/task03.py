import heapq
import math


class Task03:
    def __init__(self, file):
        self.file = file
        firts_line = self.file.readlines()
        firts_line.pop(0)
        self.ans_List = []
        self.DList = []
        s = 0
        self.con = []
        self.lis = []
        for i in range(len(firts_line)):
            l = firts_line[i].split()
            if len(l) == 2:
                s += 1
                n = str(l[0])
                self.DList.append(n)
                m = int(l[1])
                if m != 0:
                    dic = {}
                    for j in range(m):
                        var = firts_line[s]
                        a = var.strip()
                        b = a.split()
                        cost_num = int(b[2])
                        c1 = []
                        c2 = []
                        k1 = b[0]
                        k2 = b[1]
                        c1 += [cost_num, k2]
                        c2 += [cost_num, k1]

                        if k1 in dic.keys():
                            dic[k1].append(c1)
                        else:
                            dic[k1] = [c1]
                        if k2 in dic.keys():
                            dic[k2].append(c2)
                        else:
                            dic[k2] = [c2]

                        s += 1
                    self.con.append(dic)

                if m == 0:
                    dic = {}
                    dic[l[0]] = []
                    self.con.append(dic)

    def dijkstra(self, g, source, z):
        distance_dic = {}
        prev_dic = {}
        for i in g:
            distance_dic[i] = float(math.inf)
            prev_dic[i] = None
        distance_dic[source] = 0
        Sett = set()
        queue = [[0, source]]
        while queue:
            x = heapq.heappop(queue)
            y = x[1]
            if y not in Sett:
                Sett.add(y)
                if y in g.keys():
                    for v, n in g.get(y):
                        alt = distance_dic[y] + v
                        if distance_dic[n] > alt and n not in Sett:
                            distance_dic[n] = alt
                            prev_dic[n] = y
                            for i in queue:
                                if n in i[1]:
                                    queue.remove(i)
                            heapq.heappush(queue, [alt, n])
                            heapq.heapify(queue)
        g = self.DList[z]

        def path(p, source, n, list1):
            if n == source:
                self.lis.append(list1)
            else:
                i = p[n]
                list1.append(i)
                path(p, source, i, list1)

        path(prev_dic, "1", g, list1=[g])


file_output = open("input3.txt", "r")
a = Task03(file_output)

z = 0
for graphs in a.con:
    a.dijkstra(graphs, "1", z)
    z += 1
file_output = open("output3.txt", "w")
for q in a.lis:
    q.reverse()
    sa = ""
    for i in q:
        sa += str(i)
        sa += " "
    s1 = sa
    x2 = f'{s1}\n'
    a.ans_List.append(x2)
for i in a.ans_List:
    file_output.write(str(i))