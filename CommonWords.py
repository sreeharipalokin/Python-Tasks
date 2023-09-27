text = input("Enter text : ")

text_list = list(text.split())
dic = {}
for i in text_list:
    dic[i]=text_list.count(i)
counter=[]
for i,v in dic.items():
    counter.append(v)
    j = max(counter)

for i,v in dic.items():
    if v==j:
        print(i)
