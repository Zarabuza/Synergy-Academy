pets_variables = ['animal_specials', 'animal_age', 'owners_name']

pets = dict()

questions = ['Как зовут вашего любимца?', 'Укажите вид вашего животного', 'Введите возраст вашего питомца', 'Ваше имя']

for i in range(4):
    if i == 0:
        answer = input(questions[i])
        pets[answer] = 0
    else:
        pets_variables =(i, input(questions[i]))


def сonvert_list_to_dict(list):
    res_dct = {list[i]: list[i + 1] for i in range(0, len(list), 2)}
    return res_dct

pets[answer] = сonvert_list_to_dict(pets_variables)

years_type = []
if animal_age == 1:
    years_type = 'год'
elif animal_age == 2 or animal_age[-1] == 3 or animal_age[-1] == 4:
    years_type = 'года' 
else:
    years_type = 'лет'

print(f'Это {animal_specials} по кличке {animal_name}. Возраст питомца: {animal_age} {years_type}.'
f'Имя владельца: {owners_name}')