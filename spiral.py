turn = 0
number = 1
line = 0

while True:
    try:
        n = int(input("Введите число: "))
        if not n >= 4 and n <= 1000:
            raise ValueError
        break
    except (ValueError,NameError):
        print("Некорректный ввод. Введите целое положительное число от 4 до 1000!")

print("Вы ввели:",n)
turn = n+n-1
print("Количество поворотов в спирале:",turn)
A = [[0] * n for a in range(n)]

while turn>=0:
    for c in range (line,n-line):
        A[line][c] = number
        number+=1
    turn-=1
    for c in range(1+line,n-line):
        A[c][n-1-line] = number
        number+=1
    turn -= 1
    for c in range (n-2-line,-1+line,-1):
        A[n-1-line][c] = number
        number+=1
    turn -= 1
    for c in range (n-2-line,0+line,-1):
        A[c][line] = number
        number+=1
    turn -= 1
    line+=1

print("Итоговый результат:")
for a in range(n):
    for b in range(n):
        print(A[a][b], end="\t")
    print("\n")