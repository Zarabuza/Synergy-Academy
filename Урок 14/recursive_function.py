my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def rec(n):
    if len(n) == 0:
        print('Конец списка')
        return
    print(n[0])
    rec(n[1:])

rec(my_list)