import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

start = int(input())

# a list that contains information about nodes which are connected to each node
graph = [[] for i in range(n + 1)]

# short distance table with infinity
distance = [INF] * (n + 1)

# take information about all of the edges
for _ in range(m):
    a, b, c = map(int, input().split())
    # from node a, to node b, with cost of c
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # insert in to queue while short distance to the start node is set as 0
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # while the queue is not empty
        # take out the information about the shortest distance node
        dist, now = heapq.heappop(q)
        # if the node is already processed, ignore
        if distance[now] < dist:
            continue
        # check the adjcent nodes to the current node
        for i in graph[now]:
            cost = dist + i[1]
            # in case the distance is shorter through the current node
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# print all of the short distance to each node
for i in range(1, n + 1):
    if distance[i] == INF: # if the node cannot be reached
        print("INFINITY")
    else:
        print(distance[i])
