"""
Диалог выбора файла.
"""

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                            QVBoxLayout, QWidget, QLabel, QFileDialog, QTextEdit)


class FileDialogWindow(QMainWindow):
    """Окно с диалогом выбора файла."""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Инициализация интерфейса."""
        self.setWindowTitle("Диалог выбора файла")
        self.setGeometry(100, 100, 600, 400)
        
        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Вертикальный layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Метка
        self.label = QLabel("Выберите файл для открытия")
        layout.addWidget(self.label)
        
        # Кнопка выбора файла
        open_button = QPushButton("Выбрать файл")
        open_button.clicked.connect(self.open_file)
        layout.addWidget(open_button)
        
        # Кнопка сохранения файла
        save_button = QPushButton("Сохранить файл")
        save_button.clicked.connect(self.save_file)
        layout.addWidget(save_button)
        
        # Текстовое поле для отображения пути
        self.text_field = QTextEdit()
        self.text_field.setReadOnly(True)
        self.text_field.setPlaceholderText("Путь к файлу будет отображен здесь...")
        layout.addWidget(self.text_field)
    
    def open_file(self):
        """Открывает диалог выбора файла."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите файл",
            "",
            "Все файлы (*);;Текстовые файлы (*.txt);;Python файлы (*.py)"
        )
        
        if file_path:
            self.label.setText(f"Выбранный файл: {file_path}")
            self.text_field.append(f"Открыт файл: {file_path}")
            
            # Попытка прочитать содержимое файла
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.text_field.append(f"\nСодержимое файла:\n{content}")
            except Exception as e:
                self.text_field.append(f"\nОшибка при чтении файла: {e}")
    
    def save_file(self):
        """Открывает диалог сохранения файла."""
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Сохранить файл",
            "",
            "Текстовые файлы (*.txt);;Все файлы (*)"
        )
        
        if file_path:
            self.label.setText(f"Файл будет сохранен: {file_path}")
            self.text_field.append(f"Выбран путь для сохранения: {file_path}")
            
            # Сохраняем пример текста
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write("Это пример сохраненного текста.\n")
                    f.write("Файл создан через PyQt5 диалог сохранения.")
                self.text_field.append(f"\nФайл успешно сохранен!")
            except Exception as e:
                self.text_field.append(f"\nОшибка при сохранении файла: {e}")


def main():
    """Запуск приложения."""
    app = QApplication([])
    window = FileDialogWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

