x = int(input())

cnt_divisors = 0

for i in range(1, x + 1):
    if x % i == 0:
        cnt_divisors += 1

print(cnt_divisors)