print("Введите вид вашего животного")
animal_specials = input()
print("Укажите возраст вашего питомца?")
animal_age = input()
print("Как зовут вашего любимца?")
animal_name = input()
years = []
if animal_age[-1] == 1:
    years = 'год'
elif animal_age[-1] == 2 or animal_age[-1] == 3 or animal_age[-1] == 4:
    years = 'года' 
else:
    years = 'лет'
print('Это', animal_specials, 'по кличке', animal_name + '.', 'Возраст:', animal_age, years + '.')