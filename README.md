# "Сервис укорачивания ссылок" (YaCut)

#### [Описание](#1)
#### [База данных и переменные окружения](#2)
#### [Команды для запуска](#3)
#### [Работа с API](#4)
#### [Техническая информация](#5)
#### [Об авторе](#6)

---
## Описание <a id=1></a>

Проект сервиса для укорачивания ссылок (YaCut) предоставляет пользователям следующие возможности:
  - создавать короткие ссылки для любых URL адресов
  - переходить по коротким ссылкам и/или передавать их другим пользователям
  - при желании самостоятельно задавать имена коротким ссылкам
  - есть возможность работы с базой данных сервиса через запросы к API

---
## База данных и переменные окружения <a id=2></a>

Проект использует базу данных SQLite.  
Для подключения и выполненя запросов к базе данных необходимо создать и заполнить файл ".env" с переменными окружения в корневой папке проекта.

Шаблон для заполнения файла ".env":
```python
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY='Здесь указать секретный ключ'
```

---
## Команды для запуска <a id=3></a>

Перед запуском необходимо склонировать проект:
```bash
HTTPS: git clone https://github.com/moritys/yacut.git
SSH: git clone git@github.com:moritys/yacut.git
```

Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
```
```bash
Linux: source venv/bin/activate
Windows: source venv/Scripts/activate
```

И установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Создать базу данных и выполнить миграции:
```bash
flask db upgrade
```

Запустить проект можно командой:
```bash
flask run
```

Теперь доступность проекта можно проверить по адресу [http://localhost:5000/](http://localhost:5000/)

---
## Работа с API <a id=4></a>

Доступные эндпоинты:
```
"/api/id/"
"/api/id/{short_id}/"
```

Примеры запросов:
- Получение полного URL по короткой ссылке:
```
Method: GET
Endpoint: "/api/id/{short_id}/"
```

- Создание короткой ссылки:
```
Method: POST
Endpoint: "/api/id/"
Payload:
{
    "url": "string",
    "custom_id": "string",
}
```

---
## Техническая информация <a id=5></a>

Стек технологий: Python 3, html, Flask, SQLAlchemy, Alembic, Jinja2, httpcat

---
## Авторы <a id=6></a>

Masha [🍄](https://t.me/mori_tys)