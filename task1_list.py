n=int(input("how many numbers?"))
numbers=[]
for i in range(n):
    num=int(input(f"enter number{i+1}:"))
    numbers.append(num)
total=sum(numbers)
maximum=max(numbers)
minimum=min(numbers)
print("number list:",numbers)
print("total:",total)
print("maximum:",maximum)
print("minimum:",minimum)
