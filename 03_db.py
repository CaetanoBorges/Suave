import sqlite3
conexao = sqlite3.connect('registo.db')
cursor = conexao.cursor()


chave=input('Chave: ')
lado=input('Lado: ')

BI=cursor.execute(""" SELECT * FROM BI WHERE chave=? and lado=?""",(chave,lado))

if BI:
	print('Entrou no painel')
else:
	print('errado')

lista =[('13346', '346', '13000','3000', '10000','20-08-2018', 'False'), ('100000', '20000', '80000','50000', '50000','01-08-2018', 'False')  ]

cursor.executemany("""
			INSERT INTO controle (t_entradas, t_saidas, s_total, dinheiro, tpa, data, nuvem) VALUES (?,?,?,?,?,?,?)
""", lista)
conexao.commit()
print('certo')

conexao.close()