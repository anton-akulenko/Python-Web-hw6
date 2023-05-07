from psycopg2 import Error
from db_connection_hw import connection
from faker import Faker
from random import randint
from datetime import datetime, date, timedelta

fake_data = Faker("uk-UA")
subjects = [
    "Математичний аналіз",
    "Дискретна математика",
    "Геометрія",
    "Програмування",
    "Теорія імовірності",
    "Англійська",
    "Основи баз даних"
]

student_groups = ['ДК-21', 'ДК-22', 'ДК-23']
AMOUNT_TEACHERS = 7
AMOUNT_STUDENTS = 50

# connect = sqlite3.connect('hw.db')
# cur = connect.cursor()


def seed_teachers(cur):
    teachers = [fake_data.name() for _ in range(AMOUNT_TEACHERS)]
    sql = "INSERT INTO teachers(fullname) VALUES(%s);"
    cur.executemany(sql, zip(teachers,))


def seed_subjects(cur):
    sql = "INSERT INTO subjects(name, teacher_id) VALUES(%s, %s);"
    cur.executemany(sql, zip(subjects, iter(randint(1, AMOUNT_TEACHERS) for _ in range(len(subjects)))))


def seed_student_groups(cur):
    sql = "INSERT INTO student_groups(name) VALUES(%s);"
    cur.executemany(sql, zip(student_groups,))


def seed_students(cur):
    students = [fake_data.name() for _ in range(AMOUNT_STUDENTS)]
    sql = "INSERT INTO students(fullname, group_id) VALUES(%s, %s);"
    cur.executemany(sql, zip(students, iter(randint(1, len(student_groups)) for _ in range(len(students)))))


def seed_grades(cur):
    start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
    end_date = datetime.strptime("2023-06-15", "%Y-%m-%d")
    sql = "INSERT INTO grades(subject_id, student_id, grade, date_of_grade) VALUES(%s, %s, %s, %s);"

    def get_list_date(start: date, end: date) -> list[date]:
        result = []
        current_date = start
        while current_date <= end:
            if current_date.isoweekday() < 6:
                result.append(current_date)
            current_date += timedelta(1)
        return result

    list_dates = get_list_date(start_date, end_date)

    grades = []
    for day in list_dates:
        random_subject = randint(1, len(subjects))
        random_students = [randint(1, AMOUNT_STUDENTS) for _ in range(5)]
        for student in random_students:
            grades.append((random_subject, student, randint(30, 100), day.date()))
    cur.executemany(sql, grades)


if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        seed_teachers(c)
        seed_subjects(c)
        seed_student_groups(c)
        seed_students(c)
        seed_grades(c)
        c.close()
