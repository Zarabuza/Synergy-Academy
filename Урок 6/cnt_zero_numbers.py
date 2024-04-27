n = int(input())

cnt_zero = 0

for i in range(n):
    if int(input()) == 0:
        cnt_zero += 1

print(cnt_zero)