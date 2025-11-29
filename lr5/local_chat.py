"""
Локальный чат на PyQt5.
"""

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                            QVBoxLayout, QHBoxLayout, QWidget, QTextEdit, 
                            QLineEdit, QLabel)
from PyQt5.QtCore import QTimer
import datetime


class ChatWindow(QMainWindow):
    """Окно локального чата."""
    
    def __init__(self):
        super().__init__()
        self.messages = []
        self.init_ui()
    
    def init_ui(self):
        """Инициализация интерфейса."""
        self.setWindowTitle("Локальный чат")
        self.setGeometry(100, 100, 600, 500)
        
        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Основной вертикальный layout
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Метка с именем пользователя
        name_layout = QHBoxLayout()
        name_label = QLabel("Ваше имя:")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Введите ваше имя")
        self.name_input.setText("Пользователь")
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_input)
        main_layout.addLayout(name_layout)
        
        # Область сообщений
        self.messages_area = QTextEdit()
        self.messages_area.setReadOnly(True)
        self.messages_area.setPlaceholderText("Сообщения будут отображаться здесь...")
        main_layout.addWidget(self.messages_area)
        
        # Приветственное сообщение
        self.add_message("Система", "Добро пожаловать в локальный чат!")
        
        # Поле ввода сообщения
        input_layout = QHBoxLayout()
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Введите сообщение...")
        self.message_input.returnPressed.connect(self.send_message)
        input_layout.addWidget(self.message_input)
        
        # Кнопка отправки
        send_button = QPushButton("Отправить")
        send_button.clicked.connect(self.send_message)
        input_layout.addWidget(send_button)
        
        main_layout.addLayout(input_layout)
        
        # Кнопка очистки
        clear_button = QPushButton("Очистить чат")
        clear_button.clicked.connect(self.clear_chat)
        main_layout.addWidget(clear_button)
    
    def send_message(self):
        """Отправляет сообщение в чат."""
        message_text = self.message_input.text().strip()
        user_name = self.name_input.text().strip() or "Пользователь"
        
        if message_text:
            self.add_message(user_name, message_text)
            self.message_input.clear()
    
    def add_message(self, username, message):
        """Добавляет сообщение в чат."""
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {username}: {message}"
        
        self.messages.append(formatted_message)
        self.messages_area.append(formatted_message)
        
        # Автопрокрутка вниз
        scrollbar = self.messages_area.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
    
    def clear_chat(self):
        """Очищает область сообщений."""
        self.messages_area.clear()
        self.messages = []
        self.add_message("Система", "Чат очищен.")


def main():
    """Запуск приложения."""
    app = QApplication([])
    window = ChatWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

