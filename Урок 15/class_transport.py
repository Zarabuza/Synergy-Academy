class Transport:

    def __init__(self, name, max_speed, mileage):
       self.name = name
       self.max_speed = max_speed
       self.mileage = mileage

    def display_info(self):
       print(f'Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}')

autobus = Transport('Renault Logan', 180, 12)

taxi = Transport('Kia Rio', 230, 54690)

autobus.display_info()
taxi.display_info() 
