# sum of odd and even numbers
# between 15 and 35
odd=[]
even=[]
def SumOfNumbers(start,end):
    start = int(start)
    end = int(end)
    for number in range(start,end+1):
        if number %2 == 0:
            even.append(number)
        else:
            odd.append(number)

SumOfNumbers(15,35)
print(f"Sum of Odd Numbers : {sum(odd)}")
print(f"Sum of Even Numbers : {sum(even)}")

