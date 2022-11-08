from Doors import Door


class Room:
    rooms_list = []

    def __init__(self, room_id: str, room_name: str, doors: list) -> None:
        self.room_id = room_id
        self.room_name = room_name
        self.doors = []
        self.doors_id = doors
        Room.rooms_list.append({"room_obj": self,
                                "room_id": self.room_id,
                                "room_name": self.room_name,
                                "doors_id": self.doors_id,
                                })

    def add_doors(self) -> None:
        for other_room_id in self.doors_id:
            for room in Room.rooms_list:
                if room["room_id"] == other_room_id:
                    nextroom = room["room_obj"]
                    if {self, nextroom} not in Door.doors_list:
                        door = Door(self, nextroom)
                        self.doors.append(door)
                        nextroom.doors.append(door)

    def get_room_id(self) -> str:
        return self.room_id

    def get_doors(self) -> list:
        return self.doors

    def __repr__(self) -> str:
        return self.room_name
