def search(tree, value):
    index=1
    node = tree[index]
    while node is not None:
      if value == node:
        return True
      elif value < node:
        index = index * 2
      else:
        index = index * 2 + 1
      if index >= len(tree):
        break
      node = tree[index] 
    return index