def height(tree, index=1):  
  if (index < len(tree) and not tree[index] is None):
       return 1 + max(height(tree, index * 2), height(tree, index * 2 + 1))
  return 0

tree = [None , 'A', 'B', 'C', 'D', 'E', None, 'a']
print("트리의 높이:", height(tree))