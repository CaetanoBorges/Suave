import sqlite3

conexao = sqlite3.connect('registo.db')
cursor=conexao.cursor()




entradas=[(
        'Vinil + PVC',
        '2',
        '0.6x0.5',
        ' ',
        '5000',
        '10000',
        '02-08-2018',
        '02-08-2018',
        'Escola 1° de maio',
        'Borges',
        'Domigos e Tomás',
        'True',
        'False',
        'Esse trabalho é rápido pois o cliente fará outros conosco',
        'False'
),
(
        'Vinil',
        '2',
        '1x1',
        ' ',
        '7500',
        '15000',
        '02-08-2018',
        '02-08-2018',
        'Mario',
        'Borges',
        'Domigos e Milton',
        'True',
        'False',
        ' ',
        'False'
),
(
        'Lona',
        '3',
        '1x1',
        ' ',
        '7500',
        '22500',
        '02-08-2018',
        '02-08-2018',
        'Mario',
        'Borges',
        'Milton',
        'True',
        'False',
        ' ',
        'False'
),
(
        'Cartões de visita',
        '71',
        ' ',
        ' ',
        '70',
        '5000',
        '02-08-2018',
        '02-08-2018',
        'Dona Nova',
        'Borges',
        'Domigos',
        'True',
        'False',
        ' ',
        'False'
)]

query=cursor.executemany("""
INSERT INTO livro (
        descricao,
        qtd,
        tamanho,
        cor,
        p_unit,
        p_total,
        d_entra,
        d_entre,
        cliente,
        vendedor,
        executor,
        tpa,
        saida,
        nota,
        nuvem ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
""", entradas)

conexao.commit()







