'''
Capstone Project: Database

perform the following
 - Search a book
 - Add a book
 - Update a book
 - delete a book

'''
import sqlite3


#creating a database
db =  sqlite3.connect('data\library_db')
cusor = db.cursor()
# cusor.execute('''
#  drop table books''')
#----Function defination-----
def init_db():
	cusor.execute('''
Create table if not exists books(
book_id int primary key,
book_title varchar(100) not null,
book_qty int not null
)''')
	numb_rows = len(cusor.execute('''
 select * from books
 where book_id = 1002 or book_id = 1003
 ''').fetchall())
	print(numb_rows)
	if numb_rows == 0:
		cusor.execute('''
	 Insert into books 
	 values(1002, 'Software Engineering', 67)''')
		cusor.execute('''
	 Insert into books 
	 values(1003, 'Data Science', 67)''')
	
def add_book():
	pass
	
def search_book():
	pass
	
def update_book():
	pass

def delete_book():
	pass


#-------main block of code----
#initialising my database
init_db()

while True:
	menu = int(input('''Select one option below:
1 - Add a book
2 - Search a book
3 - Update Book
4 - delete book
5 - Exit program
: '''))
	if menu == 5:
		print("Thank you, Bye-bye")
		cusor.execute('''
 drop table books''')
		db.commit()
		break
	else:
		print("Invalid choice.")

	db.commit()
db.close()