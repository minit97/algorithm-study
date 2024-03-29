# ***
# 다시 풀어보기
# 다익스트라 알고리즘 복습하기!

import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()
INF = 1e9

v, e = map(int,input().split())
start = int(input())
graph = [[] for i in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))  # 시작노드, 끝노드, 거리

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])