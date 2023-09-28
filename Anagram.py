word = "rear"
res = set()
characters = []
demo = []
for character in word:
    characters.append(character)
characters.sort()
for char1 in characters:
    
    for char2 in characters:
        
        for char3 in characters:
            
            for char4 in characters:
                demo1 = []
                demo1.append(char1)
                demo1.append(char2)
                demo1.append(char3)
                demo1.append(char4)
                demo1 = tuple(demo1)
                demo.append(demo1)
                
print(set(demo))
