# Лабораторная работа 6: Веб-программирование (Flask и FastAPI)

## Описание

Данная лабораторная работа демонстрирует основы веб-программирования с использованием Flask и FastAPI, работу с REST API, шаблонами Jinja2, базами данных и WebSocket.

## Структура проекта

```
lr6/
├── flask_app.py           # Flask приложение с формой и таблицей
├── fastapi_json.py        # FastAPI с JSON endpoints
├── fastapi_db.py          # FastAPI с базой данных
├── fastapi_websocket.py   # FastAPI WebSocket чат
├── docker-compose.yml     # Docker Compose для PostgreSQL
├── chat.html              # HTML клиент для WebSocket чата
├── requirements.txt       # Зависимости проекта
├── templates/             # Шаблоны Jinja2 для Flask
│   ├── index.html
│   ├── greeting_form.html
│   ├── greeting.html
│   └── table.html
└── README.md              # Документация
```

## Выполненные задания

### 1. Страница с формой (имя → приветствие)

Flask приложение с формой ввода имени и страницей приветствия.

**Файл:** `flask_app.py`, `templates/greeting_form.html`, `templates/greeting.html`

**Запуск:**
```bash
python flask_app.py
```

**Использование:**
1. Откройте http://localhost:5000/greeting
2. Введите ваше имя в форму
3. Нажмите "Отправить"
4. Увидите страницу с приветствием

### 2. Страница с таблицей данных

Flask страница с таблицей данных, отображаемой через Jinja2 шаблон.

**Файл:** `flask_app.py`, `templates/table.html`

**Использование:**
1. Откройте http://localhost:5000/table
2. Увидите таблицу с данными пользователей

### 3. FastAPI endpoint возвращает JSON

FastAPI приложение с endpoints, возвращающими JSON данные.

**Файл:** `fastapi_json.py`

**Запуск:**
```bash
python fastapi_json.py
# или
uvicorn fastapi_json:app --host 0.0.0.0 --port 8000
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

**Файл:** `fastapi_db.py`

**Запуск БД:**
```bash
docker-compose up -d
```

**Запуск приложения:**
```bash
export DATABASE_URL="postgresql://user:password@localhost:5432/lab6db"
python fastapi_db.py
# или
uvicorn fastapi_db:app --host 0.0.0.0 --port 8001
```

**Endpoints:**
- `GET /api/products` - Получить все продукты
- `GET /api/products/{product_id}` - Получить продукт по ID
- `POST /api/products` - Создать продукт
- `DELETE /api/products/{product_id}` - Удалить продукт

**Пример создания продукта:**
```bash
curl -X POST "http://localhost:8001/api/products" \
  -H "Content-Type: application/json" \
  -d '{"name": "Ноутбук", "description": "Игровой ноутбук", "price": 75000}'
```

### 5. Приложение чат (WebSocket FastAPI)

WebSocket чат на FastAPI с HTML клиентом.

**Файл:** `fastapi_websocket.py`, `chat.html`

**Запуск:**
```bash
python fastapi_websocket.py
# или
uvicorn fastapi_websocket:app --host 0.0.0.0 --port 8002
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

### 3. Запуск Flask приложения

```bash
python flask_app.py
```

Откройте в браузере: http://localhost:5000

### 4. Запуск FastAPI JSON endpoints

```bash
python fastapi_json.py
```

Или с uvicorn:
```bash
uvicorn fastapi_json:app --host 0.0.0.0 --port 8000 --reload
```

Откройте в браузере: http://localhost:8000/docs

### 5. Запуск FastAPI WebSocket чата

```bash
python fastapi_websocket.py
```

Или с uvicorn:
```bash
uvicorn fastapi_websocket:app --host 0.0.0.0 --port 8002 --reload
```

Откройте в браузере: http://localhost:8002

### 6. Запуск FastAPI с БД

```bash
export DATABASE_URL="postgresql://user:password@localhost:5432/lab6db"
python fastapi_db.py
```

Или с uvicorn:
```bash
uvicorn fastapi_db:app --host 0.0.0.0 --port 8001 --reload
```

## Технологии

- **Flask** - веб-фреймворк для Python
- **FastAPI** - современный веб-фреймворк с автоматической документацией
- **Jinja2** - шаблонизатор для Flask
- **SQLAlchemy** - ORM для работы с БД
- **PostgreSQL** - реляционная база данных
- **WebSocket** - протокол для двусторонней связи
- **Docker Compose** - оркестрация контейнеров

## Основные концепции

### REST API

REST (Representational State Transfer) - архитектурный стиль для веб-сервисов:
- GET - получение данных
- POST - создание данных
- PUT/PATCH - обновление данных
- DELETE - удаление данных

### WebSocket

Протокол для двусторонней связи между клиентом и сервером:
- Постоянное соединение
- Низкая задержка
- Подходит для чатов, игр, real-time приложений

### Шаблоны Jinja2

Шаблонизатор для динамической генерации HTML:
- Переменные: `{{ variable }}`
- Циклы: `{% for item in items %}`
- Условия: `{% if condition %}`

## Требования

- Python 3.8+
- Docker и Docker Compose
- PostgreSQL (через Docker)

## Автор

Лабораторная работа выполнена в рамках изучения веб-программирования на Python.

