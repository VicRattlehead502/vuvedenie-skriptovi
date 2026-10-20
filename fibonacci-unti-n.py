n = int(input("Enter number: "))
x = 1
y = 1

while x < n and y<n:
    x = x + y 
    y = y + x
    if x<n:
        print(x)
    if y<n:
        print(y)
