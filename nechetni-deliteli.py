num = int(input("Enter a number: "))
for i in range(num):
    if num%(i+1) == 0 and (i+1)%2 != 0:
        print(i+1)
