# 1CETL
1CETL - это ETL приложение для сбора данных из 1C REST API и передачи в DWH (Greenplum) 

## Необходимая среда:

- Python 3.8
- Docker
- PostgreSQL | Greenplum

## Клонирование проекта

```commandline
git clone http://gitlab.ru.mgo.su/vkalinin/1cetl.git
```

## Запуск с помощью Docker

### Предварительная сборка

```commandline
docker-compose up -d --build
```

### Строка вызова:

```commandline
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
    ├── docs                    - Дополнительная документация проекта
    ├── logging_                - Классы логгера приложения
    ├── models                  - Модели SQLAlchemy
    ├── pipelines               - Основные классы для обработки данных
    ├── public                  - Папка для хранения и монтирования docker
    │   ├── credentials         - Параметры подключения
    │   └── logs                - Логи приложения
    ├── schemas                 - Схемы в нотации Pydantic
    └── main.py                 - Основной модуль приложения
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

docker run --name name-postgres -e POSTGRES_PASSWORD=my-secret -d postgres
```
По-умолчанию будет создан пользователь ```postgres```

## Первичная настройка приложения

При сборке приложения с помощью docker-compose в **Production** среде первичная настройка не требуется. 
В ```app/public/credentials``` монтируется каталог, в котором находится ```mangodb.ini``` и путь к которому берется 
из переменной окружения ```MANGOCREDENTIALS```. Аналогичным образом монтируется каталог с логами в точку 
монтирования ```app/public/logs```

Перед первым запуском приложения в **Development** среде необходимо поместить файл ```mangodb.ini``` в папку 
```app/public/credentials``` и произвести ряд настроек.

### Файл app/public/credentials/mangodb.ini

Добавить следующую секцию. Значения параметров указать те, которые использовались при создании контейнера 
с базой данных PosgreSQL

```ini
[DWHStage]
user=postgres
password=my-secret
host=localhost
port=5432
database=postgres
```

### Файл app/core/consts.py

```python
# Заменить имя файла с настройками credentials или оставить без изменений
CREDENTIALS_FILENAME = 'mangodb.ini'

# Заменить название файла для хранения лога программы или оставить без изменений
LOG_FILENAME = '1cetl.log'

# Ключу 'PROD' добавить dunder (__) для запрета случайной отправки данных в PROD GP.
# Ключ 'STAGE' используется для обозначения среды локальной разработки. Внести значение ключа
# заданное на предыдущем шаге в локальном файле mangodb.ini
DWH_ENV_KEYS = {'PROD': 'PROD_KEY',
                'DEV': 'DEV_KEY',
                'STAGE': 'DWHStage'}
```

### Файл app/config/email_settings.py

```python
# Необходимо заполнить параметры своими значениями.

MAILHOST: str = 'private-mail-server.company.ru'
PORT: int = None
FROM: str = '1CETL@company.ru'
TO: List = ['developer@company.ru', ]
SUBJECT: str = 'Logfile from 1CETL'
```

### Инициализация таблиц базы данных

Все таблицы в **Production Greenplum** созданы без поддержки ```PRIMARY KEY```. По этой причине инициализация 
базы данных посредством ORM SQLAlchemy ```create_new_db() :: app/db/init.py``` приведет к некорректной структуре. 
Поэтому операцию создания таблиц в ```STAGE``` базе данных необходимо выполнить в корневом каталоге проекта следующей командой : 

```commandline
python app/db/init_core.py
```

## Добавление новых моделей и API routes 
