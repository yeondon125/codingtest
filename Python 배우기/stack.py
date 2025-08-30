import sys
input = sys.stdin.readline

stack = []

def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()
    
def size():
    return len(stack)

def empty():
    if len(stack) == 0:
        return 1
    else:
        return 0
    
def top():
    if len(stack) == 0:
        return -1
    else:
        return stack[-1]

n = int(input())
result = []
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "push":
        push(int(cmd[1]))
    elif cmd[0] == "pop":
        result.append(str(pop()))
    elif cmd[0] == "size":
        result.append(str(size()))
    elif cmd[0] == "empty":
        result.append(str(empty()))
    elif cmd[0] == "top":
        result.append(str(top()))
print('\n'.join(result))