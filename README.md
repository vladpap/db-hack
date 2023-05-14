![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)


# Скрипт исправление оценок в эл. дневнике


## Установка.
- Загрузить `scripts.py` на сервер дневника.

## Использование

- Запистить команду:
```bash
$ python3 manage.py shell
```
- Ввести команду:
```bash
>>> import scripts
```
- Доступны команды:
    - Исправление оценок 2 и 3 на 5:
  ```bash
  >>> scripts.fix_marks('имя ученика')
  ```
    - Удаление всех замечаний:
  ```bash
  >>> scripts.remove_chastisements('имя ученика')
  ```
    - Добавление похвалы по предмету:
  ```bash
  >>> scripts.create_commendation('имя ученика', 'предмет')
  ```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python [Devman](https://dvmn.org).

Сценарии использования (use-cases) к третьем уроку курса Django ORM.


<img src="https://dvmn.org/assets/img/logo.8d8f24edbb5f.svg" alt= “” width="102" height="25">


## Для запуска локально

- Скачать электронный дневник школы.
- По ссылке [127.0.0.1:8000](http://127.0.0.1:8000) вы увидите сайт без данных.
- Скачать базу данных дневника.
- На [локальном сайте](http://127.0.0.1:8000) появятся данные.
- Скачать `scripts.py` текущего репозитория в корневой каталог.
- Использовать согласно этому README.
