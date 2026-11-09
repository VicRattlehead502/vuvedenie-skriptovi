n = int(input())
sum = 0

while n <= 0:
    n = int(input())

for char in str(n):
    sum += int(char)

pal = str(n)[::-1]

print("Сума", sum)
print("Обърнато", pal)

if pal == str(n):
    print("Палиндром е")
else:
    print("Не е палиндром")