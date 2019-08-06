# def Food_items(text):
#     text = str(text)
#     atext = int(80)
#     btext = atext-len(text)// 2
#     print(" "*btext,text)
#
# #calling functions here
#
# Food_items("my name is aaditya")
# Food_items("i am in collage ")
# Food_items("some more text")
# Food_items(92)

# def adding(a, b):
#     c = a+b
#     print("a is {} and b is {} and their sun c is {}".format(a,b,c))
#
#
# adding(3, 5)
# adding(9, 12)


def testpractice(args, sep=''):
    args = str(args)
    bstr = 40-len(args)//2
    print(" "*bstr, args)


# call a function
testpractice("my name is aadiytya", sep="-")
testpractice(20)
