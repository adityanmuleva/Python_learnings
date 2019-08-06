# shopping_list = "egg", "bread", "carrot", "milk", "curd", "vegetables"
# bad_item=""
# for items in shopping_list:
#     if items == "milk":
#         bad_item = items
#         #break
#     else:
#         print("i can buy %s" %(items))
#
# print bad_item
"""""
family = ["aaditya", "santosh", "jay", "anita", "krishna", "arpita", "harish", "kavita"]
new_mem = ''
for i in range(0, len(family)):
    if family[i] in ["aaditya", "jay", "krishna", "arpita"]:
        new_mem += family[i]
total = new_mem
print ("your family members are : {}".format(total))
"""
number = 5
multiplier = 8
answer = 0
for i in range(0, number):
    answer += multiplier
newans = answer
print(newans)
