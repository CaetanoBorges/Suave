import sqlite3

conexao = sqlite3.connect('registo.db')
id=8
cursor = conexao.cursor()


def entradas():
		logica='False'
		cursor.execute(""" SELECT p_total FROM livro WHERE saida=? """,(logica,))
		tudo=cursor.fetchall()
		y=[ ]
		for registo in tudo:
			registo = int(registo[0])
			y.append(registo)
	
	
		soma=sum(y)
		return soma

def tpa():
	logica='True'
	cursor.execute("""
	SELECT p_total FROM livro WHERE tpa=?
	""",(logica,))
	tudo=cursor.fetchall()
	y=[ ]
	for registo in tudo:
		registo=int(registo[0])
		y.append(registo)
		
	tpa=sum(y)
	return tpa
	
	
def dinheiro():
	logica='False'
	cursor.execute("""
	SELECT p_total FROM livro WHERE tpa=?
	""",(logica,))
	tudo=cursor.fetchall()
	y=[ ]
	for registo in tudo:
		registo=int(registo[0])
		y.append(registo)
		
	dinheiro=sum(y)
	return dinheiro


def saidas():
	logica='True'
	cursor.execute("""
	SELECT p_total FROM livro WHERE saida=?
	""",(logica,))
	tudo=cursor.fetchall()
	y=[ ]
	for registo in tudo:
		registo=int(registo[0])
		y.append(registo)
		
	saidas=sum(y)
	return saidas

#NUMERO DE TODOS
def n_entradas():
	logica='False'
	cursor.execute("""
	SELECT COUNT(saida) as saida FROM livro WHERE saida=?
	""",(logica,))
	tudo=cursor.fetchall()
	y=[ ]
	for registo in tudo:
		registo=int(registo[0])
		y.append(registo)
		
	n_entradas=sum(y)
	return n_entradas
		
def n_saidas():
	logica='True'
	cursor.execute("""
	SELECT COUNT(saida) as saida FROM livro WHERE saida=?
	""",(logica,))
	tudo=cursor.fetchall()
	y=[ ]
	for registo in tudo:
		registo=int(registo[0])
		y.append(registo)
		
	n_saidas=sum(y)
	return n_saidas

#GRUPOS
def grupo_e():
	logica='False'
	cursor.execute("""
	SELECT * FROM livro
	""",)
	tudo=cursor.fetchall()
	y=[ ]
	for registo in tudo:
		registo=registo
		y.append(registo)
		
	grupo=y
	return grupo

def grupo_s():
	logica='True'
	cursor.execute("""
	SELECT d_entra FROM livro WHERE saida=? GROUP BY d_entra
	""",(logica,))
	tudo=cursor.fetchall()
	y=[ ]
	for registo in tudo:
		registo=registo
		y.append(registo)
		
	grupo=y
	return grupo

def n_tpa():
		conexao = sqlite3.connect('registo.db')
		cursor = conexao.cursor()
		logica='True'
		cursor.execute("""
		SELECT * FROM livro WHERE tpa=?
		""",(logica,))
		tudo=cursor.fetchall()
		y=[ ]
		for registo in tudo:
			registo=registo
			y.append(registo)
			
		n_tpa=y
		x=0
		l=len(n_tpa)
		b=slice(l)
		
		for y in y:
			print(b)

for i in grupo_e():
	print(i[6])
	print(i[7])
	print(i[8])
print('-----------------')
print(grupo_e())

conexao.close()