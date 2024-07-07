class Podracer:
    
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"


class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        return self.max_speed * 2    

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    def flame_jet(self, other):
        other.condition == "trash"




# Anakin_Skywalker = Podracer(200, "trashed", 500)

# print(Anakin_Skywalker.repair())

# print(Anakin_Skywalker.condition)

apod = AnakinsPod(33, "trashed", 200)

bpod = Podracer(22, "trashed", 200)

spod = SebulbasPod(22, "messed up", 344)

print(apod.max_speed, apod.condition, apod.price)

print(apod.boost())

# print(bpod.repair())

# print(bpod.condition)

print(spod.flame_jet(apod))



print(spod.flame_jet(bpod))

print(bpod.condition)


