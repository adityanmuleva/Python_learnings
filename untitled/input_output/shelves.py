import shelve
# wild_animal = ["lion","tiger"]
with shelve.open("Shelve_file",writeback=True) as animals:
#     animals = shelve.open("shelve_file")
#     animals["monkey"] = "likes to eat banana"
#     animals["elephant"]= "got a lot of strength"
#     animals["cow"]="gives milk"
#     animals["Wild_Animals"] = wild_animal
    animals["Wild_Animals"].append("aaditya")
    animals["Wild_Animals"].remove("aaditya")
# for key in animals:
#     print(key)
# print("*"*40)
# print(animals["cow"])
# print(animals["monkey"])

# for keys in animals:
#     print(keys+":"+animals[keys])

# while True:
#     get_input = input("please enter name of the animals :")
#     if get_input == "quit":
#         break
#
#     if get_input in animals:
#         print(get_input+" : "+animals[get_input])
#     else:
#         print("our db doesnt contains {}".format(get_input))

# for k in animals.keys():
#     print(k)
# print("*"*40)

# for i in animals.values():
#     print(i)
# print("*"*40)

# for j in animals.items():
#     print(j)
# print("*"*40)

# for h in animals:
#     print(h+" : "+animals[h])
    for all_animals in animals:
        print(all_animals,animals[all_animals])

animals.close()
