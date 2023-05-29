from pathlib import Path
import csv


class NewClass:
    # проинициализируем пустой словарь

    def __init__(self):
        self.thedict = {}

    # подсчёт количества файлов заданной директории
    def count_files(self):
        folder_name = input("Введите путь директории: ")
        folder = Path(folder_name)
        if folder.is_dir():
            folder_count = len([1 for file in folder.iterdir()])

        print(f"В директории {folder_name} имеется {folder_count} объектов.")

    def full_csv(self):
        key_input = input('Введите первичный ключ: ')
        number_input = input('Введите номер столовой: ')
        name_inp = input('Введите название столовой: ')
        count_dish_inp = input('Введите количество блюда в граммах: ')
        rep_time_inp = input('Введите время замены блюда в формате (ЧЧ:ММ:СС):  ')
        rest_inp = input('Введите остаток блюда в граммах: ')

        self.thedict[key_input] = [number_input, name_inp, count_dish_inp, rep_time_inp, rest_inp]
        with open('data.csv', 'w') as f:
            for elem in self.thedict:
                f.write(elem + "," + self.thedict[elem][0] + "," + self.thedict[elem][1] + ",   " + self.thedict[elem][2] + ",   " +
                        self.thedict[elem][3] +
                        "," + self.thedict[elem][4] + "\n")
        f.close()

    def sort_num(self):
        print("Сортировка словаря по номеру столовой:")
        for elem in sorted(self.thedict.items(), key=lambda x: int(x[1][2])):
            print(elem[0], *elem[1])
        print("")

    def sort_str(self):
        print("Сортировка словаря по названию столовой:")
        for elem in sorted(self.thedict.items(), key=lambda x: x[1][1]):
            print(elem[0], *elem[1])
        print("")

    def write(self):
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            for line in reader:
                self.thedict[line[0]] = line[1:]

    def sort_dict_name(self):
        print("Строки, в которых имя товара 'aqua': ")
        for elem in self.thedict:
            if self.thedict[elem][1] == 'aqua':
                print(elem, *self.thedict[elem])

    def add_new_record(self):
        check = input('Add newline to file? Enter Y/N: ')
        if check == 'Y':
            NewClass.full_csv(self.thedict)
            print("Данные успешно сохранены!")
        else:
            print("Программа остановлена")

    def __repr__(self):
        return repr(self.thedict)  # представление объекта в виде строки

    def __setattr__(self, name, value):
        if name != 'thedict':
            raise AttributeError(
                "Невозможно напрямую изсенить атрибуты. Используй атрибут 'thedict'")  # запрет прямого изменения атрибутов, использование 'thedict' атрибута
        else:
            super().__setattr__(name, value)

    def __getitem__(self, index):
        return self.thedict[index]  #  доступ к элементам по индексу

    @staticmethod
    def static_method():
        print('Вызван статический метод')
        pass

    @classmethod
    def class_method(cls):
        print('Вызван метод класса')
        pass

    def __iter__(self):
        return iter(self.thedict)  # Реализация итератора (__iter__)


if __name__ == '__main__':
    collections = NewClass()
    collections.count_files()
    collections.write()

    print("Ключ, Номер столовой, Название столовой, Кол-во блюда, Время замены блюд, Остаток")
    for elem in collections:
        print(elem, *collections[elem])
    print("\n")

    collections.sort_num()
    collections.sort_str()
    collections.sort_dict_name()

    collections.add_new_record()

