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
matrix=loadMaze("Maze4.txt")

def get_path(prev, i, j):
    path = []
    path.append((i, j))
    while prev[i][j] != (-1, -1):
        i, j = prev[i][j]
        path.append((i, j))
    path.pop()  # removing source index
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


def shortest_path1(path, cost, node, dst, result):

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
            shortest_path1(path, cost + len(node[cur][ne]), node, dst, result)
            path.pop()

def shortest_path2(path, cost, node, dst, result):

    if path[-1] == dst:
        print(path, cost)
        if cost < result[0]:
            result[0] = cost
            result[1] = path[:]
        return
    cur = path[-1]
    for ne in node[cur].keys():
        if ne not in path:
            if (ord("d") <= ord(ne) <= ord("d") and
                    chr(ord(ne) - ord("d") + ord("c")) not in path):
                continue
            next_cost = cost + len(node[cur][ne])
            if next_cost >= result[0]:
                continue
            path.append(ne)
            shortest_path2(path, cost + len(node[cur][ne]), node, dst, result)
            path.pop()

def shortest_path3(path, cost, node, dst, result):

    if path[-1] == dst:
        print(path, cost)
        if cost < result[0]:
            result[0] = cost
            result[1] = path[:]
        return
    cur = path[-1]
    for ne in node[cur].keys():
        if ne not in path:
            if (ord("g") <= ord(ne) <= ord("g") and
                    chr(ord(ne) - ord("g") + ord("f")) not in path):
                continue
            next_cost = cost + len(node[cur][ne])
            if next_cost >= result[0]:
                continue
            path.append(ne)
            shortest_path3(path, cost + len(node[cur][ne]), node, dst, result)
            path.pop()

def shortest_path4(path, cost, node, dst, result):

    if path[-1] == dst:
        print(path, cost)
        if cost < result[0]:
            result[0] = cost
            result[1] = path[:]
        return
    cur = path[-1]
    for ne in node[cur].keys():
        if ne not in path:
            if (ord("i") <= ord(ne) <= ord("i") and
                    chr(ord(ne) - ord("i") + ord("h")) not in path):
                continue
            next_cost = cost + len(node[cur][ne])
            if next_cost >= result[0]:
                continue
            path.append(ne)
            shortest_path4(path, cost + len(node[cur][ne]), node, dst, result)
            path.pop()

def key_path(matrix):

    # finding all nodes
    node = {}
    node_pos = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] not in ['0', '1']:
                node[matrix[i][j]] = {}
                node_pos[matrix[i][j]] = (i, j)

    # finding edge of nodes
    for n in node.keys():
        node[n] = get_edges(matrix, n, node_pos[n], node.keys())


    # shortest path
    result1 = [sys.maxsize, []]
    result2 = [sys.maxsize, []]
    result3= [sys.maxsize, []]
    result4= [sys.maxsize, []]
    result5= [sys.maxsize, []]

    shortest_path1(["s"], 0, node, "a", result1)
    path1 = result1[1]
    #print(path1)
    shortest_path2(["a"], 0, node, "c", result2)
    path2 = result2[1]
    #print(path2)
    shortest_path3(["c"], 0, node, "f", result3)
    path3 = result3[1]
    #print(path3)
    shortest_path4(["f"], 0, node, "i", result4)
    path4 = result4[1]
    #print(path4)
    shortest_path4(["i"], 0, node, "e", result5)
    path5 = result5[1]
    #print(path5)

    path= list(itertools.chain(path1,path2,path3,path4,path5))

    #  # combine path
    total_path1 = [node_pos["s"]]
    for i in range(1, len(path1)):
        total_path1 += node[path1[i - 1]][path1[i]]
    total_path2 = [node_pos["a"]]
    for i in range(1, len(path2)):
        total_path2 += node[path2[i - 1]][path2[i]]
    total_path3 = [node_pos["c"]]
    for i in range(1, len(path3)):
        total_path3 += node[path3[i - 1]][path3[i]]
    total_path4 = [node_pos["f"]]
    for i in range(1, len(path4)):
        total_path4 += node[path4[i - 1]][path4[i]]
    total_path5 = [node_pos["i"]]
    for i in range(1, len(path5)):
        total_path5 += node[path5[i - 1]][path5[i]]

    total_path=list(itertools.chain(total_path1,total_path2,total_path3,total_path4,total_path5))

    print(path)
    print(total_path)
    #print(path)
    #return path
    #return total_path




key_path(matrix)
