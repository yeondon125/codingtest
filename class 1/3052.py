a=[0] * 42
for i in range(10) :
  a[(int(input()))%42] +=1

b=0
b = sum(map(lambda x: 1 if x > 0 else 0, a))
print(b)