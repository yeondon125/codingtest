a=[0]*10
n=['0','1','2','3','4','5','6','7','8','9']
b=int(input())
c=int(input())
d=int(input())

e=b*c*d

for i in str(e):
  for j in n:
    if i==j:
      a[int(j)]+=1

for k in a:
  print(k)