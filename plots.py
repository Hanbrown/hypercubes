# sk, 7/5/20
# [edited] pr, 7/16/20

# from pyvis.network import Network
from pyvis import network as net
import networkx as nx


# return whether two coloring values differ on exactly one vertex
def is_adjacent(n, k, v1, v2):
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

# return whether a coloring col is a proper (valid) coloring of the graph in file f
def is_valid(col, f, n):
    f.seek(6) # Set file pointer to first line of adjacency matrix
    for i in range(n):
        copy = col # Necessary for nested loop
        adj = f.readline().split(" ") # Read each row of the adjacency matrix
        digitI = col // (pow(10, n - i - 1)) # Read color from left to right

        for j in range(n-i): # We read color rtl here so we don't read over characters we already read
            digitJ = copy % 10 # Read color from right to left
            if adj[n-j-1].rstrip("\n") == "1" and digitI == digitJ: # If 2 adjacent vertices have equal colorings
                return False
            copy = copy // 10

        col = col % (pow(10, n - i - 1))

    return True

def increment(col, inc, k):
    if inc == 0:
        return col

    digit = col % 10 # = 2
    digit += inc # = 3

    inc = digit // k
    col = col // 10

    col = increment(col, inc, k)

    col *= 10
    col += digit % k

    return col

def getColors(f, n, k):
    col = 0
    maxCol = ""
    colors = []

    # set max to be k-1 repeated n times, e.g. k=3, n=4, max = 2222
    for j in range(n):
        maxCol += str(k-1)
    maxCol = int(maxCol)

    # check if col is valid coloring of graph. Add to list if it is, then increment col and repeat
    while col <= maxCol:
        if is_valid(col, f, n):
            colors.append(col)
        col = increment(col, 1, k)

    return colors

# *********************************************************************************** #
# *****                           Main Program                               ******** #

f = open("samplegraph.txt", "r")

# generate base graph

bg = net.Network()
n = int(f.readline())  # first line states number of vertices of base graph
k = int(f.readline())  # second line states number of colors (7/16/2020)

# generate base graph
for i in range(n):
    bg.add_node(i)
    neighbors = f.readline().split(" ")  # read a line of the adjacency matrix
    for j in range(i):
        if int(neighbors[j]) > 0:
            bg.add_edge(i, j)

            print(bg.num_edges())
bg.show_buttons(filter_=['physics'])
bg.show("samplegraphvis.html")

# generate coloring graph
cg = net.Network()
colorings = []
coloringsBase = getColors(f, n, k)

for coloring in coloringsBase:  # add each coloring to a list and as a node in cg
    copy = coloring # used for the loop
    val = 0
    for i in range(n):
        digitI = copy // pow(10, n-i-1)
        val += digitI * pow(k, n - i - 1)  # understand this!
        copy = copy % pow(10, n-i-1)
    colorings.append(val)
    cg.add_node(val)


nk = len(colorings)
for i in range(nk):  # generate edges between colorings by brute force
    for j in range(i):  # add edge for every adjacent previous coloring
        if is_adjacent(n, k, colorings[i], colorings[j]):  # understand this!
            cg.add_edge(colorings[i], colorings[j], color='red', value=4)

cg.show("samplecolgraphvis.html")

f.close()
