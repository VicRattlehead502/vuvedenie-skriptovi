a = int(input())
b = int(input())
nod = 0
og_a = a
og_b = b


if a <= 0 or b <= 0:
    print("Невалидни числа")
else:
    while(1):
        b = a % b
        if b == 0:
            nod = a
            break
        a = b

        
    

    nok = og_a * og_b / nod

    print("НОД: ", nod)
    print("НОК: ", nok)

    if nod == 1:
        print("Взаимно прости")
    else:
        print("Не са взаимно прости")



