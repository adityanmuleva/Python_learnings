# school = {"class1": "teacher 1",
#           "class2": "teacher 2",
#           "class3": "teacher 3",
#           "class4": "teacher 4 good teacher",
#           "class5": "teacher 5",
#           "class6": "teacher 6",
#           "class7": "teacher 7"}
# # print (school)
# # print (school["class4"])
# school["class8"] = "teacher 8 bad teacher"
# # print (school["class8"])
# print(school)
# while True:
#     a = raw_input("please enter any data :")
#     if a == "quit":
#         break
#     if a in school:
#         b = school.get(a)
#         print(b)
#     else:
#         print ("we do not have "+a)
"""
for i in range(10):
    for teacher in school:
        print (teacher+" is  "+school[teacher])
    print("="*40)
"""
school = {"class1": "teacher 1",
          "class2": "teacher 2",
          "class3": "teacher 3",
          "class4": "teacher 4 good teacher",
          "class5": "teacher 5",
          "class6": "teacher 6",
          "class7": "teacher 7"}
""""
for i in sorted(school.keys()):
    print(i+"-"+school[i])
print (school.clear())
"""
# print (school)
# print (sorted(school))
# print (sorted(school.items()))
u_tuple = tuple(school.items())
print(u_tuple)

for students in u_tuple:
    club, student = students
    print (club+" is "+student)
print (dict(u_tuple))

# it have keys and values
