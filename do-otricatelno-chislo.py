sum = 0
two_digit = 0
srednaritmetichno = 0
count = 0

while(1):
    temp = int(input())
    if temp < 0:
        break
    elif len(str(temp)) == 2:
        two_digit += 1
    sum += temp
    count += 1

srednaritmetichno = round(sum / count, 2)

print("Сума:", sum)
print("Двуцифрени числа:", two_digit)
print("Средноаритметично:", srednaritmetichno)    

