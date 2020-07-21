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
def is_valid(col, f, n): #str col, file f, int n
    f.seek(6) # Set file pointer to first line of adjacency matrix
    for i in range(n): #read each line
        adj = f.readline().split(" ")

        for j in range(n): #for each vertex, check if adjacent and if colors are same
            if adj[j] == "1" and col[i] == col[j]:
                return False
    return True

# TODO make color an int
def increment(color, k, n): # str color, int k, int n
    col = list(color)
    finalCol = ""

    inc = 1
    for i in range(n - 1, -1, -1):
        digit = (int(col[i]) + inc) % k
        inc = (int(col[i]) + inc) // k  # inc will either be 1 or 0
        col[i] = str(digit)
        finalCol = str(digit) + finalCol

    return finalCol

def getColors(f, n, k):
    col = ""
    maxCol = ""
    colors = []

    # start at 0, and increment up to max
    for i in range(n):
        col += "0"

    # set max to be k-1 repeated n times, e.g. k=3, n=4, max = 2222
    for j in range(n):
        maxCol += str(k-1)
    maxCol = int(maxCol)

    # check if col is valid coloring of graph. Add to list if it is, then increment col and repeat
    while int(col) < maxCol:
        if is_valid(col, f, n):
            colors.append(col)
        col = increment(col, k, n)

    # special case -- check if maxCol is a valid coloring. Keeping it in the loop caused an infinite loop
    maxCol = str(maxCol)
    if is_valid(maxCol, f, n):
        colors.append(col)

    return colors

# *********************************************************************************** #
# *****                           Main Program                               ******** #

f = open("samplegraph.txt", "r")

# generate base graph

bg = net.Network()
n = int(f.readline())  # first line states number of vertices of base graph
k = int(f.readline())  # second line states number of colors (7/16/2020)
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
#k = int(f.readline())  # after adjacency matrix, next line says number of colors (commented-out on 7/16/2020)
colorings = []

""" TODO: Assume the input file stops after k, and replace the following loop
that reads in colorings (corresponding to cg vertices) with code that
generates all the k-colorings by brute force subject to base graph constraints.
"""
coloringsBase = getColors(f, n, k)

"""for coloring in f:  # add each coloring to a list and as a node in cg
    labels = coloring.split(" ")  # read each label. TODO: generate this dynamically
    val = 0
    for i in range(n):
        val += int(labels[i]) * pow(k, n - i - 1)  # TODO: understand this!
    colorings.append(val)
    cg.add_node(val)
"""

for coloring in coloringsBase:  # add each coloring to a list and as a node in cg
    labels = list(coloring)  # read each label. TODO: generate this dynamically
    val = 0
    for i in range(n):
        val += int(labels[i]) * pow(k, n - i - 1)  # TODO: understand this!
    colorings.append(val)
    cg.add_node(val)


nk = len(colorings)
for i in range(nk):  # generate edges between colorings by brute force
    for j in range(i):  # add edge for every adjacent previous coloring
        if is_adjacent(n, k, colorings[i], colorings[j]):  # TODO: understand this!
            cg.add_edge(colorings[i], colorings[j], color='red', value=4)

cg.show("samplecolgraphvis.html")

f.close()
