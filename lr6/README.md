# Лабораторная работа 6: Веб-программирование (Flask и FastAPI)

## Описание

Данная лабораторная работа демонстрирует основы веб-программирования с использованием Flask и FastAPI, работу с REST API, шаблонами Jinja2, базами данных и WebSocket. Проекты организованы по принципам SOLID и KISS со слоистой архитектурой.

## Архитектура

Все проекты следуют слоистой архитектуре:

```
project/
├── config/          # Конфигурация
├── repositories/    # Доступ к данным
├── services/        # Бизнес-логика (не знает про Flask/FastAPI)
├── handlers/        # HTTP обработчики (роутинг, работа с Flask/FastAPI)
├── models/          # Модели данных (для БД проектов)
└── main.py          # Точка входа (инициализация всех слоев)
```

### Принципы:

- **Repositories** - работают только с данными
- **Services** - бизнес-логика, общаются только с repositories, НЕ знают про Flask/FastAPI
- **Handlers** - HTTP обработчики, организуют роутинг, работают с Flask/FastAPI
- **Инициализация** - вся инициализация происходит в main.py

## Структура проекта

```
lr6/
├── flask_app/              # Flask приложение
│   ├── config/
│   ├── repositories/
│   ├── services/
│   ├── handlers/
│   ├── templates/
│   └── main.py
├── fastapi_json/           # FastAPI JSON endpoints
│   ├── config/
│   ├── repositories/
│   ├── services/
│   ├── handlers/
│   ├── models/
│   └── main.py
├── fastapi_db/             # FastAPI с БД
│   ├── config/
│   ├── repositories/
│   ├── services/
│   ├── handlers/
│   ├── models/
│   └── main.py
├── fastapi_websocket/      # FastAPI WebSocket чат
│   ├── config/
│   ├── repositories/
│   ├── services/
│   ├── handlers/
│   ├── chat.html
│   └── main.py
├── docker-compose.yml       # Docker Compose для PostgreSQL
├── requirements.txt        # Зависимости проекта
└── README.md               # Документация
```

## Выполненные задания

### 1. Страница с формой (имя → приветствие)

Flask приложение с формой ввода имени и страницей приветствия.

**Путь:** `flask_app/`

**Запуск:**
```bash
cd flask_app
python main.py
# или из корня lr6:
PYTHONPATH=./flask_app python flask_app/main.py
```

**Использование:**
1. Откройте http://localhost:5000/greeting
2. Введите ваше имя в форму
3. Нажмите "Отправить"
4. Увидите страницу с приветствием

### 2. Страница с таблицей данных

Flask страница с таблицей данных, отображаемой через Jinja2 шаблон.

**Путь:** `flask_app/`

**Использование:**
1. Откройте http://localhost:5000/table
2. Увидите таблицу с данными пользователей

### 3. FastAPI endpoint возвращает JSON

FastAPI приложение с endpoints, возвращающими JSON данные.

**Путь:** `fastapi_json/`

**Запуск:**
```bash
cd fastapi_json
python main.py
# или из корня lr6:
PYTHONPATH=./fastapi_json python fastapi_json/main.py
# или через uvicorn:
cd fastapi_json && uvicorn main:app --host 0.0.0.0 --port 8000
```

**Endpoints:**
- `GET /` - Информация о приложении
- `GET /api/items` - Получить список элементов (JSON)
- `GET /api/items/{item_id}` - Получить элемент по ID
- `POST /api/items` - Создать новый элемент

**Документация API:**
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### 4. FastAPI с базой данных

FastAPI приложение с подключением к PostgreSQL базе данных.

**Путь:** `fastapi_db/`

**Запуск БД:**
```bash
docker-compose up -d
```

**Запуск приложения:**
```bash
cd fastapi_db
export DATABASE_URL="postgresql+psycopg://user:password@localhost:5432/lab6db"
python main.py
# или из корня lr6:
PYTHONPATH=./fastapi_db python fastapi_db/main.py
# или через uvicorn:
cd fastapi_db && uvicorn main:app --host 0.0.0.0 --port 8001
```

**Endpoints:**
- `GET /api/products` - Получить все продукты
- `GET /api/products/{product_id}` - Получить продукт по ID
- `POST /api/products` - Создать продукт
- `DELETE /api/products/{product_id}` - Удалить продукт

### 5. Приложение чат (WebSocket FastAPI)

WebSocket чат на FastAPI с HTML клиентом.

**Путь:** `fastapi_websocket/`

**Запуск:**
```bash
cd fastapi_websocket
python main.py
# или из корня lr6:
PYTHONPATH=./fastapi_websocket python fastapi_websocket/main.py
# или через uvicorn:
cd fastapi_websocket && uvicorn main:app --host 0.0.0.0 --port 8002
```

Откройте в браузере: http://localhost:8002

**Использование:**
1. Введите ваше имя
2. Введите сообщение и нажмите "Отправить" или Enter
3. Сообщения будут видны всем подключенным пользователям
4. Отображается история последних 10 сообщений

## Установка и запуск

### 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 2. Запуск базы данных

```bash
docker-compose up -d
```

Проверка статуса:
```bash
docker-compose ps
```

Остановка:
```bash
docker-compose down
```

### 3. Запуск приложений

**Flask:**
```bash
cd flask_app
python main.py
```

**FastAPI JSON:**
```bash
cd fastapi_json
python main.py
```

**FastAPI DB:**
```bash
cd fastapi_db
export DATABASE_URL="postgresql+psycopg://user:password@localhost:5432/lab6db"
python main.py
```

**FastAPI WebSocket:**
```bash
cd fastapi_websocket
python main.py
```

**Примечание:** Каждая папка проекта является корнем для своего проекта, поэтому нужно запускать из соответствующей папки или использовать `PYTHONPATH`.

## Архитектурные принципы

### SOLID

- **Single Responsibility** - каждый класс имеет одну ответственность
- **Open/Closed** - открыт для расширения, закрыт для модификации
- **Liskov Substitution** - подтипы заменяемы
- **Interface Segregation** - интерфейсы разделены
- **Dependency Inversion** - зависимости через конструкторы

### KISS (Keep It Simple, Stupid)

- Простая и понятная структура
- Минимум абстракций
- Прямолинейная логика

### Слоистая архитектура

1. **Repositories** - работа с данными
2. **Services** - бизнес-логика (чистый Python, без зависимостей от фреймворков)
3. **Handlers** - HTTP обработка (работа с Flask/FastAPI)
4. **Config** - конфигурация

## Технологии

- **Flask** - веб-фреймворк для Python
- **FastAPI** - современный веб-фреймворк с автоматической документацией
- **Jinja2** - шаблонизатор для Flask
- **SQLAlchemy** - ORM для работы с БД
- **PostgreSQL** - реляционная база данных
- **WebSocket** - протокол для двусторонней связи
- **Docker Compose** - оркестрация контейнеров

## Требования

- Python 3.8+
- Docker и Docker Compose
- PostgreSQL (через Docker)

## Автор

Лабораторная работа выполнена в рамках изучения веб-программирования на Python.
