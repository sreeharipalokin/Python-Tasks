sample_string = "Testing a string"


length = len(sample_string) # find length
print(length)

print(sample_string[1:6]) # string slicing
print(sample_string[1:7:2]) # string slicing with steps

print(sample_string[3:-1]) # negative slicing
print(sample_string[-5:-1])
print(sample_string[::-1]) # reversing a string

print(sample_string.swapcase()) # swapping