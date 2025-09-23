a,b,c=1,1,1
while(1):
  a,b,c=input().split()
  a,b,c=int(a),int(b),int(c)
  if(a==0 and b==0 and c==0):
    break
  if(max(a,b,c)**2==a**2+b**2+c**2-max(a,b,c)**2):
    print("right")
  else:
    print("wrong")