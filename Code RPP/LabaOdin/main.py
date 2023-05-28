import random

# быстрая сортировка списка


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


# ручной ввод списка


def input_list():

    try:
        n = int(input("Введите количество элементов списка: "))
        arr = [int(input("Введите элемент списка: ")) for i in range(n)]
        return arr
    except ValueError:
        print("Ошибка: некорректный ввод элементов списка.")

# автоматическая генерация списка


def generate_list():
    try:
        n = int(input("Введите количество элементов списка: "))
        arr = [random.randint(0, 100) for i in range(n)]
        return arr
    except ValueError:
        print("Ошибка: некорректный ввод количества элементов списка.")


if __name__ == '__main__':
    while True:
        choice = input("Введите '1', чтобы ввести элементы списка вручную, или '2', чтобы сгенерировать список автоматически: ")
        if choice == '1':
            arr = input_list()
            break
        elif choice == '2':
            arr = generate_list()
            break
        else:
            print("Ошибка: некорректный выбор.")
    unsorted_arr = arr
    print("Неотсортированный список: ", arr)
    sorted_arr = quick_sort(arr)
    print("Отсортированный список: ", sorted_arr)
    arr.sort()
    print("Отсортированный список библиотечной функцией: ", arr)