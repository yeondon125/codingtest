import sys
input=sys.stdin.readline
d=[]
n=int(input())
for i in range(n):
  a,b = input().split()
  a,b=int(a),str(b)
  d.append((a,b))
d=sorted(d,key=lambda x:(x[0]))
for age, name in d:
  print(age,name)