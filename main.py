
### Создаем классы и методы в них
class Student:    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = 0
        self.str_grades = []
      
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_l:
                lecturer.grades_l[course] += [grade]
            else:
                lecturer.grades_l[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        
        for i in self.grades.values():
            for g in i:
                self.str_grades += [g]
                
            self.average_grade = f'{sum(self.str_grades)/len(self.str_grades)}'

        
        student_str = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade}\nКурсы в процессе изучения: {" ".join(self.courses_in_progress)}\nЗавершенные курсы: {" ".join(self.finished_courses)}'
        return student_str
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_grade < other.average_grade
       
   

            
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades_l = {}
        self.courses_attached = []
        self.average_grade_l = 0
        self.str_grades_l = []
    def __str__(self):
        
        for i in self.grades_l.values():
            for g in i:
                self.str_grades_l += [g]
                
        self.average_grade_l = f'{(sum(self.str_grades_l))/len((self.str_grades_l))}'

        lecturer_str = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade_l}'
        return lecturer_str
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return (self.average_grade_l) < (other.average_grade_l)
        
        
        
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        
        reviewer_str = f'Имя: {self.name}\nФамилия: {self.surname}'
        return reviewer_str




# Создаем экземпляры классов
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'JavaS']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'JavaS']



student1 = Student('Ruoy1', 'Eman1', 'your_gender')
student1.courses_in_progress += ['Python']
student2 = Student('Ruoy2', 'Eman2', 'your_gender')
student2.courses_in_progress += ['Python']
student3 = Student('Ruoy3', 'Eman3', 'your_gender')
student3.courses_in_progress += ['Python']
student4 = Student('Ruoy4', 'Eman4', 'your_gender')
student4.courses_in_progress += ['JavaS']
student5 = Student('Ruoy5', 'Eman5', 'your_gender')
student5.courses_in_progress += ['JavaS']
student6 = Student('Ruoy6', 'Eman6', 'your_gender')
student6.courses_in_progress += ['JavaS']
reviewer1 = Reviewer('Some1', 'Buddy1')
reviewer1.courses_attached += ['Python']
reviewer2 = Reviewer('Some2', 'Buddy2')
reviewer2.courses_attached += ['Python']
reviewer3 = Reviewer('Some3', 'Buddy3')
reviewer3.courses_attached += ['Python']
reviewer4 = Reviewer('Some4', 'Buddy4')
reviewer4.courses_attached += ['JavaS']
reviewer5 = Reviewer('Some5', 'Buddy5')
reviewer5.courses_attached += ['JavaS']
lecturer1 = Lecturer('Some6', 'Buddy6')
lecturer1.courses_attached += ['Python']
lecturer2 = Lecturer('Some7', 'Buddy7')
lecturer2.courses_attached += ['JavaS']





# Используем методы для экземпляров классов
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)

reviewer5.rate_hw(student6, 'JavaS', 5)
reviewer5.rate_hw(student6, 'JavaS', 6)
reviewer5.rate_hw(student6, 'JavaS', 7)

student1.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer1, 'Python', 8)

student4.rate_lecturer(lecturer2, 'JavaS', 9)
student5.rate_lecturer(lecturer2, 'JavaS', 10)





#Вызываем "перегруженные" методы
print(student1)
print('------------------------')
print(student6)
print('------------------------')
print(student1 > student6)
print('------------------------')
print(student6 > student1)





#Создаем и вызываем функцию для классов
students1 = [student1, student6]
students2 = [student1]
courses1 = ['Python','JavaS']
lecturers1 = [lecturer1, lecturer2]

def students_hw(students, courses):
    for course in courses:
        result = 0
        for student in students:
            if isinstance(student, Student) and course == " ".join(student.courses_in_progress):
                for i in student.grades.values():
                            for g in i:
                                student.str_grades += [g]
                result = sum(student.str_grades)/len(student.str_grades)
                print(f'Средний балл студентов по курсу {course} за д.з.: {result}')
                
def lecturers_rate(lecturers, courses):
    for course in courses:
        result = 0
        for lecturer in lecturers:
            if isinstance(lecturer, Lecturer) and course == " ".join(lecturer.courses_attached):
                for i in lecturer.grades_l.values():
                            for g in i:
                                lecturer.str_grades_l += [g]
                result = sum(lecturer.str_grades_l)/len(lecturer.str_grades_l)
                print(f'Средний балл за лекции по курсу {course} за д.з.: {result}')          
            
students_hw(students1,courses1)
print('---------------------------')
 
lecturers_rate(lecturers1, courses1)