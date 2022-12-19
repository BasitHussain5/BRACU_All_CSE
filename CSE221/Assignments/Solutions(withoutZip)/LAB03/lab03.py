
# CSE221 Lab 03 Graphs

def readFile():
    # reading file from as input
    # change the file name according to yours
    f = open("graph.txt", "r")
    # first line of input contains the number of vertices in the graph
    n = f.readline()
    # strip() gets rid of the new line
    # try printing n without strip()
    print(n.strip())
    n = n.strip()
    print(type(n))
    # n is of type string. we need to convert it to int
    n = int(n)
    print(type(n))

    # the second line of the file contains the number of connections
    c = f.readline()
    c = c.strip()
    c = int(c)
    print(c)

    buildGraphUsingListofLists(c, f)


#     buildGraphUsingDictionary(c,f)

# we want to build an adjacency list like the following
# A -> B,C
# One vertex can be connected to multiple vertices
# which means multiple values are associated with one vertex
# one data structure that can be used is a dictionary of lists
# {A:[B,C]}

def buildGraphUsingDictionary(c, f):
    # creating a dictionary
    graph = {}
    # the following lines of the file contain the connections
    # creating a directed graph (a,b means a is connected to b)

    counter = 0
    while (counter < c):
        line = f.readline()  # reading each libe
        a, b = line.split(",")  # splitting the vertices
        b = b.strip()  # getting rid of \n from the end

        # we first search if the value inside variable a exists in the dictionary or not
        if (a in graph):
            # if yes, then append() the value in b to a
            graph[a].append(b)
        else:
            # create a new list in graph with a as the key and b as the value
            graph[a] = [b]
        print(a, b)
        counter += 1

    print(graph)
    printGraph(graph, None)


# TO DO
# This method must be completed by you
# You should code in such a way that the output should be
# 1 -> 2,4
# 2 -> 4
# 3 -> 1,4
# 4 -> 2
# notice this method takes both the graphs as parameters
# this means you have print the same output in the same style for both the datastructures
# if graph is none then print from listGraph
# if listGraph is none then print from graph
def printGraph(graph, listGraph):
    if listGraph == None:
        for k, v in graph.items():
            print(k, " ->", ",".join(v))
    if graph == None:
        for i in range(len(listGraph)):
            print(i + 1, " ->", ",".join(listGraph[i]))


# TO DO
# I have shown you how to build a graph using a dictionary of list
# now your job is to build a graph using list of lists [[E,B],[C,D]]
# it means A -> E,B and B -> C,D
def buildGraphUsingListofLists(c, f):
    listGraph = []
    for i in range(6):
        listGraph = [[] for j in range(c - 2)]
    counter = 0
    while (counter < c):
        line = f.readline()
        a, b = line.split(",")
        b = b.strip()
        a = int(a)
        b = int(b)
        listGraph[a - 1].append(str(b))
        counter += 1
    print(listGraph)
    printGraph(None, listGraph)


# ======================Program starts here.========================

# read file using the readFile() method
readFile()