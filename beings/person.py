from typing import Collection

class Person:
    def __init__(self, name: str, age: int, *, hobbies: Collection[str] | None = None) -> None:
        self.name = name
        self.age = age
        self.hobbies = hobbies if hobbies is not None else []

    @property
    def first_name(self) -> str:
        return self.name.split()[0]
    
    @property
    def last_name(self) -> str:
        return self.name.split()[-1]
    
    def celebrate_birthday(self) -> None:
        self.age += 1

    def add_hobby(self, hobby: str) -> None:
        self.hobbies.append(hobby)

    # def greet(self) -> str:
    #     return f"Hello, my name is {self.name} and I am {self.age} years old."