import sqlite3

conexao = sqlite3.connect('registo.db')


cursor = conexao.cursor()

cursor.execute('''
			CREATE TABLE livro (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        descricao TEXT,
        qtd INTEGER,
        tamanho VARCHAR(9),
        cor VARCHAR(9),
        p_unit FLOAT,
        p_total FLOAT,
        d_entra VARCHAR(18),
        d_entre VARCHAR(18),
        cliente VARCHAR(30),
        vendedor VARCHAR(30),
        executor VARCHAR(30),
        tpa BOOL,
        saida BOOL,
        nota TEXT,
        nuvem BOOL
);
''')

print('certo')

conexao.close()