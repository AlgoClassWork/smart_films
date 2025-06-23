import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit,
    QHBoxLayout, QListWidget, QPushButton,
    QVBoxLayout, QLineEdit, QInputDialog
)


# --- Инициализация приложения и главного окна ---
app = QApplication([])
window = QWidget()
window.setWindowTitle('Smart Films')
window.setMinimumSize(900, 600) 

# --- Создание элементов интерфейса ---

# Поле для описания фильма
description_field = QTextEdit()
description_field.setPlaceholderText('Здесь будет отображаться описание выбранного фильма...')


# Список фильмов
films_list = QListWidget()

# Кнопки для фильмов
add_film_btn = QPushButton('Добавить фильм')
del_film_btn = QPushButton('Удалить фильм')
# Задаем фиксированную высоту для единообразия кнопок и поля ввода
add_film_btn.setFixedHeight(40)
del_film_btn.setFixedHeight(40)

# Список жанров
genres_list = QListWidget()

# Кнопки для жанров
add_genre_btn = QPushButton('Добавить жанр')
del_genre_btn = QPushButton('Удалить жанр')
# Задаем фиксированную высоту
add_genre_btn.setFixedHeight(40)
del_genre_btn.setFixedHeight(40)

# Поле поиска и кнопка
search_field = QLineEdit()
search_field.setPlaceholderText('Введите название фильма для поиска...')
search_field.setFixedHeight(40) # Фиксированная высота для поля поиска
search_btn = QPushButton('Поиск')
search_btn.setFixedHeight(40) # Фиксированная высота для кнопки поиска

# --- Размещение элементов интерфейса с помощью макетов (Layouts) ---

# Главный горизонтальный макет
main_line = QHBoxLayout()
main_line.setSpacing(30) # Увеличенный отступ между левой и правой частями

# Вертикальный макет для правой части (списки, кнопки, поиск)
list_line = QVBoxLayout()
list_line.setSpacing(15) # Отступ между элементами внутри правой панели

# Горизонтальный макет для кнопок фильмов
h1_line = QHBoxLayout()
h1_line.setSpacing(10) # Отступ между кнопками "Добавить" и "Удалить"

# Горизонтальный макет для кнопок жанров
h2_line = QHBoxLayout()
h2_line.setSpacing(10) # Отступ между кнопками "Добавить" и "Удалить"

# Добавляем элементы в главный макет
main_line.addWidget(description_field, 3) # description_field занимает 3 части ширины
main_line.addLayout(list_line, 2) # list_line (правая панель) занимает 2 части ширины

# Добавляем элементы в правую панель (list_line) с учетом растяжителей
list_line.addWidget(films_list, 4) # Список фильмов занимает 4 части высоты
list_line.addLayout(h1_line) # Добавляем макет с кнопками фильмов
h1_line.addWidget(add_film_btn)
h1_line.addWidget(del_film_btn)

list_line.addWidget(genres_list, 2) # Список жанров занимает 2 части высоты (меньше, чем фильмы)
list_line.addLayout(h2_line) # Добавляем макет с кнопками жанров
h2_line.addWidget(add_genre_btn)
h2_line.addWidget(del_genre_btn)

list_line.addStretch(1) # Добавляем растяжитель, чтобы поле поиска и кнопка были внизу правой панели
list_line.addWidget(search_field)
list_line.addWidget(search_btn)


# Устанавливаем главный макет для окна
window.setLayout(main_line)

# --- Стилизация приложения (Улучшенный QSS для минимализма) ---
app.setStyleSheet("""
    QWidget {
        background-color: #fdfdfd; /* Почти чистый белый фон */
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 14px;
        color: #333333; /* Мягкий, но читаемый серый цвет текста */
    }

    /* Общие стили для полей ввода и списков */
    QTextEdit, QLineEdit, QListWidget {
        background-color: #ffffff; /* Чистый белый фон */
        border: 1px solid #e9ecef; /* Очень тонкая, едва заметная рамка */
        border-radius: 8px; /* Скругление углов чуть больше для мягкости */
        padding: 12px; /* Увеличенный внутренний отступ для "воздуха" */
        selection-background-color: #e2f4fb; /* Нежное голубое выделение */
        selection-color: #000000;
        outline: none; /* Убираем стандартный фокусный контур */
    }

    QTextEdit {
        font-size: 16px; /* Чуть больший шрифт для основного текста описания */
        line-height: 1.6; /* Увеличенный межстрочный интервал для лучшей читаемости */
    }

    QLineEdit {
        font-size: 15px;
        height: 40px; /* Соответствует высоте кнопок */
        padding: 0 12px; /* Горизонтальный отступ, вертикальный управляется height */
    }

    QListWidget {
        font-size: 15px; /* Чуть больший шрифт для элементов списка */
    }

    QListWidget::item {
        padding: 10px 15px; /* Увеличенные отступы для каждого элемента списка */
        border-bottom: 1px solid #f5f5f5; /* Очень тонкая и светлая разделительная линия */
    }

    QListWidget::item:hover {
        background-color: #f9f9f9; /* Едва заметное изменение при наведении */
    }

    QListWidget::item:selected {
        background-color: #dbeeff; /* Мягкий светло-голубой для выделенного элемента */
        color: #1a1a1a; /* Темный текст для контраста */
        border-radius: 6px; /* Скругление для выбранного элемента */
        margin: 2px; /* Небольшой отступ, чтобы выбранный элемент выглядел "приподнятым" */
    }

    /* Стили для кнопок */
    QPushButton {
        background-color: #e8e8e8; /* Светло-серый фон кнопок */
        color: #444444; /* Темно-серый текст кнопок */
        border: 1px solid #dcdcdc; /* Тонкая рамка чуть темнее фона */
        border-radius: 8px; /* Скругленные углы */
        padding: 10px 20px; /* Внутренние отступы */
        font-weight: 500; /* Немного жирнее */
        min-width: 100px; /* Чуть большая минимальная ширина */
        height: 40px; /* Фиксированная высота для всех кнопок */
    }

    QPushButton:hover {
        background-color: #dddddd; /* Чуть темнее серый при наведении */
        border-color: #c8c8c8; /* Рамка становится чуть темнее */
    }

    QPushButton:pressed {
        background-color: #cccccc; /* Еще темнее при нажатии */
        border-color: #b0b0b0;
    }
""")

# Функционал
def update_database():
    database = open('films.json', 'w', encoding='utf-8')
    json.dump(films, database, ensure_ascii=False)

def show_film_info():
    film_name = films_list.selectedItems()[0].text()
    description_field.setText( films[ film_name ]['описание'] )
    genres_list.clear()
    genres_list.addItems( films[ film_name ]['жанры'] )

def add_film():
    film_name, ok = QInputDialog.getText(window, 'Добавить фильм', 'Название')
    if film_name != '':
        films[ film_name ] = {'описание': '', 'жанры': []}
        films_list.addItem(film_name)
        update_database()
        

# Подписки на события
films_list.itemClicked.connect(show_film_info)
add_film_btn.clicked.connect(add_film)

# --- Запуск приложения ---
database = open('films.json', encoding='utf-8')
films = json.load(database)
films_list.addItems(films)
window.show() # Отображаем главное окно
app.exec() # Запускаем основной цикл обработки событий приложения
