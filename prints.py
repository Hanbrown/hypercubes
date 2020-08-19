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

def is_valid(col, adj, n, k):
    # f.seek(6) # Set file pointer to first line of adjacency matrix
    for i in range(n):

        copy = col  # Necessary for nested loop

        digitI = col // (pow(k, n - i - 1))  # Read color from left to right
        for j in range(n-i):
            digitJ = copy % k  # We read color rtl
            if adj[i][n-j-1] == 1 and digitI == digitJ:  # If 2 adjacent verts have equal colorings. n-1 b/c of rtl
                return False

            copy = copy // k

        col = col % (pow(k, n - i - 1))

    return True

def getColors(f, n, k):
    col = 0
    maxCol = pow(k, n) - 1
    colors = []

    while col <= maxCol:
        if is_valid(col, f, n):
            colors.append(col)
        col += 1

    return colors

def commutes(g1, gens, adj):

    for g2 in gens:
        if adj[g2][g1] == 1:
            return False

    return True

def getNeighbors(col, adj, k, n):
    copy = col
    gens = []
    for i in range(n):
        v = copy % pow(k, i+1) # v is a place value in col
        copy1 = col - v
        for j in range(k):
            if copy1 != col and is_valid(copy1, adj, n, k):
                gens.append(i)
                # print(copy1) Verify that the decision is being made for the right coloring
                break
            copy1 += pow(k, i)  # keep adding 1 to the place and check if the result is a valid coloring
        copy -= v
    return gens

f = open("samplegraph.txt", "r")
n = int(f.readline())
k = int(f.readline())

adj = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
g5 = getGens(20, adj, k, n)

print(commutes(1, g5, adj))

#colors = getColors(f, n, k)
#print(colors)
#print(len(colors))

#print( increment(0, 1, 3) )

f.close()
