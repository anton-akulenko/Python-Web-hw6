from psycopg2 import Error
from db_connection_hw import connection


create_tables = """
DROP TABLE IF EXISTS student_groups CASCADE;
CREATE TABLE student_groups (
  id SERIAL PRIMARY KEY NOT NULL,
  name VARCHAR(10) unique        
);

DROP TABLE IF EXISTS teachers CASCADE;
CREATE TABLE teachers (
  id SERIAL PRIMARY KEY NOT NULL,
  fullname VARCHAR(40)
);

DROP TABLE IF EXISTS students CASCADE;
CREATE TABLE students (
  id SERIAL PRIMARY KEY NOT NULL,
  fullname VARCHAR(40),
  group_id INTEGER REFERENCES student_groups(id)
	  ON DELETE cascade
	  ON UPDATE CASCADE
);

DROP TABLE IF EXISTS subjects CASCADE;
CREATE TABLE subjects (
  id SERIAL PRIMARY KEY NOT NULL,
  name VARCHAR(20),
  teacher_id INTEGER REFERENCES teachers(id)
	  ON DELETE cascade
	  ON UPDATE CASCADE
);

DROP TABLE IF EXISTS grades CASCADE;
CREATE TABLE grades (
  id SERIAL PRIMARY KEY NOT NULL,
  subject_id INTEGER REFERENCES subjects (id),
  student_id INTEGER REFERENCES students(id)
  ON DELETE cascade
  ON UPDATE cascade,
  grade INTEGER,
  date_of_grade DATE
);
"""

if __name__ == "__main__":
    with connection() as conn:
        c = conn.cursor()
        c.execute(create_tables)
        c.close()
