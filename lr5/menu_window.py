"""
Окно с меню (File→Exit).
"""

from PyQt5.QtWidgets import (QApplication, QMainWindow, QMenuBar, QAction, 
                            QTextEdit, QMessageBox)
import sys


class MenuWindow(QMainWindow):
    """Окно с меню."""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Инициализация интерфейса."""
        self.setWindowTitle("Окно с меню")
        self.setGeometry(100, 100, 500, 400)
        
        # Создаем меню
        self.create_menu()
        
        # Текстовое поле
        text_edit = QTextEdit()
        text_edit.setPlainText("Это окно с меню.\n"
                              "Используйте меню File для выхода из приложения.")
        self.setCentralWidget(text_edit)
    
    def create_menu(self):
        """Создает меню."""
        # Получаем меню-бар
        menubar = self.menuBar()
        
        # Создаем меню File
        file_menu = menubar.addMenu('File')
        
        # Действие Exit
        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Выход из приложения')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Дополнительные действия
        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)
        
        open_action = QAction('Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        
        file_menu.addSeparator()  # Разделитель
        
        file_menu.addAction(exit_action)
        
        # Меню Help
        help_menu = menubar.addMenu('Help')
        
        about_action = QAction('About', self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def new_file(self):
        """Создает новый файл."""
        QMessageBox.information(self, "New File", "Создание нового файла")
    
    def open_file(self):
        """Открывает файл."""
        QMessageBox.information(self, "Open File", "Открытие файла")
    
    def show_about(self):
        """Показывает информацию о программе."""
        QMessageBox.about(self, "About", 
                         "Окно с меню\n"
                         "Демонстрация работы с меню в PyQt5")
    
    def closeEvent(self, event):
        """Обработка закрытия окна."""
        reply = QMessageBox.question(self, "Выход", 
                                   "Вы уверены, что хотите выйти?",
                                   QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    """Запуск приложения."""
    app = QApplication(sys.argv)
    window = MenuWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

