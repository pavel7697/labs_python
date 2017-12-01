
import MySQLdb

#! Открытие соединение с базой данных
db = MySQLdb.connect(
    host="localhost",
    user="dbuser",
    passwd="123",
    db="first_db"
)
db.set_character_set('utf8')
#! Получить курсор для работы с базой данных
c=db.cursor()

#! Выполнить вставку
# c.execute("insert into films (name, description) VALUES (%s, %s);", ('Аватар', 'Это наш новый дед'))
# #! Фиксирование изменений
# db.commit()

#! Выполнить выборку
c.execute("select * from teacher;")

#! Забрать все полученные записи
entries = c.fetchall()

#! Распечатать записи
for e in entries:
    print(e)

#! Закрытие курсора
c.close()
#! Закрытие соединения
db.close()