# sk, 7/5/20
# [edited] pr, 7/16/20

# from pyvis.network import Network
from pyvis import network as net
import networkx as nx
import math


# return whether two coloring values differ on exactly one vertex
def is_adjacent(v1, v2):
    same = True
    for i in range(n):  # check each digit for sameness
        digitdif = v1 % k - v2 % k
        if same and digitdif != 0:
            same = False
        elif digitdif != 0:
            return False
        v1 = v1 // k
        v2 = v2 // k
    return True


# return whether a coloring col is a proper (valid) coloring of the graph in adjacency matrix
def is_valid(col):
    copyI = col
    for i in range(n):

        copyJ = col  # Necessary for nested loop

        digitI = copyI % k  # Read color rtl
        for j in range(n):
            digitJ = copyJ % k  # We read color rtl
            if adj[i][j] == 1 and digitI == digitJ:  # If 2 adjacent verts have equal colorings. n-1 b/c of rtl
                return False

            copyJ = copyJ // k

        copyI = copyI // k

    return True


# return an array of proper colorings of the graph base
def getColors():
    col = 0
    maxCol = pow(k, n) - 1
    colors = []

    # check if col is valid coloring of base graph. Add to list if it is, then increment col and repeat
    while col <= maxCol:
        if is_valid(col):
            colors.append(col)
        col += 1

    return colors


# Given that v is adjacent to final element in nbrs,
# and all adjacent elements of nbrs are adjacent vertices in coloring graph,
# check if all generators commute with each other
def commutes(v, nbrs):
    n = len(nbrs)
    tn = int(math.log(abs(nbrs[0] - v), k))  # Find trace of generator between v and final element in nbrs
    for i in range(1, len(nbrs)):
        t1 = int(math.log( abs(nbrs[i] - nbrs[i-1]), k))  # Find trace between two adjacent elements in nbrs
        if adj[t1][tn] == 1 or t1 == tn:
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
                gens.append(copy1)
            copy1 += pow(k, i)  # keep adding 1 to the place and check if the result is a valid coloring
        copy -= v
    return gens


def findNeighbor(v, t, N):
    for v0 in N:
        if int( math.log(abs(v - v0), k) ) == t:  # log base k of | v-v0 | == t:
            return v0
    return -1


# Precondition: i = 0; S is an array of length 1 containing v1; N has neighbors of v1
def getGens(v1, i, S, N):
    # Base case: we reach end of decision tree
    if i == len(N):
        SC = S.copy()  # These two lines may not be necessary, ultimately
        del SC[0]
        RS.append(SC)
        return

    getGens(v1, i+1, S, N)  # Skip existing generator and go left

    nv1 = N[i]
    if nv1 > -1 and commutes(nv1, S):  # commutes(i, S):
        # Find neighbor with vertex i changed
        S0 = S.copy()  # Copy created because otherwise, S is mutated in all stack frames
        S0.append(nv1)
        getGens(v1, i+1, S0, N)

    return


# *********************************************************************************** #
# *****                           Main Program                               ******** #

f = open("samplegraph.txt", "r")

# generate base graph
bg = net.Network()
global n, k, adj, RS
n = int(f.readline())  # first line states number of vertices of base graph
k = int(f.readline())  # second line states number of colors
adj = []
RS = []

# generate base graph and adjacency matrix
for i in range(n):
    bg.add_node(i)
    neighbors = f.readline().split(" ")  # read a line of the adjacency matrix
    adj.append([])
    for j in range(i):
        if int(neighbors[j]) > 0:
            bg.add_edge(i, j)
            print(bg.num_edges())

    # Add the current number to an adjacency matrix
    for j in range(n):
        adj[i].append( int(neighbors[j]) )

f.close()
bg.show_buttons(filter_=['physics'])
bg.show("samplegraphvis.html")

# generate coloring graph
cg = net.Network()
colorings = getColors()  # ************** getColors function call ******************* #

for coloring in colorings:  # add each coloring as a node in cg
    cg.add_node(coloring)

nk = len(colorings)
for i in range(nk):  # generate edges between colorings by brute force
    for j in range(i):  # add edge for every adjacent previous coloring
        if is_adjacent(colorings[i], colorings[j]):  # understand this!
            cg.add_edge(colorings[i], colorings[j], color='red', value=4)

cg.show("samplecolgraphvis.html")

v = colorings[2]
set1 = [v]
gV = getNeighbors(v)
print(gV)
getGens(v, 0, set1, gV)
RS.sort(reverse=True, key=len)
print(RS)
