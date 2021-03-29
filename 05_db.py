import sqlite3

conexao = sqlite3.connect('registo.db')
id=8
cursor = conexao.cursor()

cursor.execute("""
			SELECT  produto FROM registo WHERE id=?
""",(id,))

for registo in cursor.fetchall():
	print(registo)

conexao.close()