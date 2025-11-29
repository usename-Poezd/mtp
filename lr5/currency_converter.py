"""
Программа «Конвертер валют».
"""

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, 
                            QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, 
                            QComboBox, QMessageBox)
import sys


class CurrencyConverter(QMainWindow):
    """Конвертер валют."""
    
    def __init__(self):
        super().__init__()
        # Курсы валют (к рублю)
        self.rates = {
            'USD': 90.0,
            'EUR': 98.0,
            'GBP': 115.0,
            'JPY': 0.6,
            'CNY': 12.5,
            'RUB': 1.0
        }
        self.init_ui()
    
    def init_ui(self):
        """Инициализация интерфейса."""
        self.setWindowTitle("Конвертер валют")
        self.setGeometry(100, 100, 500, 300)
        
        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Вертикальный layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Заголовок
        title = QLabel("Конвертер валют")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)
        
        # Поле ввода суммы
        amount_layout = QHBoxLayout()
        amount_label = QLabel("Сумма:")
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Введите сумму")
        amount_layout.addWidget(amount_label)
        amount_layout.addWidget(self.amount_input)
        layout.addLayout(amount_layout)
        
        # Выбор валюты "из"
        from_layout = QHBoxLayout()
        from_label = QLabel("Из валюты:")
        self.from_currency = QComboBox()
        self.from_currency.addItems(list(self.rates.keys()))
        from_layout.addWidget(from_label)
        from_layout.addWidget(self.from_currency)
        layout.addLayout(from_layout)
        
        # Выбор валюты "в"
        to_layout = QHBoxLayout()
        to_label = QLabel("В валюту:")
        self.to_currency = QComboBox()
        self.to_currency.addItems(list(self.rates.keys()))
        self.to_currency.setCurrentText('USD')
        to_layout.addWidget(to_label)
        to_layout.addWidget(self.to_currency)
        layout.addLayout(to_layout)
        
        # Кнопка конвертации
        convert_button = QPushButton("Конвертировать")
        convert_button.clicked.connect(self.convert)
        layout.addWidget(convert_button)
        
        # Результат
        self.result_label = QLabel("Результат: ")
        self.result_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(self.result_label)
        
        # Информация о курсах
        info_label = QLabel("Курсы валют (к RUB):\n" + 
                           "\n".join([f"{k}: {v}" for k, v in self.rates.items() if k != 'RUB']))
        info_label.setStyleSheet("font-size: 10px; color: gray;")
        layout.addWidget(info_label)
    
    def convert(self):
        """Конвертирует валюту."""
        try:
            amount = float(self.amount_input.text())
            from_curr = self.from_currency.currentText()
            to_curr = self.to_currency.currentText()
            
            # Конвертируем через рубли
            # Сначала в рубли
            amount_in_rub = amount * self.rates[from_curr]
            # Потом в целевую валюту
            result = amount_in_rub / self.rates[to_curr]
            
            self.result_label.setText(
                f"Результат: {amount:.2f} {from_curr} = {result:.2f} {to_curr}"
            )
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите корректное число!")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка: {e}")


def main():
    """Запуск приложения."""
    app = QApplication(sys.argv)
    window = CurrencyConverter()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

