char_list = []
word_list = []

list1_size = int(input("Enter number of elements in list 1 : "))
for value in range(list1_size):
    item = input("Item : ")
    char_list.append(item)

list2_size = int(input("Enter number of elements in list 2 : "))
for value in range(list2_size):
    item = input("Item : ")
    word_list.append(item)

dict = {}

if len(char_list)>len(word_list):
    max_range = len(word_list)
    for i in range(max_range):
        key = char_list[i]
        dict[key]=word_list[i]

elif len(char_list)<len(word_list):
    max_range = len(char_list)
    for i in range(max_range):
        key = char_list[i]
        dict[key]=word_list[i]

else:
    max_range = len(char_list)
    for i in range(max_range):
        key = char_list[i]
        dict[key]=word_list[i]

print(dict)
    