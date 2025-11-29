"""
Окно с текстовым полем и кнопкой, выводящей текст.
"""

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, 
                            QVBoxLayout, QWidget, QLineEdit, QTextEdit)
import sys


class TextInputWindow(QMainWindow):
    """Окно с полем ввода и выводом текста."""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Инициализация интерфейса."""
        self.setWindowTitle("Ввод и вывод текста")
        self.setGeometry(100, 100, 500, 400)
        
        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Вертикальный layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Метка
        label = QLabel("Введите текст:")
        layout.addWidget(label)
        
        # Поле ввода
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Введите текст здесь...")
        self.input_field.returnPressed.connect(self.show_text)
        layout.addWidget(self.input_field)
        
        # Кнопка вывода
        button = QPushButton("Вывести текст")
        button.clicked.connect(self.show_text)
        layout.addWidget(button)
        
        # Поле вывода
        self.output_field = QTextEdit()
        self.output_field.setReadOnly(True)
        self.output_field.setPlaceholderText("Здесь будет выведен ваш текст...")
        layout.addWidget(self.output_field)
        
        # Кнопка очистки
        clear_button = QPushButton("Очистить")
        clear_button.clicked.connect(self.clear_text)
        layout.addWidget(clear_button)
    
    def show_text(self):
        """Выводит текст из поля ввода."""
        text = self.input_field.text()
        if text:
            self.output_field.append(f"Вы ввели: {text}")
            self.input_field.clear()
        else:
            self.output_field.append("Поле ввода пустое!")
    
    def clear_text(self):
        """Очищает поле вывода."""
        self.output_field.clear()


def main():
    """Запуск приложения."""
    app = QApplication(sys.argv)
    window = TextInputWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

