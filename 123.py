from os import stat_result


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.rate_lecturer = {}
    # ВЫСТАВЛЕНИЕ ОЦЕНОК ЛЕКТОРАМ
    def rate_lecturers(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_vedush:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    # РАСЧЕТ СРЕДНЕЙ ОЦЕНКИ
    def st_sr_grades(self):
        sr = 0
        for grade in self.grades.values():        # for grade in self.grades.values():
            sr += sum(grade) / len(grade)  #     sr += sum(grade) / len(grade)
            return sr                           # return sr / len(self.grades)
    # СРАВНЕНИЕ ПО ОЦЕНКАМ СТУДЕНТОВ
    def __lt__(self, other):
        return self.st_sr_grades() < other.st_sr_grades()
    # СРЕДНЯЯ ПО ОЦЕНКАМ ОДНОГО КУРСА
    # def st_sr_kurs(self, kurs):
    #     sr=0
    #     for m in self.grades.keys():
    #         if m == kurs:
    #             for grade in self.grades[m]:
    #                 sr += sum(grade) / len(grade)
    #         print(m, kurs)
    #     return sr

    # МАГИЧЕСКИЙ МЕТОД STR
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
    # РАСЧЕТ СРЕДНЕЙ ОЦЕНКИ
    def le_sr_grades(self):
        sr = 0
        for grade in self.grades.values():
            sr += sum(grade) / len(grade)
        return sr
    # СРАВНЕНИЕ ПО ОЦЕНКАМ ЛЕКТОРОВ
    def __lt__(self, other):
        return self.le_sr_grades() < other.le_sr_grades()
    # МАГИЧЕСКИЙ МЕТОД STR
    def __str__(self):
        return f"Имя: {self.name} \nФамилия:{self.surname} \nСредняя оценка за лекции:{self.le_sr_grades()}"

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    # ВЫСТАВЛЕНИЕ ОЦЕНОК СТУДЕНТАМ
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_vedush and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    # МАГИЧЕСКИЙ МЕТОД STR
    def __str__(self):
        return f"Имя: {self.name} \nФамилия:{self.surname}"

# СОЗДАЮ СТУДЕНТОВ
best_student = Student('Petya', 'Bratishkin', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']
best_student1 = Student('Jenya', 'Animro', 'your_gender')
best_student1.courses_in_progress += ['Python', 'JS']
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
cool_reviewer2.rate_hw(best_student1, 'Python', 4)
# ВЫВОД ПО ЗАДАНИЯМ
print(f"\nРевивер 1:\n{cool_reviewer}")
print(f"\nРевивер 2:\n{cool_reviewer2}")
print(f"\nЛектор 1:\n{cool_lecturer1}")
print(f"\nЛектор 2:\n{cool_lecturer2}")
print(f"\nСтудент 1:\n{best_student}")
print(f"\nСтудент 2:\n{best_student1}")
print(f"\nСредняя оценка студента 1 {best_student.st_sr_grades()}")
print(f"Средняя оценка студента 2 {best_student1.st_sr_grades()}")
print(f'У второго больше ср оценка? {best_student<best_student1}')
print(f"\nСредняя оценка лектора 1 {cool_lecturer1.le_sr_grades()}")
print(f"Средняя оценка лектора 2 {cool_lecturer2.le_sr_grades()}")
print(f'У первого больше ср оценка? {cool_lecturer2<cool_lecturer1}')

# print(best_student1.st_sr_kurs(kurs='Python'))
students = [best_student, best_student1]
course = 'Python'
def average_rating_student_course(students: list[Student], course):
    sr = []
    for m in students:
        for n in m.grades.get(course):
            sr.append(n)
        sr = sum(sr)/len(sr)
        print(sr)
print(average_rating_student_course(students, course))
#  я не понимаю как сделать среднюю именно по курсу, сделал в классе студентов что я догнал, помогите,
# потому что через чаты нереально нормально получить помощь, может покажите примерный код
# print(', '.join(m.courses_in_progress))


