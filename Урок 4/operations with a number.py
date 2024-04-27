num = int(input())

units = num % 10
tens = num //10 % 10
hundreds = num //100 % 10
thousands = num //1000 % 10
tens_of_thousands = num // 10000



print(tens ** units * hundreds / (tens_of_thousands - thousands))