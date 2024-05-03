def fact(num):
    fact_num = 1
    for i in range(2, num + 1):
       fact_num *= i
    return fact_num

num = int(input('Введите число, факториал которого вы хотите узнать: '))
          
fact_num = fact(num)

def fact_list(num):
    fact_list = []
    for i in range(num, 0, - 1):
        fact_list.append(fact(i))
    return fact_list

print(fact_list(fact_num))