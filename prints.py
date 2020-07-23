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
        copy = col # Necessary for nested loop
        adj = f.readline().split(" ") # Read each row of the adjacency matrix
        digitI = col // (pow(10, n - i - 1)) # Read color from left to right

        for j in range(n-i):
            digitJ = copy % 10 # Read color from right to left
            if adj[n-j-1].rstrip("\n") == "1" and digitI == digitJ:
                return False
            copy = copy // 10

        col = col % (pow(10, n - i - 1))

    return True

def increment(col, inc, k):
    if inc == 0:
        return col

    digit = col % 10 # = 2
    digit += inc # = 3

    inc = int( digit / k )
    col = int( col / 10 )

    col = increment(col, inc, k)

    col *= 10
    col += digit % k

    return col

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

print(is_valid(101, f, n))

#colors = getColors(f, n, k)
#print(colors)
#print(len(colors))

#print( increment(0, 1, 3) )

f.close()
