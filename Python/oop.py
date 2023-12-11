class Person:
    def __init__(self, name: str, age: int, height: int) -> None:
        self.name = name
        self.age = age
        self.height = height

    def say_hello(self):
        print(f"Hello {self.name}")


peter = Person(name="Peter", age=19, height=180)
peter.say_hello()
