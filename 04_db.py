import sqlite3

conexao = sqlite3.connect('registo.db')

prod = input('Produto: ')
qtd = input('qtd: ')
tc = input(' tamanho: ')
dtr = input(' Recebido em: ')
dte = input('Entregar em: ')
pu = input('P Unitario: ')
pt = input('P Total: ')
cli = input('Cliente: ')
recp = input('Recepcionista: ')
exec = input('Executor: ')

cursor = conexao.cursor()

cursor.execute("""
			INSERT INTO registo (
        produto, qtd, tc, dtrecebido, dtentrega, pu, pt, cliente, recp, exec ) VALUES (?,?,?,?,?,?,?,?,?,?)
""", (prod, qtd, tc, dtr, dte, pu, pt, cli, recp, exec))
conexao.commit()
print('certo')

conexao.close()