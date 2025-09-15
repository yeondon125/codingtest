import sys
input = sys.stdin.readline

a= input
print(1 if a%400 == 0 or (a%4 == 0 and a%100 != 0) else 0)