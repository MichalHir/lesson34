class Animal:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sounds(self):
        pass

class Dog(Animal):
    def __init__(self, name, age,is_pure):
        super().__init__(name, age)
    #     self.type = "dog"
        self.is_pure = is_pure
    def make_sounds(self):
        return "woff"

class cat(Animal):
    def __init__(self, name, age,ear_cut):
        super().__init__(name, age)
        # self.type = "cat"
        self.ear_cut = ear_cut
    def make_sounds(self):
        return "meow"
    def is_sterilized(self):
        return self.ear_cut

class StreetCat(cat):
    def make_sounds(self):
        return "differen meow"

        