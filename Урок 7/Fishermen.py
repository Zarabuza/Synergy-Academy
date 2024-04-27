m = int(input())
n = int(input())

fishermens_weight = [int(input()) for _ in range(n)]
fishermens_weight.sort()

cnt_boats = 0 #сюда будем записывать кол-во использованных лодок

while len(fishermens_weight) != 0:
    if len(fishermens_weight) > 1:
        if (fishermens_weight[-1] + fishermens_weight[0]) < m:
            cnt_boats += 1
            del fishermens_weight[-1]
            del fishermens_weight[0]
        else:
            cnt_boats += 1
            del fishermens_weight[-1]
    else:
        cnt_boats += 1

print(cnt_boats)