"""
Flask приложение с формой и таблицей данных.
"""

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Данные для таблицы (в реальном приложении это была бы БД)
table_data = [
    {'id': 1, 'name': 'Иван', 'age': 25, 'city': 'Москва'},
    {'id': 2, 'name': 'Мария', 'age': 30, 'city': 'Санкт-Петербург'},
    {'id': 3, 'name': 'Петр', 'age': 28, 'city': 'Новосибирск'},
    {'id': 4, 'name': 'Анна', 'age': 22, 'city': 'Екатеринбург'},
]


@app.route('/')
def index():
    """Главная страница."""
    return render_template('index.html')


@app.route('/greeting', methods=['GET', 'POST'])
def greeting():
    """Страница с формой (имя → приветствие)."""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        if name:
            return render_template('greeting.html', name=name)
        else:
            return render_template('greeting_form.html', error='Пожалуйста, введите имя!')
    return render_template('greeting_form.html')


@app.route('/table')
def table():
    """Страница с таблицей данных."""
    return render_template('table.html', data=table_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

