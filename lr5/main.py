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
        from simple_gui import SimpleWindow
        btn1 = QPushButton("1. Простейший GUI")
        btn1.clicked.connect(lambda: self.open_app(SimpleWindow))
        layout.addWidget(btn1)
        
        from text_input_window import TextInputWindow
        btn2 = QPushButton("2. Окно с текстовым полем")
        btn2.clicked.connect(lambda: self.open_app(TextInputWindow))
        layout.addWidget(btn2)
        
        from file_dialog import FileDialogWindow
        btn3 = QPushButton("3. Диалог выбора файла")
        btn3.clicked.connect(lambda: self.open_app(FileDialogWindow))
        layout.addWidget(btn3)
        
        from local_chat import ChatWindow
        btn4 = QPushButton("4. Локальный чат")
        btn4.clicked.connect(lambda: self.open_app(ChatWindow))
        layout.addWidget(btn4)
        
        from clicker_game import ClickerGame
        btn5 = QPushButton("5. Игра «Кликер»")
        btn5.clicked.connect(lambda: self.open_app(ClickerGame))
        layout.addWidget(btn5)
        
        # Информация
        info = QLabel("\nДля запуска отдельного приложения:\n"
                     "python simple_gui.py\n"
                     "python text_input_window.py\n"
                     "python file_dialog.py\n"
                     "python local_chat.py\n"
                     "python clicker_game.py")
        info.setStyleSheet("font-size: 10px; color: gray;")
        layout.addWidget(info)
    
    def open_app(self, app_class):
        """Открывает выбранное приложение."""
        self.app_window = app_class()
        self.app_window.show()


def main():
    """Запуск главного меню."""
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

