lis = [44,68,42,33,32,40]

dic = {"Thomas":68,"Tom":32,"Jack":78}

for item in lis:
    for key,value in dic.items():
        if item == value:
            print(key)
        