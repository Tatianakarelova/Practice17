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

element =(5)
def binary_n(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_n(array, element, left, middle - 1)
    else:
        return binary_n(array, element, middle + 1, right)

array = [i for i in range(0, 10)]

print(element,"Позиция элемента")


