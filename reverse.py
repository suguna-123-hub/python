num=int(input("enter the numbers one by one"))
numbers=[]
for i in range(num):
    num=int(input(f"enter the number{i+1}"))
    numbers.append(num)
print("list:",numbers)
reversed_numbers=list(reversed(numbers))
print("list:",reversed_numbers)

