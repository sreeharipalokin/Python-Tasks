lis = [44,68,42,33,32,40]

dic = {"Thomas":68,"Tom":32,"Jack":78}

for i in lis:
    for j,v in dic.items():
        if i==v:
            print(j)
        