"""
Класс «Студент» с методом вывода информации.
"""


class Student:
    """Класс для представления студента."""
    
    def __init__(self, name, age, student_id, course, average_grade):
        """
        Инициализация студента.
        
        Args:
            name: Имя студента
            age: Возраст
            student_id: Номер студенческого билета
            course: Курс обучения
            average_grade: Средний балл
        """
        self.name = name
        self.age = age
        self.student_id = student_id
        self.course = course
        self.average_grade = average_grade
    
    def display_info(self):
        """
        Выводит информацию о студенте.
        
        Returns:
            str: Строка с информацией о студенте
        """
        info = f"""
        Информация о студенте:
        Имя: {self.name}
        Возраст: {self.age}
        Номер студенческого билета: {self.student_id}
        Курс: {self.course}
        Средний балл: {self.average_grade}
        """
        return info.strip()
    
    def __str__(self):
        """Строковое представление объекта."""
        return f"Студент {self.name} (ID: {self.student_id}, Курс: {self.course})"
    
    def __repr__(self):
        """Официальное строковое представление объекта."""
        return (f"Student(name='{self.name}', age={self.age}, "
                f"student_id='{self.student_id}', course={self.course}, "
                f"average_grade={self.average_grade})")

