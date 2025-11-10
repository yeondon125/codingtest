from collections import deque  # 큐 사용을 위해 import


def vlr(tree, index=1):
    if index >= len(tree) or tree[index] is None:
        return
    print(tree[index], end=' ')
    vlr(tree, 2 * index)
    vlr(tree, 2 * index + 1)

def lvr(tree, index=1):
  if index >= len(tree) or tree[index] is None:
      return
  lvr(tree, 2 * index)
  print(tree[index], end=' ')
  lvr(tree, 2 * index + 1)

def lrv(tree, index=1):
  if index >= len(tree) or tree[index] is None:
      return
  
  lrv(tree, 2 * index)
  lrv(tree, 2 * index + 1)
  print(tree[index], end=' ')

def bfs(tree):
    queue = deque()     
    queue.append(1)     
    while queue:
        index = queue.popleft()   

        if index >= len(tree) or tree[index] is None:
            continue

        print(tree[index], end=' ')

        left = 2 * index 
        right = 2 * index + 1
        queue.append(left)
        queue.append(right)



tree = [None , 'A', 'B', 'C', 'D', 'E', 'F']

print("\nvlr 탐색 결과:")
vlr(tree)

print("\nlvr 탐색 결과:")
lvr(tree)

print("\nlrv 탐색 결과:")
lrv(tree)

print("\n너비 우선 탐색 결과:")
bfs(tree)
