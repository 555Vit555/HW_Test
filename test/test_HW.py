import pytest

from main import Student, Lecturer, Reviewer
# Тест метода rate_lecturer класса Student

@pytest.fixture
def student():
    return Student('John', 'Doe', 'male')

@pytest.fixture
def lecturer():
    return Lecturer('Jane', 'Smith')

def test_rate_lecturer(student, lecturer):
    lecturer.courses_attached.append('Python')
    student.courses_in_progress.append('Python')
    
    student.rate_lecturer(lecturer, 'Python', 9)
    assert lecturer.grades_l['Python'] == [9]
    
    student.rate_lecturer(lecturer, 'Python', 8)
    assert lecturer.grades_l['Python'] == [9, 8]
    
    student.rate_lecturer(lecturer, 'JavaScript', 7)
    assert 'JavaScript' not in lecturer.grades_l

    student.rate_lecturer(lecturer, 'Python', 10)
    assert lecturer.grades_l['Python'] == [9, 8, 10]



# Тест метода rate_hw класса Reviewer

@pytest.fixture
def student():
    return Student('John', 'Doe', 'male')

@pytest.fixture
def reviewer():
    
    return Reviewer('Jane', 'Smith')


def test_rate_hw(student, reviewer):
    reviewer.courses_attached.append('Python')
    student.courses_in_progress.append('Python')
    
    reviewer.rate_hw(student, 'Python', 9)
    assert student.grades['Python'] == [9]


def test_lecturer_str(lecturer):
    lecturer = Lecturer('name', 'surname')
    lecturer.courses_attached.append('Python')
    lecturer.grades_l['Python'] = [5, 4, 3]

    expected_output = 'Имя: name\nФамилия: surname\nСредняя оценка за лекции: 4.0'
    assert str(lecturer) == expected_output