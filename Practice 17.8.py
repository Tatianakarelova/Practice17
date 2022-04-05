array = [9, 5, 4, 3, 2, 1]
while True:
    try:
        n = int(input("Введите любое целое число"))
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова: ")

array.append(n)
for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)


