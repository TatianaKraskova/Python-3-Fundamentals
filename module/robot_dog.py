from module.robot import Robot


class Robot_Dog(Robot):
    def make_noise(self):
        print('Woof Woof!')

    def fetch(self, item):
        print(f"{self.name} is fetching the {item}!")

    def sit(self):
        print(f"{self.name} is sitting!")

    def roll_over(self):
        print(f"{self.name} rolled over!")
