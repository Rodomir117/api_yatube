# API для Yatube
Проект api_yatube

Учебный проект Яндекс.Практикум курса Python-разработчик(backend).

## Технологии

    Python 3.9
    Django 3.2
    Django REST framework 3.12


## Инструкция для пользователей Git Bash

1.Клонировать репозиторий и перейти в папку **api_yatube**:

        git clone git@github.com:Rodomir117/api_yatube.git
        cd api_yatube

2.Cоздать и активировать виртуальное окружение:

        py -m venv venv
        source venv/Scripts/activate

3.Установить зависимости из файла requirements.txt:

        pip install -r requirements.txt

5.Перейти в папку проекта **yatube_api** и запустить его:

        cd yatube_api
        ./manage.py migrate
        ./manage.py runserver

6.Перейти на локальный сервер:

        http://127.0.0.1:8000/
  