class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.rate_lecturer = {}

    def rate_lecturers(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_vedush:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
                # lecturer.m_grades.append(grade)
            else:
                lecturer.grades[course] = [grade]
                # lecturer.m_grades.append(grade)
        else:
            return 'Ошибка'

    def st_sr_grades(self):
        sr = 0
        for grade in self.grades.values():
            sr += sum(grade) / len(grade)
        return sr / len(self.grades)

    def __str__(self):
        return (f"Имя: {self.name} \nФамилия:{self.surname} \nСредняя оценка за домашние "
                f"задания: {self.st_sr_grades()}\nКурсы в процессе обучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_vedush = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def __lt__(self, other):
        return self.sr_rate < other.sr_rate

    def __str__(self):
        return f"Имя: {self.name} \nФамилия:{self.surname} \nСредняя оценка за лекции:"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_vedush and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name} \nФамилия:{self.surname}"

# СОЗДАЮ СТУДЕНТОВ
best_student = Student('Petya', 'Bratishkin', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']
best_student1 = Student('Jenya', 'Animro', 'your_gender')
best_student1.courses_in_progress += ['JS']
best_student1.finished_courses += ['Введение в программирование']
# СОЗДАЮ ЛЕКТОРОВ И СТАВЛЮ ИМ ОЦЕНКИ
cool_lecturer1 = Lecturer('Dima', 'Buddy') # Лектор 1
cool_lecturer1.courses_vedush += ['Python', 'JS']
cool_lecturer2 = Lecturer('Vasya', 'Bomz') # Лектор 2
cool_lecturer2.courses_vedush += ['JS']
best_student.rate_lecturers(cool_lecturer1, 'Python', 7)
best_student.rate_lecturers(cool_lecturer1, 'Python', 4)
best_student1.rate_lecturers(cool_lecturer2, 'JS', 3)
# ЗАДАЮ РЕВИВЕРОВ И СТАВЛЮ СТУДЕНТАМ ОЦЕНКИ
cool_reviewer = Reviewer('Some', 'Buddy') # Ревивер 1
cool_reviewer.courses_vedush += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 4)
cool_reviewer2 = Reviewer('One', 'Buddy') # Ревивер 2
cool_reviewer2.courses_vedush += ['JS']
cool_reviewer2.rate_hw(best_student1, 'JS', 5)
#ОЦЕНКИ
# print(f"Оценка лектора 1 {cool_lecturer1.grades} ")
# print(f"Оценка лектора 2 {cool_lecturer2.grades} ")
# print(f"Оценка студенту {best_student.grades}")
# print(f"Оценка студенту {best_student1.grades}")
# ВЫВОД ПО ЗАДАНИЮ 3
# print(f"Ревивер:\n{cool_reviewer2}")
# print(f"Лектор:\n{cool_lecturer1}")
# print(f"Лектор:\n{cool_lecturer2}")
print(f"Студент 1:\n{best_student} \nСтудент 2: \n{best_student1}")


# print(f"Средняя оценка лекторов {cool_lecturer1.sr_grades} ")