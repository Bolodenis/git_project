class Vehicle:
    def __init__(self, model, origin):
        self.model = model
        self.origin = origin

    def character(self):
        return f"Vehicle of model {self.model} from {self.origin}."

class Rich(Vehicle):
    def __init__(self, salary, age, model, origin):
        super().__init__(model, origin)
        self.salary = salary
        self.age = age
    def describe(self):
        super().character()
        print(f"People who earn {self.salary} of {self.age} age qualify to drive {self.character()}")
user = Rich(45000, 37, "premio", "German")
print(user.model)
print(user.character())
user.describe()
