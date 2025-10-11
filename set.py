n=int(input("how many numbers?"))
set1=set()
for i in range(n):
    num=int(input(f"enter number{i+1}:"))
    set1.add(num)
print("set1:",set1)
n=int(input("how many numbers?"))
set2=set()
for i in range(n):
    num=int(input(f"enter number{i+1}:"))
    set2.add(num)
print("set2:",set2)
union=set1.union(set2)
print("union:",union)
intersection=set1&set2
print("intersection:",intersection)
add_num=int(input(f"enter add number:"))
set1.add(add_num)
print(set1)
remove_num=int(input(f"enter remove number:"))
set1.remove(remove_num)
print(set1)

