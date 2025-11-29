"""
Игра «Кликер» на PyQt5.
"""

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                            QVBoxLayout, QWidget, QLabel)
from PyQt5.QtCore import QTimer


class ClickerGame(QMainWindow):
    """Игра-кликер."""
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.clicks_per_second = 0
        self.auto_click_level = 0
        self.init_ui()
        self.start_auto_clicker()
    
    def init_ui(self):
        """Инициализация интерфейса."""
        self.setWindowTitle("Игра Кликер")
        self.setGeometry(100, 100, 400, 500)
        
        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Вертикальный layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Заголовок
        title = QLabel("КЛИКЕР")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title)
        
        # Счет
        self.score_label = QLabel(f"Счет: {self.score}")
        self.score_label.setStyleSheet("font-size: 18px;")
        layout.addWidget(self.score_label)
        
        # Кнопка клика
        self.click_button = QPushButton("КЛИКНИ МЕНЯ!")
        self.click_button.setStyleSheet("""
            font-size: 20px;
            padding: 20px;
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
        """)
        self.click_button.clicked.connect(self.increment_score)
        layout.addWidget(self.click_button)
        
        # Информация об автокликере
        self.auto_click_label = QLabel(f"Автокликер: {self.clicks_per_second} кликов/сек")
        layout.addWidget(self.auto_click_label)
        
        # Кнопка улучшения автокликера
        self.upgrade_button = QPushButton(f"Улучшить автокликер (стоимость: {self.get_upgrade_cost()})")
        self.upgrade_button.clicked.connect(self.upgrade_auto_clicker)
        layout.addWidget(self.upgrade_button)
        
        # Кнопка сброса
        reset_button = QPushButton("Сбросить игру")
        reset_button.clicked.connect(self.reset_game)
        layout.addWidget(reset_button)
    
    def increment_score(self):
        """Увеличивает счет при клике."""
        self.score += 1
        self.update_ui()
    
    def get_upgrade_cost(self):
        """Возвращает стоимость улучшения автокликера."""
        return (self.auto_click_level + 1) * 10
    
    def upgrade_auto_clicker(self):
        """Улучшает автокликер."""
        cost = self.get_upgrade_cost()
        if self.score >= cost:
            self.score -= cost
            self.auto_click_level += 1
            self.clicks_per_second = self.auto_click_level
            self.update_ui()
    
    def auto_click(self):
        """Автоматически увеличивает счет."""
        if self.clicks_per_second > 0:
            self.score += self.clicks_per_second
            self.update_ui()
    
    def start_auto_clicker(self):
        """Запускает таймер автокликера."""
        self.timer = QTimer()
        self.timer.timeout.connect(self.auto_click)
        self.timer.start(1000)  # Каждую секунду
    
    def update_ui(self):
        """Обновляет интерфейс."""
        self.score_label.setText(f"Счет: {self.score}")
        self.auto_click_label.setText(f"Автокликер: {self.clicks_per_second} кликов/сек")
        self.upgrade_button.setText(f"Улучшить автокликер (стоимость: {self.get_upgrade_cost()})")
        
        # Блокируем кнопку улучшения, если недостаточно очков
        if self.score < self.get_upgrade_cost():
            self.upgrade_button.setEnabled(False)
            self.upgrade_button.setStyleSheet("background-color: #cccccc;")
        else:
            self.upgrade_button.setEnabled(True)
            self.upgrade_button.setStyleSheet("background-color: #2196F3; color: white;")
    
    def reset_game(self):
        """Сбрасывает игру."""
        self.score = 0
        self.auto_click_level = 0
        self.clicks_per_second = 0
        self.update_ui()


def main():
    """Запуск приложения."""
    app = QApplication([])
    window = ClickerGame()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

