# README #

Тестовое задание Quadro-Group

# Установка виртуального окружения #
```
#!bash
$ sh build_env.sh dev
```
dev - дев-среда
prod - продакшн

# Как запустить? #
1) Активируем виртуальное окружение. Заходим в корень проекта и выполняем:
```
#!bash
$ source env/bin/activate
```
2) Запускаем приложение
```
#!bash
$ python manage.py runserver
```
3) Cуперпользователь: логин - root, пароль - root.

# Примеры запросов #
1. Авторизация
```
#!bash
$ curl --data "username=root&password=root" http://127.0.0.1:8000/app/api/login/
```
2. Выход
```
#!bash
$ curl --data "session=ngd2xn5c0ncife5652zt131chy6vnqlw" http://127.0.0.1:8000/app/api/logout/
```
3. Получение статистики населения по городам:
```
#!bash
$ curl -X GET http://127.0.0.1:8000/app/api/stat/ -H 'Authorization: Token b9bcfb0abadf02d546952e775c2f66a209dc0bd3'
```
ОБРАТИТЕ ВНИМАНИЕ НА ТОКЕН АВТОРИЗАЦИИ: ```b9bcfb0abadf02d546952e775c2f66a209dc0bd3```
4. Добавление категории
```
#!bash
$ curl -X POST -d name=Палатки -d description='Большие и маленькие' http://127.0.0.1:8000/app/api/category/ -H 'Authorization: Token b9bcfb0abadf02d546952e775c2f66a209dc0bd3'
```
Остальные запросы обрабатываются тоже через этот токен.

