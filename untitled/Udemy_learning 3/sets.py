"""

farm_animals = {"cow", "buffalo", "sheep", "hen"}
for animals in farm_animals:
    print(animals)
print ("="*40)

wild_animals = set(["tiger", "lion", "zebra", "jaguar"])
for animals in wild_animals:
    print (animals)

farm_animals.add("special")
wild_animals.add("special")
print (farm_animals)
print (wild_animals)

i_tera = iter(farm_animals)
print (i_tera)
print (next(i_tera))
while True:
    print (next(i_tera))
# for i in i_tera:
#     print (next(i_tera))

"""
"""
# union and intersection
Set_A = set(range(0, 20, 2))
print (Set_A)
print (len(Set_A))

Squares = (4, 6, 9, 16, 25)
Set_B = set(Squares)
print (Set_B)
print (len(Set_B))

print ("=" * 40)
print ("A union B")
print (Set_A.union(Set_B))
print (len(Set_A.union(Set_B)))

print ("=" * 40)
print ("A intersection B")
print (Set_A.intersection(Set_B))
print (len(Set_A.intersection(Set_B)))
"""
# subsTraction
"""
Set_A = set(range(0, 40, 2))
print (sorted(Set_A))

Squares = (4, 6, 9, 16, 25, 30)
Set_B = set(Squares)
print (sorted(Set_B))

print("-" * 40)
print (sorted(Set_A.difference(Set_B)))

print("-" * 40)
print (sorted(Set_B.difference(Set_A)))
"""

# {upaDated SuBsTrAction}

"""
Set_A = set(range(0, 40, 2))
print (sorted(Set_A))

Squares = (4, 6, 9, 16, 25, 30)
Set_B = set(Squares)
print (sorted(Set_B))

print ("-" * 40)
Set_A.difference_update(Set_B)
print (sorted(Set_A))
print (sorted(Set_A.symmetric_difference(Set_B)))
Set_A.difference_update(Set_B)
print (sorted(Set_A))

"""
# {DisCard and REmoVe}
"""
Set_A = set(range(0, 40, 2))
print (sorted(Set_A))

Set_A.discard(12)
print (sorted(Set_A))

print("="*80)
Set_A.remove(6)
print(sorted(Set_A))

if 2 in Set_A:
    Set_A.remove(2)
    print(sorted(Set_A))

"""

# subset and Superset
"""

Set_A = set(range(0, 20, 2))
print (Set_A)
print (len(Set_A))

Squares = (4, 6, 10, 14)
Set_B = set(Squares)
print (Set_B)
print (len(Set_B))

print ("="*40)

if Set_B.issubset(Set_A):
    print("Set_B is subset of Set_A")
else:
    print("Set_B is not subset of Set_A")

if Set_A.issuperset(Set_B):
    print("Set_B is superset of Set_A")
else:
    print("Set_B is not superset of Set_A")
"""
