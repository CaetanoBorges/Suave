import sqlite3

conexao = sqlite3.connect('registo.db')


cursor = conexao.cursor()

cursor.execute("""
			INSERT INTO registo (
        produto, qtd, tc, dtrecebido, dtentrega, pu, pt, cliente, recp, exec ) VALUES ('Vinil + PVC', '1', '1m²', '28-07-2018', '29-07-2018', 'fhj ', '7500', 'TAV', 'Alê Borge', 'Edeangola.com')
""")
conexao.commit()
print('certo')

conexao.close()