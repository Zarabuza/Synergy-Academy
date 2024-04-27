word = input()

vowel_letters = ['a', 'e', 'o', 'u', 'i'] #Создаём список с гласными буквами для цикла for

vowel_count = 0 #счётчик гласных букв
consonant_count = 0 #счётчик согласных букв

# Считаем количество гласных и согласных букв в слове
for i in word:
    if i in vowel_letters:
        vowel_count += 1
    else:
        consonant_count += 1

print('Количество гласных букв в слове =', vowel_count, 'Количество cогласных букв в слове =', consonant_count, sep = '\n')

# Cчитаем количество вхождений каждой из гласных букв в слово. 
count_every_vowel = []
for el in vowel_letters:
  count_every_vowel.append(word.count(el))

''' 
Далее выполняем данное условие задачи: 
"А также определите количество каждой из этих гласных букв.
Если какой-то из перечисленных букв нет - Выведите False"
''' 

if 0 not in count_every_vowel:
    for i in range(len(count_every_vowel)):
      for el in range(len(vowel_letters)):
        if i == el:
          print('Количеcтво вхождений буквы', vowel_letters[el], 'в слово равно', count_every_vowel[i])
          #Сделал через вложенные циклы, чтобы не писать 5 принтов с разными буквами и разными счётчиками
else:
    print(False)
