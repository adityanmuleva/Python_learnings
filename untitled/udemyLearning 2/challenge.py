# challenge 1
"""""
menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam" "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])
for meal in menu:
    if not "spam" in meal:
        print(meal)
        for ingredient in meal:
            print(ingredient)
"""
"""

# challenge 2
string = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
get = iter(string)
print(get)
for i in string:
    print(next(get))
"""
# challange 3

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "pulling the rug"), (2, "psycho"), (3, "Mayhem"),(4, "Kentish Town wallz"))

album, artist, year, tracks = imelda
print (album)
print (artist)
print (year)

for song in tracks:
    print (song)
