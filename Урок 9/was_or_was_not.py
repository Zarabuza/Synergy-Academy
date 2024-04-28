numbers = input().split()

tmp = set()

for el in numbers:
    if el in tmp:
        print('YES')
    else:
        print('NO')
        tmp.add(el)
