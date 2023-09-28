size = int(input("Enter size : "))
sample_list = []
for position in range(size):
    item = input("Item : ")
    sample_list.append(item)

result = []
for position in range(1,size,2):
    result.append(sample_list[position])
   
print(result)    