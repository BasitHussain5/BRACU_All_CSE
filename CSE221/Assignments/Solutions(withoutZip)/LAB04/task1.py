def task01a(file, sample):
    if sample == 1:
        file_out = open("output1a_1.txt", "w")
    elif sample == 2:
        file_out = open("output1a_2.txt", "w")

    l = file.readline().strip()
    l = l.split()
    m, n = int(l[0]), int(l[1])

    adj_mat = [[0 for i in range(m)] for j in range(n)]

    for i in range(n):
        fil = file.readline()
        n1, n2, w = int(fil[0]), int(fil[2]), int(fil[4])
        adj_mat[n1 - 1][n2 - 1] = w

    for i in range(n):
        for j in range(m):
            a = adj_mat[i][j]
            file_out.write(str(a) + " ")
        file_out.write("\n")


file1 = open("input1a_1.txt", "r")
file2 = open("input1a_2.txt", "r")
task01a(file1, 1)
task01a(file2, 2)


def task01b(file, sample):
    if sample == 1:
        file_out = open("output1b_1.txt", "w")
    elif sample == 2:
        file_out = open("output1b_2.txt", "w")
    elif sample == 3:
        file_out = open("output1b_3.txt", "w")

    l = file.readline().strip()
    l = l.split()
    m, n = int(l[0]), int(l[1])
    dic_graph = {}
    for i in range(m + 1):
        dic_graph[i] = []

    for j in range(n):
        l2 = file.readline()
        x, y, z = l2.split()
        x, y, z = int(x), int(y), int(z)
        if x in dic_graph.keys():
            dic_graph[x].append((y, z))
    for key, val in dic_graph.items():
        file_out.write(f'{key}:{" ".join(map(str, val))}')
        file_out.write("\n")


file1 = open("input1b_1.txt", "r")
file2 = open("input1b_2.txt", "r")
file3 = open("input1b_3.txt", "r")
task01b(file1, 1)
task01b(file2, 2)
task01b(file3, 3)

# Brainstorming:
# a) What if it was an undirected graph? Can you think of where
# you have to modify in your code for an undirected graph?

# If it was an undirected graph, then we modify our code in these way that graph represent vertices in
# bidirectional i.e
#         if x in dic_graph.keys():
#             dic_graph[x].append((y, z))
#         if y in dic_graph.keys():
#             dic_graph[y].append((x, z))



# In the last input of Task 01 (B), you notice there are two
# edges from node ‘9’ to node ‘2’ of cost 10 and 12, known as
# parallel edges. If a graph contains parallel edges, then
# can we represent the graph using Adjacency Matrix?

# The adjacency matrix of a finite undirected graph is a symmetric matrix. This remains true even if we allow loops and parallel edges.
# The adjacency matrix of a finite undirected graph has entries only 0s and 1s. This remains true even if we allow loops but is no longer true if we allow parallel edges.
# The adjacency matrix of a finite undirected graph has 0s throughout the diagonal. This remains true even if we allow parallel edges but is no longer true if we allow loops.
