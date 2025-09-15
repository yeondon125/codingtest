import sys
input = sys.stdin.readline

a,b= input().split()
a,b = int(a), int(b)
c = list(map(int, input().split()))
for i in range(a) :
  if b > c[i] :
    print(c[i])