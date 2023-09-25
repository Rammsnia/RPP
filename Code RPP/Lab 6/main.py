
import cherrypy
from peewee import *

db = SqliteDatabase('data_base.db')

# модель для Истории столовой


class DiningRoom(Model):
    id = AutoField()
    Name_dish = CharField()
    Amount_grams = IntegerField()
    Serving_time = TimeField()
    Rep_time = TimeField()
    Rem_dish = IntegerField()

    class Meta:
        database = db  # модель будет использовать базу данных data_dabe.db


db.create_tables([DiningRoom])  # создание таблицы в базе данных


class WebInterface(object):
    @cherrypy.expose
    def index(self):

        canteens = DiningRoom.select()  # получение объектов из базы данных

        # генерация HTML-страницы для отображения истории столовой
        html = '<head><link rel="stylesheet" href="style.css"></head>'
        html += '<body><h1>История столовой</h1>'
        html += '<table>'
        html += '<tr><th>№</th>' \
                '<th>Название блюда</th>' \
                '<th>Кол-во граммов</th>' \
                '<th>Время подачи</th>' \
                '<th>Время замены</th>' \
                '<th>Остаток</th>' \
                '<th>Изменить</th></tr>'

        for canteen in canteens:
            html += f'<tr><td>{canteen.id}</td><td>{canteen.Name_dish}</td><td>{canteen.Amount_grams}</td><td>{canteen.Serving_time}</td><td>{canteen.Rep_time}</td><td>{canteen.Rem_dish}</td>'
            html += f'<td><a href="/edit_canteen?id={canteen.id}">Изменить</a></td></tr>'

        html += '</table>'

        # форма для добавления записей
        html += '''
            <h2>Добавить истрию:</h2>
            <form method="post" action="add_history">
                <input type="text" name="name_dish" placeholder="Название блюда" required><br>
                <input type="number" name="amount_grams" placeholder="Кол-во граммов" required><br>
                <input type="time" name="serving_time" placeholder="Время подачи" required><br>
                <input type="time" name="rep_time" placeholder="Время замены" required><br>
                <input type="number" name="rem_dish" placeholder="Остаток" required><br>
                <input type="submit" value="Добавить">
            </form>
        '''

        html += '</body>'

        return html

    @cherrypy.expose
    def add_history(self, name_dish, amount_grams, serving_time, rep_time, rem_dish):
        # создание новой истории столовой
        canteen = DiningRoom(Name_dish=name_dish,
                             Amount_grams=amount_grams,
                             Serving_time=serving_time,
                             Rep_time=rep_time,
                             Rem_dish=rem_dish)
        canteen.save()


        return 'История столовой добавлена успешно.'

    @cherrypy.expose
    def edit_canteen(self, id):
        canteen = DiningRoom.get(DiningRoom.id == id)

        html = '<head><link rel="stylesheet" href="style.css"></head>'
        html += '<body>'
        html += f'<h2>Изменение истории столовой (ID: {canteen.id}):</h2>'
        html += f'<form method="post" action="update_history?id={canteen.id}">'
        html += f'<input type="text" name="name_dish" placeholder="Название блюда" value="{canteen.Name_dish}" required><br>'
        html += f'<input type="text" name="amount_grams" placeholder="Кол-во в граммах" value="{canteen.Amount_grams}" required><br>'
        html += f'<input type="time" name="serving_time" placeholder="Время подачи" value="{canteen.Serving_time}" required><br>'
        html += f'<input type="time" name="rep_time" placeholder="Время замены" value="{canteen.Rep_time}" required><br>'
        html += f'<input type="number" name="rem_dish" placeholder="Остаток" value="{canteen.Rem_dish}" required><br>'
        html += '<input type="submit" value="Обновить">'
        html += '</form>'
        html += '</body>'

        return html

    @cherrypy.expose
    def update_history(self, id, name_dish, amount_grams, serving_time, rep_time, rem_dish):
        canteen = DiningRoom.get(DiningRoom.id == id)
        canteen.Name_dish = name_dish
        canteen.Amount_grams = amount_grams
        canteen.Serving_time = serving_time
        canteen.Rep_time = rep_time
        canteen.Rem_dish = rem_dish
        canteen.save()

        return f'Посещение (ID: {canteen.id}) успешно обновлено!'


# Запуск CherryPy
cherrypy.quickstart(WebInterface())

