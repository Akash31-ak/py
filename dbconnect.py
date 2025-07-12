import sqlite3
conn = sqlite3.connect('student.db')#creates file if not exists
# Create a cursor object to execute SQL commands
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
grade TEXT)
""")

# cursor.execute("""
# INSERT INTO students(name,age,grade)
# values(?,?,?)
# """,("Alice",20,"A+"))

conn.commit()
students_data = {
    ("Akash",20,"B"),
    ("Prakash",23,"A"),
    ("Rakesh",24,"A+")
}
# conn.executemany("""
# INSERT INTO students(name,age,grade)
# values(?,?,?)
# """,students_data)
# conn.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.execute('''
UPDATE students
SET grade = ?
WHERE name = ?
''',("A","Akash"))
conn.commit()

cursor.execute('''
DELETE FROM students
WHERE name = ?
''',("Rakesh",))
conn.commit()
conn.close()