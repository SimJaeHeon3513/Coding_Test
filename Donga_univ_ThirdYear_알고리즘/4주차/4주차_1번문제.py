def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(reversed(graph[node]))
    return visit[-1]

def bfs(graph, start_node):
    visit = list()
    queue = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)

        if node not in visit:
            visit.append(node)

            if node in graph:
                queue.extend(sorted(graph[node]))
    return visit[-1]

from collections import defaultdict

t = int(input())
for i in range(t):
    degree, edge = map(int, input().split())

    graph = defaultdict(list)

    for _ in range(edge):
        ind, outd = map(int, input().split())
        graph[ind].append(outd)
        graph[outd].append(ind)

    for key in graph:
        graph[key].sort()

    data = list(map(int, input().split()))
    start_case = data[0]
    start_list = data[1:]

    print(f"Test Case: #{i+1}")
    for s in start_list:
        print(f"start:{s} ", f"DFS:{dfs(graph, s)} ", f"BFS:{bfs(graph, s)} ")