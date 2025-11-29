"""
Рисование фигур мышью.
"""

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                            QVBoxLayout, QWidget, QLabel)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QColor
import sys


class DrawingCanvas(QWidget):
    """Холст для рисования."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.shapes = []
        self.current_shape = None
        self.drawing = False
        self.shape_type = "rectangle"
        self.setMinimumSize(700, 500)
        self.setStyleSheet("background-color: white; border: 1px solid black;")
    
    def set_shape_type(self, shape_type):
        """Устанавливает тип фигуры."""
        self.shape_type = shape_type
    
    def mousePressEvent(self, event):
        """Обработка нажатия мыши."""
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.start_point = event.pos()
            self.current_shape = {
                'type': self.shape_type,
                'start': self.start_point,
                'end': self.start_point
            }
    
    def mouseMoveEvent(self, event):
        """Обработка движения мыши."""
        if self.drawing and self.current_shape:
            self.current_shape['end'] = event.pos()
            self.update()
    
    def mouseReleaseEvent(self, event):
        """Обработка отпускания мыши."""
        if event.button() == Qt.LeftButton and self.drawing:
            self.drawing = False
            if self.current_shape:
                self.shapes.append(self.current_shape.copy())
                self.current_shape = None
                self.update()
    
    def paintEvent(self, event):
        """Отрисовка фигур."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Рисуем сохраненные фигуры
        for shape in self.shapes:
            self.draw_shape(painter, shape)
        
        # Рисуем текущую фигуру
        if self.current_shape:
            self.draw_shape(painter, self.current_shape)
    
    def draw_shape(self, painter, shape):
        """Рисует фигуру."""
        pen = QPen(QColor(0, 0, 255), 2)
        painter.setPen(pen)
        
        start = shape['start']
        end = shape['end']
        
        if shape['type'] == 'rectangle':
            x = min(start.x(), end.x())
            y = min(start.y(), end.y())
            width = abs(end.x() - start.x())
            height = abs(end.y() - start.y())
            painter.drawRect(x, y, width, height)
        
        elif shape['type'] == 'circle':
            x = min(start.x(), end.x())
            y = min(start.y(), end.y())
            width = abs(end.x() - start.x())
            height = abs(end.y() - start.y())
            painter.drawEllipse(x, y, width, height)
        
        elif shape['type'] == 'line':
            painter.drawLine(start, end)
    
    def clear_canvas(self):
        """Очищает холст."""
        self.shapes = []
        self.current_shape = None
        self.update()


class DrawingWindow(QMainWindow):
    """Окно для рисования фигур мышью."""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Инициализация интерфейса."""
        self.setWindowTitle("Рисование фигур")
        self.setGeometry(100, 100, 800, 600)
        
        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Вертикальный layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Метка
        label = QLabel("Выберите тип фигуры и рисуйте мышью на холсте")
        layout.addWidget(label)
        
        # Холст для рисования (создаем до кнопок, чтобы можно было на него ссылаться)
        self.canvas = DrawingCanvas()
        
        # Кнопки выбора типа фигуры
        from PyQt5.QtWidgets import QHBoxLayout
        button_layout = QHBoxLayout()
        
        rect_button = QPushButton("Прямоугольник")
        rect_button.clicked.connect(lambda: self.canvas.set_shape_type("rectangle"))
        button_layout.addWidget(rect_button)
        
        circle_button = QPushButton("Круг")
        circle_button.clicked.connect(lambda: self.canvas.set_shape_type("circle"))
        button_layout.addWidget(circle_button)
        
        line_button = QPushButton("Линия")
        line_button.clicked.connect(lambda: self.canvas.set_shape_type("line"))
        button_layout.addWidget(line_button)
        
        clear_button = QPushButton("Очистить")
        clear_button.clicked.connect(self.canvas.clear_canvas)
        button_layout.addWidget(clear_button)
        
        layout.addLayout(button_layout)
        
        # Добавляем холст в layout
        layout.addWidget(self.canvas)
    
    def set_shape_type(self, shape_type):
        """Устанавливает тип фигуры."""
        self.canvas.set_shape_type(shape_type)
    
    def clear_canvas(self):
        """Очищает холст."""
        self.canvas.clear_canvas()


def main():
    """Запуск приложения."""
    app = QApplication(sys.argv)
    window = DrawingWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

