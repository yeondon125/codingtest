import math
a,b=input().split()
a,b=int(a),int(b)

print(math.gcd(a,b))
print((a*b)//math.gcd(a,b))
