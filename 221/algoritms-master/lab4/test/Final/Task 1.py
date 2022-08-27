from queue import PriorityQueue
import math


def Dijkstra(adj_list, source):
    queue = PriorityQueue()
    isVisited = [False] * len(adj_list)
    distance = [math.inf] * len(adj_list)
    distance[source] = 0
    queue.put((distance[source], source))
    while not queue.empty():
        present_node = queue.get()[1]
        if isVisited[present_node]:
            continue
        else:
            isVisited[present_node] = True
            for nodes in adj_list[present_node]: #node[0]=vertex name,  node[1]=weight between present node and node
                alt_weight = distance[present_node] + nodes[1]
                if alt_weight < distance[nodes[0]]:
                    distance[nodes[0]] = alt_weight
                    queue.put((distance[nodes[0]], nodes[0]))

    return distance[len(adj_list) - 1]


f = open("Task 1 input.txt", "r")
T = int(f.readline())
g = ""
for i in range(T):
    vertices, edges = f.readline().split()
    vertices = int(vertices)
    edges = int(edges)
    adj_list = [[] for x in range(vertices+1)]
    for j in range(edges):
        u, v, w = f.readline().split()
        u, v, w = int(u), int(v), int(w)
        adj_list[u].append([v, w])
    print(adj_list)
    j = []
    a = [str((Dijkstra(adj_list, 1)))]
    j.append(a)
    for i in j:
        for k in i:
            g += k + " "
b = open("Task 1 output.txt", "w")
for i in g:
    b.write(i)
b.close()

