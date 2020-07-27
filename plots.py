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

# return an array of proper colorings of the graph base
def getColors(base, n, k):
    col = 0
    maxCol = pow(k, n) - 1
    colors = []

    # check if col is valid coloring of base graph. Add to list if it is, then increment col and repeat
    while col <= maxCol:
        if is_valid(col, base, n, k):
            colors.append(col)
        col += 1

    return colors

# TODO use brute-force to find faces in the graphs
# def shadeFaces(g): # g is the graph whose faces we want to shade
#
#     return

# *********************************************************************************** #
# *****                           Main Program                               ******** #

f = open("samplegraph.txt", "r")

# generate base graph
bg = net.Network()
n = int(f.readline())  # first line states number of vertices of base graph
k = int(f.readline())  # second line states number of colors
matrix = []

# generate base graph and adjacency matrix
for i in range(n):
    bg.add_node(i)
    neighbors = f.readline().split(" ")  # read a line of the adjacency matrix
    matrix.append([])
    for j in range(i):
        if int(neighbors[j]) > 0:
            bg.add_edge(i, j)
            print(bg.num_edges())

    # Add the current number to an adjacency matrix
    for j in range(n):
        matrix[i].append( int(neighbors[j]) )

f.close()
bg.show_buttons(filter_=['physics'])
bg.show("samplegraphvis.html")

# generate coloring graph
cg = net.Network()
colorings = getColors(matrix, n, k)  # ************** getColors function call ******************* #

for coloring in colorings:  # add each coloring as a node in cg
    cg.add_node(coloring)

nk = len(colorings)
for i in range(nk):  # generate edges between colorings by brute force
    for j in range(i):  # add edge for every adjacent previous coloring
        if is_adjacent(n, k, colorings[i], colorings[j]):  # understand this!
            cg.add_edge(colorings[i], colorings[j], color='red', value=4)

cg.show("samplecolgraphvis.html")

