import sys
input=sys.stdin.readline
h,m=input().split()
h,m=int(h),int(m)
if m<45:
    h-=1
    m+=15
    if h==-1:
        h=23
else:
  m-=45

print(h ,m)  