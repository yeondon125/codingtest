def count(tree, index=1):  
  if (index < len(tree) and not tree[index] is None):
      return 1+ count(tree, index*2) + count(tree, index*2+1)
  return 0

tree = [None , 'A', 'B', 'C', 'D', 'E', None, 'a']

print("노드의 개수:", count(tree))