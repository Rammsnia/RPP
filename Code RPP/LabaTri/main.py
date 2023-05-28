from pathlib import Path
import csv

def count_files():
    folder_name = input("Введите путь директории: ")
    folder = Path(folder_name)
    if folder.is_dir():
        folder_count = len([1 for file in folder.iterdir()])

    print(f"В директории {folder_name} имеется {folder_count} объектов.")


def full_csv(thedict):
    key_input = input('Введите первичный ключ: ')
    number_input = input('Введите номер столовой: ')
    name_inp = input('Введите название столовой: ')
    count_dish_inp = input('Введите количество блюда в граммах: ')
    rep_time_inp = input('Введите время замены блюда в формате (ЧЧ:ММ:СС):  ')
    rest_inp = input('Введите остаток блюда в граммах: ')

    thedict[key_input] = [number_input, name_inp, count_dish_inp, rep_time_inp, rest_inp]
    with open('data.csv', 'w') as f:
        for elem in thedict:
            f.write(elem + "," + thedict[elem][0] + "," + thedict[elem][1] + ",   " + thedict[elem][2] + ",   " + thedict[elem][3] +
                    "," + thedict[elem][4] + "\n")
    f.close()

def sort_num(thedict):
    print("Сортировка словаря по номеру столовой:")
    for elem in sorted(thedict.items(), key=lambda x: int(x[1][2])):
        print(elem[0], *elem[1])
    print("")


def sort_str(thedict):
    print("Сортировка словаря по названию столовой:")
    for elem in sorted(thedict.items(), key=lambda x: x[1][1]):
        print(elem[0], *elem[1])
    print("")


def write(thedict):
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            thedict[line[0]] = line[1:]


def sort_dict_name(thedict):
    print("Строки, в которых имя товара 'aqua': ")
    for elem in thedict:
        if thedict[elem][1] == 'aqua':
            print(elem, *thedict[elem])



if __name__ == '__main__':
    thedict = {}
    count_files()
    write(thedict)

    print("Ключ, Номер столовой, Название столовой, Кол-во блюда, Время замены блюд, Остаток")
    for elem in thedict:
        print(elem, *thedict[elem])
    print("\n")

    sort_num(thedict)
    sort_str(thedict)
    sort_dict_name(thedict)

    check = input('Add newline to file? Enter y/n: ')
    if check == 'y':
        full_csv(thedict)
        print("Данные успешно сохранены!")
    else:
        print("Программа остановлена")
