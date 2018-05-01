class Cat (object):
    def __init__(self, name):
        # Constructor function sets up self with attributes
        self.name = name
        self.hp = 20
        self.well_being = 100
        self.hunger = 0
        self.number_of_legs = 4

    def meow(self):
        print(self.name + " meow")

    def sleep(self):
        if self.hp > 20:
            self.hp += 5
        print(self.name + " prrr. Your HP is now " + str(self.hp))

meowth = Cat("Skull Crusher")
meowth.meow()
meowth.sleep()

other = Cat("Princess")
other.meow()
other.sleep()
