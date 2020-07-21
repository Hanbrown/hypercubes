# A file for messing around with various code ideas

"""


col = "000"
for int(col) <= max
    check if valid (function)
        if valid, add to list colors
    increment col (function)
return list


def increment(string color, int k, int n):
    col = list(color)
    #n = 3
    #k = 3

    digit = int(col[n-1])
    digit += 1
    col[n-1] = str(digit)

    for i in range(n-1):
        if int(col[n-i-1]) > k-1:
            col[n-i-1] = 0
            digit = int(col[n-i-2])
            digit += 1
            col[n-i-2] = str(digit)
        else:
            return col

    return col

valid:
    #take current vertex. Are there adjacent vertices with the same color? If yes, invalid. If no, valid. Do for each vertex
    for i in range(n):
        adj = next line
        for j in range(n, start at i):
            if(adj[j] == 1):
                if(col[i] == col[j]):
                    return false
    return true


******************************************
adj[] = file.readline.split

col = ""
cols[]

for s in range( len( adj ) ):
    col += "0"


while col <= 222, e.g. (3-coloring)
    for i in range( adj.len )
        if adj[i] == 1:
            col[i]++



for each line in file, i++
    for m in range(k):
        for j in range( len( adj ), 1): # start at 1. for each number in adjacency matrix row
            if adj[j] == 1
                col[j]++

        cols.append(col)

    adj[] = file.readline.split

"""

def is_valid(col, f, n):
    f.seek(6) # Set file pointer to first line of adjacency matrix
    for i in range(n):
        adj = f.readline().split(" ")
        for j in range(n):
            if adj[j] == "1" and col[i] == col[j]:
                return False
    return True

def increment(color, k, n):
    col = list(color)
    finalCol = ""

    digit = int(col[n - 1])
    digit += 1
    col[n - 1] = str(digit)

    for i in range(n - 1):
        if int(col[n - i - 1]) > k - 1:
            col[n - i - 1] = 0
            digit = int(col[n - i - 2])
            digit += 1
            col[n - i - 2] = str(digit)
        else:
            for j in range(n):
                finalCol += str(col[j])
            return finalCol

    for j in range(n):
        finalCol += str(col[j])

    return finalCol

def getColors(f, n, k):
    col = ""
    maxCol = ""
    colors = []

    for i in range(n):
        col += "0"

    for j in range(n):
        maxCol += str(k-1)
    maxCol = int(maxCol)

    while int(col) <= maxCol:
        if is_valid(col, f, n):
            colors.append(col)
        col = increment(col, k, n)

    return colors


f = open("samplegraph.txt", "r")
n = int(f.readline())
k = int(f.readline())

colors = getColors(f, n, k)
print(colors)
print(len(colors))

f.close()
