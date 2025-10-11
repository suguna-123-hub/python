n=int(input("how many numbers?"))
numbers=[]
for i in range(n):
    num=int(input(f"enter number{i+1}:"))
    numbers.append(num)
print("number list:",numbers)
