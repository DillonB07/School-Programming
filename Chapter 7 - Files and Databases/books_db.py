import sqlite3

db = sqlite3.connect('Library.db')

cursor = db.cursor()

try:
    cursor.execute('''
CREATE TABLE Books
(
book_isbn text,
booke_title text,
book_type text,
book_author text,
publisher text
) 
''')
except sqlite3.OperationalError:
    print('Table already exists. Dropping and recreating table')
    cursor.execute('''
DROP TABLE Books;
''')
    cursor.execute('''
CREATE TABLE Books
(
book_isbn text,
booke_title text,
book_type text,
book_author text,
publisher text
) 
''')
    db.commit()


cursor.execute('''
INSERT INTO Books
VALUES ('978-0-340-88851-3','A2 Pure Mathematics', 'Non fictional', 'Catherine Berry', 'Hodder Education'),
('978-1-118-10227-5', 'Android 4 Application Development', 'Non fictional', 'Reto Meier', 'Wiley'),
('0-596-00699-3', 'Programming in C#', 'Non fictional', 'Jesse Liberty', 'O Reilly')
''')


db.commit()

res = cursor.execute("SELECT * FROM Books")

library = cursor.fetchall()

print(library)

for book in library:
    print(book)

db.close()
