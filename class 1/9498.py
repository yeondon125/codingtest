import sys
input = sys.stdin.readline

a= int(input())
a /= 10
if a >= 9:
    print("A")
elif a >= 8:
    print("B")
elif a >= 7:
    print("C")
elif a >= 6:
    print("D")
else:
    print("F")