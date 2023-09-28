text = input("Enter text : ")

text_list = list(text.split(","))
dic = { item:text_list.count(item) for item in text_list }
for key,value in dic.items():
    if value > 1:
        print(f"{key}:{value}")

