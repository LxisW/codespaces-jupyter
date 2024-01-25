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


peter = Person(name="Peter", age=19, height=180)
peter.say_hello()
print(peter.get_data())
