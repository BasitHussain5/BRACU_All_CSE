from collections import defaultdict


class GraphCycle:
    def __init__(self, v):
        self.graph = defaultdict(list)
        self.ver = v

    def AppendVer(self, a, b):
        self.graph[a].append(b)

    def IsCyc(self, ver, vis, stack):
        vis[ver] = 1
        stack[ver] = 1

        for i in self.graph[ver]:
            if vis[i] == 0:
                if self.IsCyc(i, vis, stack) == 1:
                    return 1
            elif stack[i] == 1:
                return 1
        stack[ver] = 0
        return 0

    def isCyclic(self):
        vis = [0] * (self.ver + 1)
        stack = [0] * (self.ver + 1)
        for i in range(self.ver):
            if vis[i] == 0:
                if self.IsCyc(i, vis, stack) == 1:
                    return 1
        return 0


f1 = open("input4_1.txt", "r")
f11 = open("output4_1.txt", "w")
x = f1.readline().split()
a, b = int(x[0]), int(x[1])
g = GraphCycle(a)
for i in range(b):
    k = f1.readline().split()
    m, n = int(k[0]), int(k[1])
    g.AppendVer(m, n)
if g.isCyclic() == 1:
    f11.write("Yes")
else:
    f11.write("No")

f2 = open("input4_2.txt", "r")
f22 = open("output4_2.txt", "w")
x = f2.readline().split()
a, b = int(x[0]), int(x[1])
g = GraphCycle(a)
for i in range(b):
    k = f2.readline().split()
    m, n = int(k[0]), int(k[1])
    g.AppendVer(m, n)
if g.isCyclic() == 1:
    f22.write("Yes")
else:
    f22.write("No")

f3 = open("input4_3.txt", "r")
f33 = open("output4_3.txt", "w")
x = f3.readline().split()
a, b = int(x[0]), int(x[1])
g = GraphCycle(a)
for i in range(b):
    k = f3.readline().split()
    m, n = int(k[0]), int(k[1])
    g.AppendVer(m, n)
if g.isCyclic() == 1:
    f33.write("Yes")
else:
    f33.write("No")

f4 = open("input4_4.txt", "r")
f44 = open("output4_4.txt", "w")
x = f4.readline().split()
a, b = int(x[0]), int(x[1])
g = GraphCycle(a)
for i in range(b):
    k = f4.readline().split()
    m, n = int(k[0]), int(k[1])
    g.AppendVer(m, n)
if g.isCyclic() == 1:
    f44.write("Yes")
else:
    f44.write("No")

f5 = open("input4_5.txt", "r")
f55 = open("output4_5.txt", "w")
x = f5.readline().split()
a, b = int(x[0]), int(x[1])
g = GraphCycle(a)
for i in range(b):
    k = f5.readline().split()
    m, n = int(k[0]), int(k[1])
    g.AppendVer(m, n)
if g.isCyclic() == 1:
    f55.write("Yes")
else:
    f55.write("No")

# Brainstorming:
#
# a) Can you find out if the given graph is a tree or not?
# Yes we can find out if the given graph is a tree or not by apply conditions
# if there is no cycle in graph
#  if there is coneected graph
#  and ther is n-1 edges

# b) Suppose that you have an undirected and unweighted graph.
# Can you find out if the graph contains an Odd length Cycle?
# An odd length cycle means the cycle will contain odd
# numbers of vertices.

# It goes without saying that a graph cannot be bipartite if its cycles are odd in length.
# There are two sets of vertices in a bipartite graph, and none of them are connected to any
# other vertex in the same set. Contrary to the definition of bipartite, two vertices of the
# same set must be connected for a cycle of odd length.