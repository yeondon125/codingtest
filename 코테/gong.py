
import math

def lcm(a,b):
    return a * b // math.gcd(a, b)

def solution(numbers):
    answer = 0
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result