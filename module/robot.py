class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0, 0]
        print('My name is', self.name)

    def walk(self, x):
        self.position[0] = self.position[0] + x
        print('New position:', self.position)

class Robot_Dog(Robot):
    def make_noise(self):
        print('Woof Woof!')

    def fetch(self, item):
        print(f"{self.name} is fetching the {item}!")

    def sit(self):
        print(f"{self.name} is sitting!")

    def roll_over(self):
        print(f"{self.name} rolled over!")

# Main program
my_robot_dog = Robot_Dog('Bud')

# Call methods on the Robot_Dog instance
my_robot_dog.make_noise()  # Output: Woof Woof!
my_robot_dog.walk(5)       # Output: New position: [5, 0]
my_robot_dog.fetch('ball') # Output: Bud is fetching the ball!
my_robot_dog.sit()         # Output: Bud is sitting!
my_robot_dog.roll_over()   # Output: Bud rolled over!
