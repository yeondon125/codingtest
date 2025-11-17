graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 5],
    4: [2],
    5: [2, 3]
}

visited = [False] * (len(graph) + 1)  
def dfs(node):
    if visited[node]:
        return
    visited[node] = True
    print(node, end=' ')
    for a in graph[node]:
        dfs(a)

dfs(1)  
