
pets = dict()
pets_tmp = dict()

def create():
    
    
    keys = ['animal_specials', 'animal_age', 'owners_name']

    questions = ['Как зовут вашего питомца? ', 'Укажите вид вашего животного ', 'Введите возраст вашего питомца ', 'Ваше имя: ']

    pets_variables = dict.fromkeys(keys)

    for i in range(4):
        if i == 0:
            animal_name = input(questions[i])
            pets_tmp[animal_name] = 0
        else:
            pets_variables[keys[i-1]] = input(questions[i])

    pets_tmp[animal_name] = pets_variables
    pets[(list(pets_tmp.keys()).index(animal_name)) + 1] = pets_tmp
    
    return pets

def get_pet(ID):
    if ID in pets:
        return True
    else:
        return False

def get_suffix(age, num):
    animal_name = list(pets[num])[num - 1]
    years_type = [] 
    
    if int(pets[num][animal_name]['animal_age']) % 10 == 1 and int(pets[num][animal_name]['animal_age']) != 11:
        years_type = 'год'
    elif int(pets[num][animal_name]['animal_age']) % 10 in [2, 3, 4] and int(pets[num][animal_name]['animal_age']) not in [12, 13, 14]:
        years_type = 'года'
    else:
        years_type = 'лет'
    
    return years_type

def read(num):
    if get_pet(num):
        animal_name = list(pets[num])[num - 1]
        print(f'Это {str(pets[num][animal_name]["animal_specials"]).lower()} по кличке "{animal_name}". Возраст питомца: {pets[num][animal_name]["animal_age"]} {get_suffix(pets[num][animal_name]['animal_age'], num)}. Имя владельца: {pets[num][animal_name]["owners_name"]}')
    else:
        read(num = int(input('Питомца с таким идентификатором не существует, попробуйте ещё раз: ')))

def update(num):
    
    if get_pet(num):
        keys = ['animal_specials', 'animal_age', 'owners_name']

        questions = ['Как зовут вашего питомца? ', 'Укажите вид вашего животного ', 'Введите возраст вашего питомца ', 'Ваше имя: ']

        pets_variables = dict.fromkeys(keys)

        pets_change = dict()

        for i in range(4):
            if i == 0:
                animal_name = input(questions[i])
                pets_change[animal_name] = 0
            else:
                pets_variables[keys[i-1]] = input(questions[i])

        pets_change[animal_name] = pets_variables
        pets[num] = pets_change
    else:
        update(num = int(input('Питомца с таким идентификатором не существует, попробуйте ещё раз: ')))

def delete(num):
    if get_pet(num):
        key = num
        if key in pets:
            del pets[key]
            print(f"Элемент с идентификатором {key} удален")
        else:
            print("Элемент не найден")
    else:
        delete(num = int(input('Питомца с таким идентификатором не существует, попробуйте ещё раз: ')))


command = input('Пожалуйста, введите одну из комманд "create", "read", "update", "delete" или "stop": ')
while command != 'stop':
    if command == 'create':
         create()
    elif command == 'read':
        read(int(input('Введите идентификатор питомца: ')))
    elif command == 'update':
        update(int(input('Введите идентификатор питомца, информацию о котором вы хотите обновить: ')))
    elif command == 'delete':
        delete(int(input('Введите идентификатор питомца, информацию о котором вы хотите удалить: ')))
    else:
        print('Проверьте правильность введённой вами команды')
        command = input('Пожалуйста, введите одну из комманд "create", "read", "update", "delete" или "stop": ')

print(pets)