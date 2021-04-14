import csv
import sqlite3
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
import os
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    #1
    test1 = 'This is a test of the emergency text system'
    with open('test.txt', 'w') as out:
        out.write(test1)

    #2
    with open('test.txt', 'r') as out:
        test2 = out.read()

    print(test1, test2)

    # 3
    books = [{'author': 'J R R Tolkien', 'book': 'The Hobbit'},
             {'author': 'Lynne Truss', 'book': "Eats, Shoots & Leaves"}]

    with open('books.csv', 'wt') as fout:
        cout = csv.DictWriter(fout, ['author', 'book'])
        cout.writeheader()
        cout.writerows(books)

    # 4
    books2 = []

    with open('books.csv', 'rt') as fin:
        cin = csv.DictReader(fin)
        books2 = [row for row in cin]

    print(books2)

    #5
    books3 = [{'title': 'The Weirdstone of Brisingamen', 'author': 'Alan Garner', 'year': '1960'},
              {'title': 'Perdido Street Station', 'author': 'China Miéville', 'year': '2000'},
              {'title': 'Thud!', 'author': 'Terry Pratchett', 'year': '2005'},
              {'title': 'The Spellman Files', 'author': 'Lisa Lutz', 'year': '2007'},
              {'title': 'Small Gods', 'author': 'Terry Pratchett', 'year': '1992'}]

    with open('books.csv', 'wt') as fin:
        fin = csv.DictWriter(fin, ['title', 'author', 'year'])
        fin.writeheader()
        fin.writerows(books3)

    #6
    try :
        pass
        #os.remove('books.db')
    except FileNotFoundError:
        print('nothing to remove')
    conn = sqlite3.connect('books.db')
    curs = conn.cursor()
    # curs.execute('''CREATE TABLE books
    # (title VARCHAR(20) PRIMARY KEY,
    # author VARCHAR(20),
    # year INT)''')

    with open('books.csv', 'rt') as fin:
        cin = csv.DictReader(fin, ['title', 'author', 'year'])
        books = [row for row in cin]
        ins = 'INSERT INTO books (title, author, year) VALUES (?, ?, ?)'
        for book in books:
            print('ins')
            curs.execute(ins, (book['title'], book['author'], book['year']))
        conn.commit()

    curs.execute('SELECT * FROM books ORDER BY title')
    print(curs.fetchall())
    curs.execute('SELECT * FROM books ORDER BY year')
    print(curs.fetchall())
    curs.close()
    conn.close()

    #7
    conn = sa.create_engine('sqlite:///books.db', echo = True)
    
    Base = declarative_base()
    class Books(Base):
        __tablename__ = 'books'
        title = sa.Column(sa.String, primary_key=True)
        author = sa.Column(sa.String)
        year = sa.Column(sa.Integer)
        # def __init__(self, title, author, year):
        #    self.title = title
        #    self.author = author
        #    self.year = year
        # def __repr__(self):
        #    return "<Books({}, {}, {})>".format(self.title, self.author, self.year)

    #Base.metadata.create_all(conn)
    Session = sessionmaker(bind = conn)
    session = Session()
    result = session.query(Books).order_by('title')

    for row in result:
        print('Title:', row.title)

    # 7-2
    for row in session.query(Books).order_by('year'):
        print('Title:', row.title, 'Year:', row.year)

    # 16.9
    import redis
    conn = redis.Redis()
    
    conn.hmset('test', {'count': 1, 'name': 'Fester Bestertester'})
    print(conn.hgetall('test'))

    conn.hincrby('test', 'count')
    print(conn.hget('test', 'count'))

    
