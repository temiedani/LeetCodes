from unicodedata import name


class Human:
    def __init__(self, name, occupation) -> None:
        self.name = name
        self.occupation = occupation

    def do_work(self):
        return print(f"the occupation is {self.occupation}")

    def whats_name(self):
        return print(f"the name is {self.name}")  



class Studet(Human):
    def __init__(self,name,occupation,age) -> None:
        super().__init__(name,occupation)
        self.age=age

tom = Studet("temie", "SWE",12)

tom.do_work()
tom.whats_name()

print(dir(tom))