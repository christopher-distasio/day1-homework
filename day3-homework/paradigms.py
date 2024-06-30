class Podracer:
    
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"


Anakin_Skywalker = Podracer(200, "trashed", 500)

print(Anakin_Skywalker.repair())

print(Anakin_Skywalker.condition)

