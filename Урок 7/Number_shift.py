n = int(input()) 

s = [int(input()) for _ in range(n)]

print(s.pop(), *s)
