x = int(input()) #минимальная сумма инвестиций
mike = int(input()) #количество денежных средств Майкла
ivan = int(input()) #количество денежных средств Ивана

if (mike >= x) and (ivan >= x):
    print('2')
elif (mike >= x) and (ivan <= x):
    print('Mike')
elif (mike <= x) and (ivan >= x):
    print('Ivan')
else:
    if mike + ivan >= x:
        print(1)
    else:
        print(0)

