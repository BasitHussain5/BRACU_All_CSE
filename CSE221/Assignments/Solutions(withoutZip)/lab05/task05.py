import heapq
import math


class Task05:
    def __init__(self, file):
        self.file = file
        line1 = self.file.readlines()
        line1.pop(0)
        self.ans_List = []
        self.source = []
        s = 0
        val = []
        self.network = []
        for j in range(len(line1)):
            l = line1[j].split()
            if len(l) == 2:
                s += 1
                m = int(l[1])
                if m != 0:
                    d = {}
                    for i in range(m):
                        ln = line1[s]
                        a = ln.strip()
                        b = a.split()
                        cost_num = int(b[2])
                        c1 = []
                        k1 = b[0]
                        k2 = b[1]

                        c1 += [cost_num, k2]
                        if k1 in d.keys():
                            d[k1].append(c1)
                        else:
                            d[k1] = [c1]
                        s += 1

                        if k2 not in val:
                            val.append(k2)
                        if k1 not in val:
                            val.append(k1)
                    for k in val:
                        if k not in d.keys():
                            d[k] = []

                    self.network.append(d)
                    idx = s
                    scr = line1[idx].strip()
                    self.source.append(str(scr))
                    s += 1

                if m == 0:
                    d = {}
                    d[l[0]] = []
                    idx = s
                    scr = line1[idx].strip()
                    self.source.append(str(scr))
                    self.network.append(d)
                    s += 1

    def network_function(self, g, source):
        distance = {}
        prev_graph = {}
        for i in g:
            distance[i] = float(-math.inf)
            prev_graph[i] = None
        distance[source] = float(math.inf)
        queue = [[-distance[source], source]]
        while queue:
            x = heapq.heappop(queue)
            y = x[1]
            if y in g.keys():
                for v, n in g.get(y):
                    val = v
                    alter = min(distance[y], v)
                    if alter > distance[n]:
                        distance[n] = alter
                        prev_graph[n] = y
                        heapq.heappush(queue, [-alter, n])
                        heapq.heapify(queue)
        data_list = []
        ss = {}
        sort = sorted(distance.keys())
        for k in sort:
            if k not in ss.keys():
                ss[k] = distance[k]

        if ss[source] == float('inf'):
            data_list.append(0)
        for k in ss.keys():
            if ss[k] != float('-inf') and ss[k] != float('inf'):
                data_list.append(ss[k])
            if ss[k] == float('-inf'):
                data_list.append(-1)

        for i in data_list:
            if i == -1:
                data_list.pop(0)
                data_list.append(0)
                break
        self.ans_List.append(data_list)


file_input = open('input5.txt', "r")
a = Task05(file_input)
z = 0
for i in a.network:
    scr = a.source[z]
    a.network_function(i, scr)
    z += 1
ans = []

for i in a.ans_List:
    stro = ""
    for j in i:
        stro += str(j)
        stro += " "
    x2 = f"{stro}\n"
    ans.append(x2)
file_output = open('output5.txt', "w")
for i in ans:
    file_output.write(str(i))