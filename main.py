from Rooms import Room
from Player import Player
from Levels import LEVEL1 as level
from Enemy import Enemy
from random import randint
from Dice import Dice


rooms : list = []
win_room = level[(randint(0, len(level)-1))]

def do_maze():
    """Creates a maze"""
    for room_obj in level:
        room = Room(**room_obj)
        rooms.append(room)
    for room in rooms:
        room.add_doors()


if __name__ == "__main__":
    do_maze()
    player = Player("You")
    enemy = Enemy(rooms)
    dice = Dice()
    print(f"{player.name} have entered the Maze.")
    print(f"{player.name} have {player.health} HP.")
    player.look_around()
    while True:
        enemy.run(rooms)
        player.play()
        if player.location.get_room_id() == enemy.location.get_room_id():
            print(f'Oh, {enemy.name} here.')
            if dice.throw() < 10:
                player.health -= 1
                print(f"{player.name} HP: {player.health}!")
            if player.health == 0:
                print(f"{player.name} LOOOOOSE!Game OVER!")
                break
        elif player.location.get_room_id() == win_room["room_id"]:
            print(f"{player.name} leave from the maze! You won!")
            break
