from Rooms import Room

class Player:

    def __init__(self, name: str) -> None:
        self.name = name
        self.location = Room.rooms_list[0]["room_obj"]
        self.health: int = 2

    def look_around(self) -> str:
        print(f"{self.name} in the {self.location}.")

    def play(self):
        inputs: dict = {}
        check_list: list = []
        for i, door in enumerate(self.location.get_doors()):
            inputs[str(i)] = door.entrance(self.location)
            print(f"Press '{i}' for move to {door.entrance(self.location)}")
            check_list = list(range(len(self.location.get_doors())))
        user_in = input('Make a choise: ')
        if user_in.isdigit() and int(user_in) in check_list:
            self.location = inputs.get(user_in)
        else:
            print('Incorrect input, please try again: ')
        print(f"{self.name} enter the {self.location}.")
