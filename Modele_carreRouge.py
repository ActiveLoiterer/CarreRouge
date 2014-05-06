import time
import random

class Jeu:
	def __init__(self,nomJoueur):
		self.nomJoueur = nomJoueur
		self.joueur = Pion(self,225,225,265,265)
		self.listeCarreBleu = []
		self.carrebleu1 = CarreBleu(self,100,100,160,160)
		self.carrebleu2 = CarreBleu(self,300,85,360,135)
		self.carrebleu3 = CarreBleu(self,85,350,105,410)
		self.carrebleu4 = CarreBleu(self,355,340,455,360)
		self.listeCarreBleu.append(self.carrebleu1)
		self.listeCarreBleu.append(self.carrebleu2)
		self.listeCarreBleu.append(self.carrebleu3)
		self.listeCarreBleu.append(self.carrebleu4)
		self.listeNom = [] #pour les highscore
		self.temps = None # pour le temps de la partie



class Pion:
	def __init__(self,parent,x1,y1,x2,y2):
		self.posX1=x1
		self.posY1=y1
		self.posX2=x2
		self.posY2=y2

	def changePos(self,x,y):
		self.posX1=x
		self.posY1=y
		self.posX2=x+40
		self.posY2=y+40

class CarreBleu:
	def __init__(self,parent,x1,y1,x2,y2):
		self.posX1=x1
		self.posY1=y1
		self.posX2=x2
		self.posY2=y2
		self.vitesse = 5

	def changePos(self,x,y):
		self.posX1=self.posX1 + x
		self.posY1=self.posY1 + y
		self.posX2=self.posX2 + x
		self.posY2=self.posY2 + y
	
	def collisionAvecMur(self):
		pass



	

