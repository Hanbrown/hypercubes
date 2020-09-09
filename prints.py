# A file for messing around with various code ideas
import math

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


def is_valid(col):
    # f.seek(6) # Set file pointer to first line of adjacency matrix
    for i in range(n):

        copy = col  # Necessary for nested loop

        digitI = col // (pow(k, n - i - 1))  # Read color from left to right
        for j in range(n - i):
            digitJ = copy % k  # We read color rtl
            if adj[i][n - j - 1] == 1 and digitI == digitJ:  # If 2 adjacent verts have equal colorings. n-1 b/c of rtl
                return False

            copy = copy // k

        col = col % (pow(k, n - i - 1))

    return True


def getColors():
    col = 0
    maxCol = pow(k, n) - 1
    colors = []

    while col <= maxCol:
        if is_valid(col):
            colors.append(col)
        col += 1

    return colors

# Given that v is adjacent to final element in nbrs,
# and all adjacent elements of nbrs are adjacent vertices in coloring graph,
# check if all generators commute with each other
def commutes(g1, v, nbrs):
    n = len(nbrs)
    tN = int(math.log(abs(nbrs[n-1] - v), k))  # Find trace of generator between v and final element in nbrs
    for i in range(1, len(nbrs)):
        t1 = int(math.log( abs(nbrs[i] - nbrs[i-1]), k))  # Find trace between two adjacent elements in nbrs
        if adj[t1][tN] == 1:
            return False

    return True


def getNeighbors(col):
    copy = col
    gens = []
    for i in range(n):
        v = copy % pow(k, i + 1)  # v is a place value in col
        copy1 = col - v
        for j in range(k):
            if copy1 != col and is_valid(copy1):
                # gens.append(i)
                gens.append(copy1)
                # print(copy1) Verify that the decision is being made for the right coloring
                break
            copy1 += pow(k, i)  # keep adding 1 to the place and check if the result is a valid coloring
        copy -= v
    return gens


# Precondition: i = 0; S is an array of length 1 containing v1; N has neighbors of v1
def getGens(v1, i, S, N):
    # Base case: we reach end of decision tree
    if i == n:
        SC = S.copy()  # These two lines may not be necessary, ultimately
        del SC[0]
        RS.append(SC)
        return

    getGens(v1, i+1, S, N)  # Skip existing generator and go left

    nv1 = findNeighbor(v1, i, N)
    if nv1 > -1 and commutes(i, nv1, S):  # commutes(i, S):
        # Find neighbor with vertex i changed
        S0 = S.copy()  # Copy created because otherwise, S is mutated in all stack frames
        S0.append(nv1)
        N = getNeighbors(nv1)
        getGens(nv1, i+1, S0, N)

    return


def findNeighbor(v, t, N):
    for v0 in N:
        if int( math.log(abs(v - v0), k) ) == t:  # log base k of | v-v0 | == t:
            return v0
    return -1

# ******************************************************************************************************************** #
global f, n, k, adj, RS
f = open("samplegraph.txt", "r")
n = int(f.readline())
k = int(f.readline())

adj = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
v = 7
g5 = getNeighbors(v)
RS = []
set1 = [v]
getGens(v, 0, set1, g5)
print(RS)

# colors = getColors()
# print(colors)
# print(len(colors))

f.close()
