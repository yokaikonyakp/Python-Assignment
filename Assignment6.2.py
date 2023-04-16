class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def hunt(self):
        print(f"{self.name} is a Jack Russell Terrier and loves to hunt.")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def guard(self):
        print(f"{self.name} is a Bulldog and is great at guarding.")

# Creating objects and call the functions


dog1 = Dog("Whitie", 2, "White")
dog1.description()
dog1.get_info()

dog2 = JackRussellTerrier("Enzo", 2, "Blackbrown")
dog2.description()
dog2.get_info()
dog2.hunt()

dog3 = Bulldog("Milkie", 1, "Red")
dog3.description()
dog3.get_info()
dog3.guard()
