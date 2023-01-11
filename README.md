# Yatube: сообщества

[![CI](https://github.com/yandex-praktikum/hw02_community/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/yandex-praktikum/hw02_community/actions/workflows/python-app.yml)

### Описание
Социальная сеть для публикации дневников: реализована регистрация, размещение публикаций, добавление публикаций в группы.
Дополнительно:
- Подключена база данных.
- 10 последних записей выводятся на главную страницу. 
- В админ-зоне доступно управление объектами модели Post: можно публиковать новые записи или редактировать/удалять существующие.

### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
```
python -m venv venv
source venv/Scripts/activate
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- В папке с файлом manage.py выполните команду:
```
python manage.py runserver
```
### Технологии
- Python 3.7
- Django 2.2.19

### Автор
Иван Голенко
