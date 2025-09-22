import sys
input=sys.stdin.readline
a=int(input())

for i in range(a) :
  b=input()
  c=[0]
  for j in range(len(b)) :
    if b[j] == 'O' :
      c.append(c[j]+1)
    else :
      c.append(0)
  print(sum(c))