pets = dict()

keys = ['animal_specials', 'animal_age', 'owners_name']

questions = ['Как зовут вашего любимца?', 'Укажите вид вашего животного', 'Введите возраст вашего питомца', 'Ваше имя']

pets_variables = dict.fromkeys(keys)

for i in range(4):
    if i == 0:
        animal_name = input(questions[i])
        pets[animal_name] = 0
    else:
        pets_variables[keys[i-1]] = input(questions[i])

pets[animal_name] = pets_variables

years_type = [] 
if pets[animal_name]['animal_age'][-1] == '1':
    years_type = 'год'
elif pets[animal_name]['animal_age'][-1] == '2' or pets[animal_name]['animal_age'][-1] == '3' or pets[animal_name]['animal_age'][-1] == '4':
    years_type = 'года'
else:
    years_type = 'лет'

print(f'Это {pets[animal_name]["animal_specials"]} по кличке "{animal_name}". Возраст питомца: {pets[animal_name]["animal_age"]} {years_type}. Имя владельца: {pets[animal_name]["owners_name"]}')