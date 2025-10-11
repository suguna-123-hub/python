a = 15
b = 25
c = 20

if (a >= b and a <= c) or (a <= b and a >= c):
    second = a
elif (b >= a and b <= c) or (b <= a and b >= c):
    second = b
else:
    second = c

print("Second biggest:", second)
