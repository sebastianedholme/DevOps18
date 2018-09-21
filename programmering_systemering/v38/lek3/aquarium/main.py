class Fish:
    def __init__(self, first_name, last_name="Fish", skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        return f"{self.first_name} is swimming"

    def swim_backwards(self):
        return f"{self.first_name} can swim backwards"

    def eyelids_status(self):
        if self.eyelids is False:
            print("Eyelids are closed")
        else:
            print('Closing eyelids')
            self.eyelids = False

class Shark(Fish):
    animal_type = "fish"
    location = "ocean"
    followers = 5

    def __init__(self, first_name, last_name = "Shark",
                skeleton="cartilage", eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        return f"{self.first_name} cannot swim backwards, but can sink backwards"

class Trout(Fish):
    def __init__(self, water = "freshwater"):
        self.water = water
        super().__init__(self)

class Clownfish(Fish):
    def live_with_anemone(self):
        return f"{self.first_name} is coexisting with sea anemone."

class Coral:
    def community(self):
        return "Coral lives in a community"

class Anemone:
    def protect_clownfish(self):
        return "The anemone is protecting the clownfish"

class CoralReef(Coral, Anemone):
    pass

def main():
    casey = Clownfish("Casey")
    print(casey.first_name + " " + casey.last_name)
    print(casey.swim())
    print(casey.live_with_anemone())

    sammy = Shark("Sammy")
    print(f"{sammy.first_name} {sammy.last_name}")

    terry = Trout()
    terry.first_name = "Terry"
    print(f"{terry.first_name} {terry.last_name}")
    print(terry.eyelids)
    print(terry.water)
    print(terry.swim())

    great_barrier = CoralReef()
    print(f"{great_barrier.community()} {great_barrier.protect_clownfish()}")

if __name__ == "__main__":
    main()
