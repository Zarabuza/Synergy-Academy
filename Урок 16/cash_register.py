class Cash_Register():

    def __init__(self, cash):
        self.cash = cash

    def top_up(self, x):
        self.cash += x

    def count_1000(self):
        thousands = self.cash // 1000
        print(f'В кассе тысячных купюр находится: {thousands} шт.')

    def take_away(self, y):
        if self.cash - y >= 0:
            self.cash -= y
        else:
            print('В кассе недостаточно денег.')

    
cr1 = Cash_Register(int(input('Денег в кассе: ')))
cr1.top_up(int(input('Добавляем в кассу: ')))
cr1.count_1000()
cr1.take_away(int(input('Берём из кассы: ')))
print(f'Денег в кассе осталось {cr1.cash}')

