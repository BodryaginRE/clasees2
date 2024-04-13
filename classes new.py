def calculate_average_grade_for_all_courses():
    total_sum = 0


class Student:
    def __init__(self, name, surname):
        self.l_courses_attached = []
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course].append(grade)
        else:
            self.grades[course] = [grade]

    def get_average_grade(self):
        global res
        sum_ = 0
        len_ = 0
        for mark in self.grades.values():
            sum_ += sum(mark)
            len_ += len(mark)
            res = round(sum_ / len_, 2)
        return res

    def assign_grade(self, lecturer, grade):
        lecturer.set_grade(self.name, grade)

    def get_average_grade_for_homework(self):
        pass

    def rate_bl(self, lecturer, l_course, l_grade, ):
        if isinstance(lecturer,
                      Lecturer) and l_course in self.l_courses_attached and l_course in lecturer.courses_in_progress:
            if l_course in lecturer.l_grades:
                lecturer.l_grades[l_course] += [l_grade]
            else:
                lecturer.l_grades[l_course] = [l_grade]
        else:
            return 'Ошибка'

    def medium_grade_student(self):
        list_grade = self.grades.values()
        sum_grade = 0
        for grade_student in list_grade:
            sum_grade += sum(grade_student)
            return sum_grade / len(grade_student)

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.grades}\nКурсы "
                f"в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}")

    def __lt__(self, other_student):
        if isinstance(other_student, Student):
            return self.medium_grade_student() < other_student.medium_grade_student()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.l_gradescourses_attached = []
        self.l_courses = []
        self.l_courses_attached = []
        self.l_grades = {}
        self.lecturers = Lecturer
        self.l_courses_in_progress = []

    def medium_grade(self):
        list_grade = self.l_grades.values()
        sum_grade = 0
        for grade_lecturer in list_grade:
            sum_grade += sum(grade_lecturer)
            return sum_grade / len(grade_lecturer)

    def __lt__(self, other_lecturer):
        if isinstance(other_lecturer, Lecturer):
            return self.medium_grade() < other_lecturer.medium_grade()

    def __str__(self):
        return f"Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции: {self.l_grades}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_nw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка!"

    def __str__(self):
        return f"Имя:{self.name},\nФамилия: {self.surname}"


def create_instances(num_instances, course):
    instances = []
    for _ in range(num_instances):
        instances.append(Student(course))
    return instances


def calculate_average(instances, attribute):
    total = 0
    count = 0
    for instance in instances:
        value = instance.get_attribute(attribute)
        total += value
        count += 1
    if count:
        return total / count
    else:
        pass


student_1 = Student('Антон', 'Пануфриев')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Git']
student_2 = Student('Василиса', 'Кашпир')
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Python']

lecturer_1 = Lecturer('Аркадий', 'Новиков')
lecturer_1.l_courses_attached += ['Python']
lecturer_2 = Lecturer('Анастасия', 'Золотова')
lecturer_2.l_gradescourses_attached += ['Git']

student_1.rate_bl(lecturer_1, 'Python', 10)
student_2.rate_bl(lecturer_2, 'Git', 8)

reviewer_1 = Reviewer('Анжелика', 'Никифорова')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Константин', 'Алымов')
reviewer_2.courses_attached += ['Git']

reviewer_1.rate_nw(student_1, 'Python', 9)
reviewer_2.rate_nw(student_2, 'Git', 7)
best_student = Student('Андрей', 'Безубов')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Максим', 'Уваров')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_nw(best_student, 'Python', 10)
cool_reviewer.rate_nw(best_student, 'Python', 10)
cool_reviewer.rate_nw(best_student, 'Python', 10)

best_lecturer = Lecturer('Дмитрий ', 'Карпов')
best_lecturer.l_courses_attached += ['Git']

cool_student = Student('Вадим', 'Поликарпов')

cool_student.rate_bl(best_lecturer, 'Git', 15)
cool_student.rate_bl(best_lecturer, 'Git', 15)
cool_student.rate_bl(best_lecturer, 'Git', 15)

some_reviewer = Reviewer('Максим', 'Уваров')
some_lecturer = Lecturer('Максим', 'Уваров')
some_student = Student('Вадим', 'Поликарпов')

print(some_student)
print(best_student.grades)
print(best_lecturer.l_grades)
print(some_reviewer)
print(some_lecturer)
