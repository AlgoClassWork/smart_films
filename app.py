from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit,
    QHBoxLayout, QListWidget, QPushButton,
    QVBoxLayout
)

# Создание элементов интерфейса
app = QApplication([])
window = QWidget()
window.setWindowTitle('Smart Films')

description_field = QTextEdit()

films_list = QListWidget()
films_list.addItems(['Интерстеллар', 'Семь', 'Король лев'])
add_film_btn = QPushButton('Добавить фильм')
del_film_btn = QPushButton('Удалить фильм')

genres_list = QListWidget()
genres_list.addItems(['Боевик', 'Комедия', 'Драмма'])
add_genre_btn = QPushButton('Добавить жанр')
del_genre_btn = QPushButton('Удалить жанр')
# Размещение элементов интерфейса
main_line = QHBoxLayout()
list_line = QVBoxLayout()
h1_line = QHBoxLayout()
h2_line = QHBoxLayout()
main_line.addWidget(description_field)
main_line.addLayout(list_line)
list_line.addWidget(films_list)
list_line.addLayout(h1_line)
h1_line.addWidget(add_film_btn)
h1_line.addWidget(del_film_btn)
list_line.addWidget(genres_list)
list_line.addLayout(h2_line)
h2_line.addWidget(add_genre_btn)
h2_line.addWidget(del_genre_btn)
window.setLayout(main_line)

# Запуск приложения
window.show()
app.exec()