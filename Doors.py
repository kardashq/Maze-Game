class Door:
    doors_list = []

    def __init__(self, room_1: object, room_2: object) -> None:
        self.room_1 = room_1
        self.room_2 = room_2
        Door.doors_list.append({self.room_1, self.room_2})

    def entrance(self, now_in: object) -> object:
        return list({self.room_1, self.room_2} - {now_in})[0]

    def __repr__(self) -> str:
        return f'{self.room_1}'

