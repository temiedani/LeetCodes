# class Person:
#     home = "earth"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def getName(self):
#         print(f"your name is {self.name}")


# x = Person("Temie", 11)
# x.getName()
# print(x.home)

# parent class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class


class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

    def xx(self):
        super().swim()


peggy = Penguin()
# peggy.whoisThis()
# peggy.swim()
# peggy.run()
peggy.xx()
