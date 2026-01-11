"""
Главное меню для запуска всех приложений LR5.
"""

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                            QVBoxLayout, QWidget, QLabel)
import sys


class MainMenu(QMainWindow):
    """Главное меню для выбора приложения."""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Инициализация интерфейса."""
        self.setWindowTitle("Лабораторная работа 5 - Графические интерфейсы")
        self.setGeometry(100, 100, 400, 500)
        
        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Вертикальный layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Заголовок
        title = QLabel("Выберите приложение:")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)
        
        # Кнопки для запуска приложений
        from text_input_window import TextInputWindow
        btn1 = QPushButton("1. Окно с текстовым полем и кнопкой")
        btn1.clicked.connect(lambda: self.open_app(TextInputWindow))
        layout.addWidget(btn1)
        
        from listbox_window import ListboxWindow
        btn2 = QPushButton("2. Список (Listbox) и выбор элемента")
        btn2.clicked.connect(lambda: self.open_app(ListboxWindow))
        layout.addWidget(btn2)
        
        from menu_window import MenuWindow
        btn3 = QPushButton("3. Окно с меню (File→Exit)")
        btn3.clicked.connect(lambda: self.open_app(MenuWindow))
        layout.addWidget(btn3)
        
        from drawing_window import DrawingWindow
        btn4 = QPushButton("4. Рисование фигур мышью")
        btn4.clicked.connect(lambda: self.open_app(DrawingWindow))
        layout.addWidget(btn4)
        
        from currency_converter import CurrencyConverter
        btn5 = QPushButton("5. Конвертер валют")
        btn5.clicked.connect(lambda: self.open_app(CurrencyConverter))
        layout.addWidget(btn5)
        
        # Информация
        info = QLabel("\nДля запуска отдельного приложения:\n"
                     "python text_input_window.py\n"
                     "python listbox_window.py\n"
                     "python menu_window.py\n"
                     "python drawing_window.py\n"
                     "python currency_converter.py")
        info.setStyleSheet("font-size: 10px; color: gray;")
        layout.addWidget(info)
    
    def open_app(self, app_class):
        """Открывает выбранное приложение."""
        self.app_window = app_class()
        self.app_window.show()


def main():
    """Запуск главного меню."""
    import os
    # Подавляем предупреждения Wayland
    os.environ.setdefault('QT_QPA_PLATFORM', 'xcb')
    
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

