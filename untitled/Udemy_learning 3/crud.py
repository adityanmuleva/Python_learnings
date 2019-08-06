# to create any dictionary use {}(json) syntax:
"""
dictionary = {"name": "aaditya muleva",
              "passion": "i do not know",
              "hobbies": "playing outdoor games",
              "collage": "IES IPS ACADEMY",
              "class":"12",
              "profession": "none"}
print(dictionary)
another_dictionary = {"name": "xyz",
                      "class": "13",

                      "school": "random public school"}
print(another_dictionary)
another_dictionary.update(dictionary)

print (another_dictionary)
"""
"""
newdict = another_dictionary
name = "harish"
print name.replace("harish", "Krishna")
"""
# delete a dictionary
"""
dictionary = {"name": "aaditya muleva",
              "passion": "i do not know",
              "hobbies": "playing outdoor games",
              "collage": "IES IPS ACADEMY",
              "class":"12",
              "profession": "none"}
print(dictionary)
another_dictionary = {"name": "xyz",
                      "class": "13",

                      "school": "random public school"}
another_dictionary.clear()
print another_dictionary
"""
# another operations
String = "this is my string"
print ("to capitalize: - ", String.upper())
String1 = "THIS IS MY ANOTHER STRING"
print ("in small letters :- ", String1.lower())
print ("to replace :- ", String1.replace("THIS IS MY ANOTHER STRING", "this is replaced string"))
String2 = iter(String1)
print (String2)
print (next(String2))
print (next(String2))
print (next(String2))
print (next(String2))
print (next(String2))
print (next(String2))