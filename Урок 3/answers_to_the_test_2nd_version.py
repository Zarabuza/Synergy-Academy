stages = []  #список с ответами студента

stages_numbers = ["первый", "второй", "третий", "четвёртый", "пятый", "шестой"] #список с номерами этапов развития человека для цикла for

#Цикл будет выполняться до тех пор, пока все ответы пользователя не будут верны, но условие сделал не через список, а через принт (было интересно сработает или нет)
while print != 'dryopithecus=>ramapithecus=>australopithecus=>homo erectus=>homo sapiens neanderthalensis=>homo sapiens sapiens':
    for i in range(6):
        print("Введите", stages_numbers[i] , "этап развития человечества")
        stages.append(input().lower()) #Сразу переводим все буквы в строке в нижний регистр, чтобы студенты могли использовать любой регистр при ответах
    print(*stages, sep = '=>')

    if stages == ['dryopithecus', 'ramapithecus', 'australopithecus', 'homo erectus', 'homo sapiens neanderthalensis', 'homo sapiens sapiens']:
        print('Поздравляем! Вы успешно сдали тест')
        break
    else:
        print('Ответ неверный. Попробуйте снова')
        stages.clear()