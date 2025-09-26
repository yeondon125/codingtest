import sys
input = sys.stdin.readline

def asdf(n):
    if n-n//1 >= 0.5 :
        return int(n//1+1)
    else :
        return int(n//1)
    
n=int(input())
a=[]

for i in range(n):
      a.append(int(input()))
a.sort()

if (n>3) :
  m= asdf(n*0.15) if n*0.15 > 0.5 else 1
  r=sum(a)
  for i in range(m):
      r=r-a[i]-a[n-1-i]

  print(asdf(r/(n-m*2)))


elif (n==0) : print(0)
elif (n<4) :
  print(asdf(sum(a)/n))