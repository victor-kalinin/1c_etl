# 1CETL
1CETL - это ETL приложение для сбора данных из 1C REST API и передачи в DWH (Greenplum) 

## Необходимая среда:

- Python 3.8
- Docker
- PostgreSQL | Greenplum

## Клонирование проекта

```
git clone http://gitlab.ru.mgo.su/vkalinin/1cetl.git
```

## Запуск с помощью Docker

### Предварительная сборка

```
docker-compose up -d --build
```

### Строка вызова:

```
docker run --rm {NAME_OF_CONTAINER} -{key} {VALUE(s)}


Список ключей запуска:

  -h, --help                    Вывод справки со списком ключей
  -e, --env         PROD        Рабочее окружение
                    DEV
                    STAGE 
  
  -g, --groups      static      Список групп таблиц для пакетной выгрузки данных
                    params
                    accums
                    assert
  
  -t, --table_name  TABLE_NAME  Название таблицы для единичной выгрузки
  -m, --months      MONTHS      Количество месяцев для выгрузки периода
  -d, --direction   FORWARD     Направление формирования периода выгрузки
                    BACKWARD
  -ca, --clear_all              Режим полной очистки таблиц без загрузки данных
```

## Структура приложения

Файлы, связанные с приложением, находятся в папке ``app``. 
Ниже представлена подробная структура этой папки:
```
    app
    ├── config                  - Папка с настройками приложения
    │   ├── api_conn            - Настройки routes для подключения к api
    │   ├── dwh_db.py           - Настройки подключения к БД
    │   └── email_settings.py   - Настройки для отправки e-mail
    ├── core                    - Базовые модули приложения
    │   ├── templates           - Шаблонные классы
    │   ├── consts.py           - Константы и настройки
    │   ├── enums.py            - Классы с перечислениями
    │   ├── helpers.py          - Вспомогательные функции
    │   └── sql.py              - Текстовые SQL-запросы
    ├── db                      - Классы и функции для работы с БД
    ├── logging_                - Классы логгера приложения
    ├── models                  - Модели SQLAlchemy
    ├── pipelines               - Основные классы для обработки данных
    ├── public                  - Папка для хранения и монтирования docker
    │   ├── credentials         - Параметры подключения
    │   └── logs                - Логи приложения
    ├── schemas                 - Схемы в нотации Pydantic
    └── main.py                 - Основной модуль приложения
```

## Первичная настройка приложения

```
dwh_db.py
email_settings.py
consts.py

mangodb.ini
```

## Настройка окружения для разработки

### Использование виртуальной среды python

&nbsp;&nbsp;&nbsp;&nbsp;**Установка:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```pip install virtualenv```

&nbsp;&nbsp;&nbsp;&nbsp;**Активация:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```$ source env/bin/activate```

&nbsp;&nbsp;&nbsp;&nbsp;**Деактивация:** &nbsp;```(env) $ deactivate```

### Установка необходимых зависимостей
```commandline
pip install --no-cache-dir -r requirements.txt
```

### Установка Postgres через Docker
```commandline
docker pull postgres

docker run --name name-postgres -e POSTGRES_PASSWORD=mysecret -d postgres
```
По-умолчанию будет создан пользователь ```postgres```

### Настройка подключения к БД

```
скопировать mangodb.ini в app/public/credentials
или с другим именем, о его прописать в consts.py
Добавить в файл секцию stage с ключом указанным выше
файл app/config/dwh_db.py

```

### Инициализация таблиц базы данных
```
Из-за особенности хранения без PK
```



## Добавление новых моделей и API routes 