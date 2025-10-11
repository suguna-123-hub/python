num=int(input("enter the numbers one by one"))
numbers=[]
count=0
count1=0
for i in range(num):
    num=int(input(f"enter the number{i+1}"))
    numbers.append(num)
    print("list:",numbers)
    if num%2==0:
        count+=1
    else:
        count1+=1
print("even-",count)
print("odd-",count1)
                
