import sqlite3
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.accordion import Accordion
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.app import runTouchApp
import time
from kivy.clock import Clock
import threading
from kivy.graphics import *

class TelaPrincipal(Screen):
	def min(self):
		at="uiyui"
		return at

class TelaControleUm(Screen):
	pass

class TelaControleDois(Screen):
	#conexao = sqlite3.connect('registo.db')
	#cursor = conexao.cursor()

	def entradas(self):
		conexao = sqlite3.connect('registo.db')
		cursor = conexao.cursor()
		logica='False'
		cursor.execute(""" SELECT p_total FROM livro WHERE saida=? """,(logica,))
		tudo=cursor.fetchall()
		y=[ ]
		for registo in tudo:
			registo = int(registo[0])
			y.append(registo)
	
	
		soma=str(sum(y))
		return soma

	def tpa(self):
		conexao = sqlite3.connect('registo.db')
		cursor = conexao.cursor()
		logica='True'
		cursor.execute("""
		SELECT p_total FROM livro WHERE tpa=?
		""",(logica,))
		tudo=cursor.fetchall()
		y=[ ]
		for registo in tudo:
			registo=int(registo[0])
			y.append(registo)
			
		tpa=str(sum(y))
		return tpa
		
		
	def dinheiro(self):
		conexao = sqlite3.connect('registo.db')
		cursor = conexao.cursor()
		logica='False'
		cursor.execute("""
		SELECT p_total FROM livro WHERE tpa=?
		""",(logica,))
		tudo=cursor.fetchall()
		y=[ ]
		for registo in tudo:
			registo=int(registo[0])
			y.append(registo)
			
		dinheiro=str(sum(y))
		return dinheiro


	def saidas(self):
		conexao = sqlite3.connect('registo.db')
		cursor = conexao.cursor()
		logica='True'
		cursor.execute("""
		SELECT p_total FROM livro WHERE saida=?
		""",(logica,))
		tudo=cursor.fetchall()
		y=[ ]
		for registo in tudo:
			registo=int(registo[0])
			y.append(registo)
			
		saidas=str(sum(y))
		return saidas

	def total(self):
		entradas=self.entradas()
		saidas=self.saidas()
		tot=(int(entradas)-int(saidas))
		return str(tot)

	#NUMERO DE TODOS
	def n_entradas(self):
		conexao = sqlite3.connect('registo.db')
		cursor = conexao.cursor()
		logica='False'
		cursor.execute("""
		SELECT COUNT(saida) as saida FROM livro WHERE saida=?
		""",(logica,))
		tudo=cursor.fetchall()
		y=[ ]
		for registo in tudo:
			registo=int(registo[0])
			y.append(registo)
			
		n_entradas=str(sum(y))
		return n_entradas
			
	def n_saidas(self):
		conexao = sqlite3.connect('registo.db')
		cursor = conexao.cursor()
		logica='True'
		cursor.execute("""
		SELECT COUNT(saida) as saida FROM livro WHERE saida=?
		""",(logica,))
		tudo=cursor.fetchall()
		y=[ ]
		for registo in tudo:
			registo=int(registo[0])
			y.append(registo)
			
		n_saidas=str(sum(y))
		return n_saidas

	def n_dinheiro(self):
		conexao = sqlite3.connect('registo.db')
		cursor = conexao.cursor()
		logica='False'
		cursor.execute("""
		SELECT COUNT(tpa) as tpa FROM livro WHERE tpa=?
		""",(logica,))
		tudo=cursor.fetchall()
		y=[ ]
		for registo in tudo:
			registo=int(registo[0])
			y.append(registo)
			
		n_dinheiro=str(sum(y))
		return n_dinheiro

	def n_tpa(self):
		conexao = sqlite3.connect('registo.db')
		cursor = conexao.cursor()
		logica='True'
		cursor.execute("""
		SELECT COUNT(tpa) as tpa FROM livro WHERE tpa=?
		""",(logica,))
		tudo=cursor.fetchall()
		y=[ ]
		for registo in tudo:
			registo=int(registo[0])
			y.append(registo)
			
		n_tpa=str(sum(y))
		return n_tpa

	#GRUPOS
	def grupo_e(self):
		conexao = sqlite3.connect('registo.db')
		cursor = conexao.cursor()
		logica='False'
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

	def grupo_s(self):
		conexao = sqlite3.connect('registo.db')
		cursor = conexao.cursor()
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

class TelaFaturas(Screen):
	pass

class TelaTodosDias(Screen):
	def __init__(self,**kwargs):
		super(TelaTodosDias, self).__init__(**kwargs)
		with self.canvas:
			Color(1,1,1)
			Rectangle(size=(1000,1150))
		layout=GridLayout(cols=1, spacing=10, size_hint_y=None, padding=10)
		layout.bind(minimum_height=layout.setter('height'))
		
		root=ScrollView(size_hint=(1,None), size=(Window.width, Window.height))
		im=Image(source='suave.jpg')
		layout.add_widget(im)
		conexao = sqlite3.connect('registo.db')
		cursor = conexao.cursor()
		logica='True'
		cursor.execute("""
		SELECT * FROM livro
		""",)
		tudo=cursor.fetchall()
		for registo in tudo:
			registo=registo
			y=registo
			layout.add_widget(Button(text=str(y[1]), size_hint=[1,None], height=55))
			
		root.add_widget(layout)
		self.add_widget(root)
	
	


class GestorDeTela(ScreenManager):
	pass

construtor=Builder.load_file('suave.kv')


class start(App):
	def build(self):
		return construtor



start().run()

