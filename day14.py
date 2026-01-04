import mysql.connector

db = mysql.conector.connect(
username = "root",
host = "localhost",
port = 3306,
database = "python"
)


my_terminal = db.cursor()
# my_terminal.execute('Insert into student (name, address) values ("Ayush, "Kanchanpur)')
# db.commit()
# print(db)


