import random


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    element = arr[0]
    left = list(filter(lambda x: x < element, arr))
    right = list(filter(lambda x: x > element, arr))
    pivot = [i for i in arr if i == element]

    return quick_sort(left) + pivot + quick_sort(right)

# проверка
# создание списка от 0 до 20

range_num = int(input("Введите количество чисел в рандомном массиве: "))
arr = [i for i in range(0, range_num)]
# перемешивание списка
random.shuffle(arr)
# вывод  перемешанного списка
print("Перемешанный список: ")
print(arr)
print("Отсортированный список: ")
print(quick_sort(arr))
print("Введите последовательность (самописная реализация): ")
# создание рандомного листа
random_list_of_nums = [int(x) for x in input().split()]
quick_sort(random_list_of_nums)
print(random_list_of_nums)
print("Введите последовательность (библиотечная функция): ")
list_nums = [int(x) for x in input().split()]
list_nums.sort()
print(list_nums)