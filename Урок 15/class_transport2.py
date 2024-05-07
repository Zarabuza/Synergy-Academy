class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров."

class Autobus(Transport):
    def seating_capacity(self, capacity = 50):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров."
        

car1 = Transport('Volkswagen', 220, 34600)
car2 = Autobus('Iveco', 100, 65782)

print(car1.seating_capacity(5))
print(car2.seating_capacity())