sum_even = 0
max_uneven = 0

N = int(input())

if N <= 0:
    print("Невалиден брой")
else:
    for i in range(N):
        temp = int(input())

        if temp % 2 == 0:
            sum_even += temp

        elif temp % 2 != 0 and temp > max_uneven:
            max_uneven = temp
        elif max_uneven == 0 and temp % 2 != 0:
            max_uneven = temp

    print("Сума от четни числа", sum_even)

    if max_uneven == 0:
        print("Няма нечетни числа")
    else:
        print("Най-голямо нечетно", max_uneven)
