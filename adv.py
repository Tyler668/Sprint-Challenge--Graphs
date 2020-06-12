from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "C:\\Users\\tyler\\Documents\\github\\Sprint-Challenge--Graphs\\maps\\main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
traversal_path = []

# Where have I been, what direction must I go to get to my previous room?
travelRecord = []
# Determine the direction to backtrack given the direction you traveled
inverseDirections = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# Visited is a dict of each room id and its immediately available paths
visited = {}
# Initiate by visiting the first room, in this case, room 0
visited[player.current_room.id] = player.current_room.get_exits()

# Keep going while there are still rooms we haven't visited
# While the list of unique rooms we've been to is less than the list of total rooms
while len(visited.keys()) < len(room_graph):
    # If not in visited, add it and set its value to that room's available paths
    if player.current_room.id not in visited:
        visited[player.current_room.id] = player.current_room.get_exits()
        previousRoom = travelRecord[-1]
        # Remove the direction from which you came from the running, it doesn't count as a possible new direction
        visited[player.current_room.id].remove(previousRoom)
    # If there are no available paths, then you hit a dead end, therefore travel in the reverse direction
    if len(visited[player.current_room.id]) == 0:
        previousRoom = travelRecord[-1]
        travelRecord.pop()
        traversal_path.append(previousRoom)
        # Make the player turn back
        player.travel(previousRoom)
    # If the current room is in the visited dict, pop each available new room off the dict entry's list of possible paths
    else:
        nextRoom = visited[player.current_room.id][-1]
        visited[player.current_room.id].pop()
        traversal_path.append(nextRoom)
        # In doing so, keep a record of where you'd have to travel to get back to the room you were just in.
        travelRecord.append(inverseDirections[nextRoom])
        # Move onward to the next available path
        player.travel(nextRoom)

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

# bfs(494, )
# print('Cur room')
