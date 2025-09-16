a=10
b=10
while True:
  a,b = input().split()
  a,b = int(a), int (b)
  if a!=0 and b !=0 :
    print(a+b)
  else : break