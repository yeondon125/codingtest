import sys
input=sys.stdin.readline
m=[-1]*26
n=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

a=input()

for i in a:
  for idx, j in enumerate(n):
    if i==j and m[idx]==-1:
      m[idx]=a.index(i)

for k in range(len(m)):
  print(m[k], end=' ')