ip_address = input("please enter any ip : ")
segment = 1
segment_length = 0
character = ""
for character in ip_address:
    if character == '.':
        print("segment {} contains {} characters _".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1
if character != '.':
    print("segment {} contains {} characters ".format(segment, segment_length))
