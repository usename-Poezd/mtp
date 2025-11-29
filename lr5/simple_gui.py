"""
Простейший GUI на PyQt5.
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget


class SimpleWindow(QMainWindow):
    """Простое окно с приветствием."""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Инициализация интерфейса."""
        self.setWindowTitle("Простое окно")
        self.setGeometry(100, 100, 300, 200)
        
        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Вертикальный layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Метка с текстом
        label = QLabel("Привет, это простейший GUI на PyQt5!")
        layout.addWidget(label)
        
        # Кнопка закрытия
        button = QPushButton("Закрыть")
        button.clicked.connect(self.close)
        layout.addWidget(button)


def main():
    """Запуск приложения."""
    app = QApplication([])
    window = SimpleWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

