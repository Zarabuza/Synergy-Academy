class Turtle():

    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self, plus = 1):
        self.s += plus

    def degrade(self, minus = 1):
        if self.s - minus > 0:
            self.s -= minus
        else:
            print('Шаг не может быть меньше единицы.')

    def count_moves(self, x2, y2):
        res = abs(self.x - x2)/self.s + abs(self.y - y2)/self.s
        print(res)

turtle_1 = Turtle(-2, -2, 1)
turtle_1.go_up()
turtle_1.go_down()
turtle_1.go_left()
turtle_1.go_right()
turtle_1.evolve()
turtle_1.degrade()
turtle_1.count_moves(-3, 2)

print(turtle_1.__dict__)

