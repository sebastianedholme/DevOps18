class Robot:
    def __init__(self, name, build_year, lk = 0.5, lp = 0.5):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp

    @property
    def condition(self):
        s = self.__potential_psychic + self.__potential_physical
        if s <= -1:
            return "I feel miserable!"
        elif s <= 0:
            return "I feel bad!"
        elif s <= 0.5:
            return "Could be worse"
        elif s <= 1:
            return "Seems to be okay!"
        else:
            return "Great!!"

x = Robot("The dude", 1981, 0.2, 0.4)
y = Robot("Sam the man", 1920, -0.9, 0.1)
print(x.condition)
print(y.condition)
