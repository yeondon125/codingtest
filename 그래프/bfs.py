from collections import deque

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 5],
    4: [2],
    5: [2, 3]
}

visited = [False] * (len(graph) + 1)

def bfs(start):
    queue = deque([start])   
    visited[start] = True    
    
    while queue:
        node = queue.popleft()   
        print(node, end=' ')     
        
        for a in graph[node]:
            if not visited[a]:   
                visited[a] = True
                queue.append(a)  

bfs(1)

