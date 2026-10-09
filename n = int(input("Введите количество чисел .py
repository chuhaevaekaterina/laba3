n = int(input("Введите количество чисел N: "))
target = int(input("Введите число для посика: "))
count = 0
print(f"Введите {n} чисел последовательности:")
for i in range(n):
    num = int(input())
    if num == target:
        count += 1
print(f"Количество элементов, совпадающих с {target}: {count}")        