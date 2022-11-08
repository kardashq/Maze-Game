from random import choice


class Enemy:
    def __init__(self, rooms: list) -> None:
        self.name = "OMONOVEC"
        self.location = choice(rooms)

    def run(self, rooms) -> None:
        print(f"{self.name} in {self.location}")
        self.location = choice(rooms)


