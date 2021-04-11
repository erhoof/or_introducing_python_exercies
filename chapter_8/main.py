import csv
import sqlite3

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
    conn = sqlite3.connect('books.db')
    curs = conn.cursor()
    cusr.execute('')
