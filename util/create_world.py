from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

r_outside = Room(title="Outside Cave Entrance",
               description="North of you, the cave mount beckons")

r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
passages run north and east.""")

r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. There are exits to the south and east.""")

r_parking_lot = Room(title="Empty Parking Lot",
               description="""North of you, an light flickers inside a telephone box. To the west is the empty treasure chamber.""")

r_telephone_box = Room(title="Telephone Box", description="""An old telephone box with a neon sign flickering above it. It says 'Time is Short'. Strangely, the telephone box has a second door that opens to the east.""")

r_swoosh = Room(title="The Swoosh of Space and Time", description="""You find yourself falling through a bright tunnel of noisy light. It makes you feel queasy, but you can see an exit below you to the east and the telephone box can still be seen above you and to the west..""")

r_old_kitchen = Room(title="A Shabby Old Kitchen", description="""You land in an old kitchen, full of dusty appliances. Above you and to the west you can see the bottom of the tunnel. You probably shouldn't go back that way again. To the north and south you can see two doors.""")

r_treasure_room = Room(title="A room that formerly contained some useful items", description="""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_alley = Room(title="The back of the kitchen",
               description="You are standing in an alley-way beside several bags of rubbish. The air smells stale. North of you, the old kitchen beckons. You see a gate to the east.")

r_twelve = Room(title="Twelve", description="Another room")
r_thirteen = Room(title="Thirteen", description="Another room")
r_fourteen = Room(title="Fourteen", description="Another room")
r_fifteen = Room(title="Fifteen", description="Another room")


r_outside.save()
r_foyer.save()
r_overlook.save()
r_narrow.save()
r_treasure.save()
r_parking_lot.save()
r_telephone_box.save()
r_swoosh.save()
r_old_kitchen.save()
r_alley.save()
r_treasure_room.save()
r_twelve.save()
r_thirteen.save()
r_fourteen.save()
r_fifteen.save()

# Link rooms together
r_outside.connectRooms(r_foyer, "n")
r_foyer.connectRooms(r_outside, "s")

r_foyer.connectRooms(r_overlook, "n")
r_overlook.connectRooms(r_foyer, "s")

r_foyer.connectRooms(r_narrow, "e")
r_narrow.connectRooms(r_foyer, "w")

r_narrow.connectRooms(r_treasure, "n")
r_treasure.connectRooms(r_narrow, "s")

r_treasure.connectRooms(r_parking_lot, "e")
r_parking_lot.connectRooms(r_treasure, "w")

r_parking_lot.connectRooms(r_telephone_box, "n")
r_telephone_box.connectRooms(r_parking_lot, "s")

r_telephone_box.connectRooms(r_swoosh, "e" )
r_swoosh.connectRooms(r_telephone_box, "w" )

r_swoosh.connectRooms(r_old_kitchen, "e")
r_old_kitchen.connectRooms(r_swoosh, "w")

r_old_kitchen.connectRooms(r_treasure, "n")
r_treasure.connectRooms(r_old_kitchen, "s")

r_alley.connectRooms(r_old_kitchen, "n")
r_old_kitchen.connectRooms(r_alley, "s")

r_alley.connectRooms(r_twelve, "e")
r_twelve(r_alley, "w")

r_twelve.connectRooms(r_thirteen, "n")
r_thirteen.connectRooms(r_twelve, "s")

r_thirteen.connectRooms(r_fourteen, "w")
r_fourteen.connectRooms(r_thirteen, "e")

r_fourteen.connectRooms(r_fifteen, "n")
r_fifteen.connectRooms(r_fourteen, "s")



players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()
