c =0
def FLOODFIL(x ,y, o, n): 
    if x < 0 or x >= len(field[0]) or y < 0 or y >= len(field):
        return
    if field[y][x] == "#":
        return
    if field[y][x] != o and field[y][x] != "D":
        return
    if field[y][x] == "D":
        global c
        c +=1
    field[y][x] = n
    FLOODFIL(x+1, y, o, n)
    FLOODFIL(x-1, y, o, n)
    FLOODFIL(x, y+1, o,n)
    FLOODFIL(x, y-1, o, n)


f = open("input6_1.txt", "r")
f1 = open("output6_1.txt", "w")
n = f.readline().split()
a, b = int(n[0]), int(n[1])
field = []
for i in range(a):
    s = f.readline().strip()
    t = []
    for j in range(b):
        t.append(s[j])
    field.append(t)
FLOODFIL(0, 0, ".", "GO")
f1.write(str(c))

f = open("input6_2.txt", "r")
f2 = open("output6_2.txt", "w")
n = f.readline().split()
a, b = int(n[0]), int(n[1])
field = []
for i in range(a):
    s = f.readline().strip()
    t = []
    for j in range(b):
        t.append(s[j])
    field.append(t)
FLOODFIL(0, 0, ".", "GO")
f2.write(str(c))

f = open("input6_3.txt", "r")
f3 = open("output6_3.txt", "w")
n = f.readline().split()
a, b = int(n[0]), int(n[1])
field = []
for i in range(a):
    s = f.readline().strip()
    t = []
    for j in range(b):
        t.append(s[j])
    field.append(t)
FLOODFIL(0, 0, ".", "GO")
f3.write(str(c))

f = open("input6_4.txt", "r")
f4 = open("output6_4.txt", "w")
n = f.readline().split()
a, b = int(n[0]), int(n[1])
field = []
for i in range(a):
    s = f.readline().strip()
    t = []
    for j in range(b):
        t.append(s[j])
    field.append(t)
FLOODFIL(0, 0, ".", "GO")
f4.write(str(c))


f = open("input6_5.txt", "r")
f5 = open("output6_5.txt", "w")
n = f.readline().split()
a, b = int(n[0]), int(n[1])
field = []
for i in range(a):
    s = f.readline().strip()
    t = []
    for j in range(b):
        t.append(s[j])
    field.append(t)
FLOODFIL(0, 0, ".", "GO")
f5.write(str(c))

f = open("input6_6.txt", "r")
f6 = open("output6_6.txt", "w")
n = f.readline().split()
a, b = int(n[0]), int(n[1])
field = []
for i in range(a):
    s = f.readline().strip()
    t = []
    for j in range(b):
        t.append(s[j])
    field.append(t)
FLOODFIL(0, 0, ".", "GO")
f6.write(str(c))

f = open("input6_7.txt", "r")
f7 = open("output6_7.txt", "w")
n = f.readline().split()
a, b = int(n[0]), int(n[1])
field = []
for i in range(a):
    s = f.readline().strip()
    t = []
    for j in range(b):
        t.append(s[j])
    field.append(t)
FLOODFIL(0, 0, ".", "GO")
f7.write(str(c))