class Person:
    def __init__(self, name: str, age: int, height: int) -> None:
        self.name = name
        self.age = age
        self.height = height

    def say_hello(self) -> None:
        print(f"Hello {self.name}")

    def get_data(self) -> dict:
        data = {"name": self.name, "age": self.age, "height": self.height}
        return data


class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def get_name(self):
        return self.name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


dog = Dog(name="Bello")
print(dog.speak())
print(dog.get_name())

# peter = Person(name="Peter", age=19, height=180)
# peter.say_hello()
# print(peter.get_data())
