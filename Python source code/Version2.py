import sys
import collections
import itertools

def loadMaze(filename):
    #load the data from the file into a 2D list
    with open(filename) as i:
        maze = []
        for line in i:
            line = line.split()
            maze.append(line)
            print(line)
    return maze
matrix=loadMaze("Maze1.txt")


def get_path(prev, i, j):
    path = []
    path.append((i, j))
    while prev[i][j] != (-1, -1):
        i, j = prev[i][j]
        path.append((i, j))
    path.pop()  # remove last source index
    return path[::-1]


def get_edges(matrix, s_node, src, t_node):
    bfs = collections.deque([src, (None, None)])
    parent = [[None] * len(matrix[0]) for _ in range(len(matrix))]
    parent[src[0]][src[1]] = (-1, -1)
    d = 1
    edge = {}
    while bfs:
        i, j = bfs.popleft()
        if i == None:
            d += 1
            if bfs:
                bfs.append((None, None))
        else:
            for n_i, n_j in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if (0 <= n_i < len(matrix) and 0 <= n_j < len(matrix[0]) and
                        parent[n_i][n_j] == None):
                    parent[n_i][n_j] = (i, j)
                    if matrix[n_i][n_j] in t_node:
                        edge[matrix[n_i][n_j]] = get_path(parent, n_i, n_j)
                        if len(edge) == len(t_node) - 1:
                            break
                    elif matrix[n_i][n_j] == "0":
                        bfs.append((n_i, n_j))
    return edge


def shortest_path(path, cost, node, dst, result):
    if path[-1] == dst:
        print(path, cost)
        if cost < result[0]:
            result[0] = cost
            result[1] = path[:]
        return
    cur = path[-1]
    for ne in node[cur].keys():
        if ne not in path:
            if (ord("b") <= ord(ne) <= ord("b") and
                    chr(ord(ne) - ord("b") + ord("a")) not in path):
                continue
            next_cost = cost + len(node[cur][ne])
            if next_cost >= result[0]:
                continue
            path.append(ne)
            shortest_path(path, cost + len(node[cur][ne]), node, dst, result)
            path.pop()



def key_path(matrix):

    # finding nodes
    node = {}
    node_pos = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] not in ['0', '1']:
                node[matrix[i][j]] = {}
                node_pos[matrix[i][j]] = (i, j)

    # 2. finding edges of nodes
    for n in node.keys():
        node[n] = get_edges(matrix, n, node_pos[n], node.keys())


    # 3. shortest path
    result = [sys.maxsize, []]
    shortest_path(["s"], 0, node, "e", result)
    path = result[1]
    #print(path)

     # total path
    total_path = [node_pos["s"]]
    for i in range(1, len(path)):
        total_path += node[path[i - 1]][path[i]]

    print(total_path)
    #return path
    #return total_path



key_path(matrix)
