from game.models import Player, Room
from util.generate_world import World

w = World()
num_rooms = 100
width = 10
height = 10
w.generate_rooms(width, height, num_rooms)
w.print_rooms() 