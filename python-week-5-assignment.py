# QUESTION 1

# Base Class
class Superhero:
    def __init__(self, hero_name, real_name, power_level):
        self.hero_name = hero_name
        self.__real_name = real_name  # Encapsulated (private)
        self.power_level = power_level

    def reveal_identity(self):
        return f"My real name is {self.__real_name}. Shhh, don't tell anyone!"

    def special_move(self):
        return f"{self.hero_name} uses a generic super move!"

# Child Class 1: Speedster
class Speedster(Superhero):
    def __init__(self, hero_name, real_name, power_level, top_speed):
        super().__init__(hero_name, real_name, power_level)
        self.top_speed = top_speed

    def special_move(self):
        return f"{self.hero_name} runs at {self.top_speed} mph, breaking the sound barrier! 💨"

# Child Class 2: Strongman
class Strongman(Superhero):
    def __init__(self, hero_name, real_name, power_level, lifting_capacity):
        super().__init__(hero_name, real_name, power_level)
        self.lifting_capacity = lifting_capacity

    def special_move(self):
        return f"{self.hero_name} lifts {self.lifting_capacity} tons with one hand! 💪"

# Let's create some heroes!
flash = Speedster("The Flash", "Barry Allen", 9000, 800)
hulk = Strongman("The Hulk", "Bruce Banner", 9500, 100)

# Interact with them
print(flash.special_move())
print(hulk.special_move())

print(flash.reveal_identity())
print(hulk.reveal_identity())


# QUESTION 2

# Base class (optional, but clean)
class Vehicle:
    def move(self):
        pass  # Just a placeholder

# Car class
class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving on the highway!")

# Plane class
class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying through the clouds!")

# Bicycle class
class Bicycle(Vehicle):
    def move(self):
        print("🚴‍♂️ The bicycle is pedaling down the trail!")

# Let's test them all
def test_vehicles():
    vehicles = [Car(), Plane(), Bicycle()]
    
    for v in vehicles:
        v.move()

if __name__ == "__main__":
    print("🎯 Vehicle Movement Simulation Starting...\n")
    test_vehicles()
