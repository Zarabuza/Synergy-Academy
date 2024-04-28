
print('Вводите числа по очереди. Они попадут в первый список. Для завершения формирования списка отправьте любой символ, кроме цифры')

try:
    list_1 = []
 
    while True:
        list_1.append(int(input()))

except:
    unique_numbers_1 = set(list_1)

print('Вводите числа по очереди. Они попадут во второй список. Для завершения формирования списка отправьте любой символ, кроме цифры')

try:
    list_2 = []
 
    while True:
        list_2.append(int(input()))

except:
    unique_numbers_2 = set(list_2)


unique_numbers_total = unique_numbers_1.intersection(unique_numbers_2)

print(len(unique_numbers_total))

