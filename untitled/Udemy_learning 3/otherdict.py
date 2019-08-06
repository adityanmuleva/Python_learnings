"""
my_list = ["a", "b", "c", "d"]
new_string = " hello ".join(my_list)
print (new_string)

"""
# practice challange

locations = {0: "you are sitting in front of computer learning python",
             1: "you are on the road",
             2: "you are standing at th etop of the hill",
             3: "you are inside a building, a well house for a small stream",
             4: "you are in the valley",
             5: "you are in forest"}

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

loc = 1
while True:
    available_exits = ",".join(exits[loc].keys())
    print (locations[loc])

    if loc == 0:
        break
    direction = input("available exits are : " + available_exits).upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("you cannot go in that direction")
