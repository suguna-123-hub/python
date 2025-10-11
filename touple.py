num=int(input("enter the numbers one by one"))
numbers=[]
for i in range(num):
    num=(input(f"enter the number{i+1}"))
    numbers.append(num)
numbers_tuple = tuple(numbers)
print("List:", numbers)
print("Tuple:", numbers_tuple)
