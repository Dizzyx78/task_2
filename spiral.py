turn = 0
s = 1
flag = 0

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
A = [[0] * n for i in range(n)]

while turn>=0:
    for k in range (flag,n-flag):
        A[flag][k] = s
        s+=1
    turn-=1
    for k in range(1+flag,n-flag):
        A[k][n-1-flag] = s
        s+=1
    turn -= 1
    for k in range (n-2-flag,-1+flag,-1):
        A[n-1-flag][k] = s
        s+=1
    turn -= 1
    for k in range (n-2-flag,0+flag,-1):
        A[k][flag] = s
        s+=1
    turn -= 1
    flag+=1

print("Итоговый результат:")
for i in range(n):
    for j in range(n):
        print(A[i][j], end="\t")
    print("\n")