"""
Список (Listbox) и выбор элемента.
"""

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, 
                            QVBoxLayout, QWidget, QListWidget, QMessageBox)
import sys


class ListboxWindow(QMainWindow):
    """Окно со списком и выбором элемента."""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Инициализация интерфейса."""
        self.setWindowTitle("Список и выбор элемента")
        self.setGeometry(100, 100, 400, 500)
        
        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Вертикальный layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Метка
        label = QLabel("Выберите элемент из списка:")
        layout.addWidget(label)
        
        # Список
        self.list_widget = QListWidget()
        # Добавляем элементы в список
        items = ["Яблоко", "Банан", "Апельсин", "Груша", "Виноград", 
                 "Клубника", "Малина", "Черника"]
        self.list_widget.addItems(items)
        self.list_widget.itemDoubleClicked.connect(self.show_selected)
        layout.addWidget(self.list_widget)
        
        # Метка для отображения выбранного элемента
        self.selected_label = QLabel("Выбранный элемент: нет")
        layout.addWidget(self.selected_label)
        
        # Кнопка показа выбранного элемента
        show_button = QPushButton("Показать выбранный элемент")
        show_button.clicked.connect(self.show_selected)
        layout.addWidget(show_button)
        
        # Кнопка добавления элемента
        add_button = QPushButton("Добавить элемент")
        add_button.clicked.connect(self.add_item)
        layout.addWidget(add_button)
        
        # Кнопка удаления элемента
        remove_button = QPushButton("Удалить выбранный элемент")
        remove_button.clicked.connect(self.remove_item)
        layout.addWidget(remove_button)
    
    def show_selected(self):
        """Показывает выбранный элемент."""
        current_item = self.list_widget.currentItem()
        if current_item:
            selected_text = current_item.text()
            self.selected_label.setText(f"Выбранный элемент: {selected_text}")
            QMessageBox.information(self, "Выбранный элемент", 
                                   f"Вы выбрали: {selected_text}")
        else:
            self.selected_label.setText("Выбранный элемент: нет")
            QMessageBox.warning(self, "Предупреждение", 
                              "Пожалуйста, выберите элемент из списка!")
    
    def add_item(self):
        """Добавляет новый элемент в список."""
        from PyQt5.QtWidgets import QInputDialog
        text, ok = QInputDialog.getText(self, "Добавить элемент", 
                                       "Введите название элемента:")
        if ok and text:
            self.list_widget.addItem(text)
    
    def remove_item(self):
        """Удаляет выбранный элемент из списка."""
        current_item = self.list_widget.currentItem()
        if current_item:
            reply = QMessageBox.question(self, "Подтверждение", 
                                       f"Удалить '{current_item.text()}'?",
                                       QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.list_widget.takeItem(self.list_widget.row(current_item))
                self.selected_label.setText("Выбранный элемент: нет")
        else:
            QMessageBox.warning(self, "Предупреждение", 
                              "Пожалуйста, выберите элемент для удаления!")


def main():
    """Запуск приложения."""
    app = QApplication(sys.argv)
    window = ListboxWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

