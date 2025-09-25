import sys
import statistics
input=sys.stdin.readline
n=int(input())
a=[]
for i in range(n):
  a.append(int(input()))
  

print(round(sum(a)/n))
a.sort()
print(ａ[n//2] )
modes = statistics.multimode(a)
modes.sort()
if len(modes) > 1:
    print(modes[1]) 
else:
    print(modes[0])

print(max(a)-min(a))

