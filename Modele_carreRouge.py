import time
import random
import math

class Jeu:
	def __init__(self,nomJoueur):
		self.nomJoueur = nomJoueur
		self.joueur = Pion(self,225,225,265,265)
		self.listeCarreBleu = []
		self.carrebleu1 = CarreBleu(self,100,100,160,160,math.pi/4)
		self.carrebleu2 = CarreBleu(self,300,85,360,135,math.pi/4*3)
		self.carrebleu3 = CarreBleu(self,85,350,105,410,math.pi/4*7)
		self.carrebleu4 = CarreBleu(self,355,340,455,360,math.pi/4*5)
		self.listeCarreBleu.append(self.carrebleu1)
		self.listeCarreBleu.append(self.carrebleu2)
		self.listeCarreBleu.append(self.carrebleu3)
		self.listeCarreBleu.append(self.carrebleu4)
		self.listeNom = [] #pour les highscore
		self.temps = None # pour le temps de la partie

	def startTimer(self):
		pass

	def updateCarreBleu(self):
		for i in self.listeCarreBleu:
			i.changePos()
			i.collisionAvecMur(0,700,0,700)

	def incremVitesse(self)
		for i in self.listeCarreBleu:
			i.vitesse += 1


class Pion:
	def __init__(self,parent,x1,y1,x2,y2):
		self.posX1=x1
		self.posY1=y1
		self.posX2=x2
		self.posY2=y2
		self.dead = False

	def changePos(self,x,y):
		self.posX1=x
		self.posY1=y
		self.posX2=x+40
		self.posY2=y+40

	def isDead(self):
		if self.dead == False:
			return False        
		else:
			return True

	def isOutOfBounds(self, gauche, droite, haut, bas ):
		if self.x1 <= gauche:                                       #collision avec la bordure vers la gauche
			return True
		
		elif self.x2 >= droite:                                       #collision avec la bordure vers la droite
			return True
        
		elif self.y1 <= haut:                                       #collision avec la bordure vers le haut
			return True
        
		elif self.y2 >= bas:                                       #collision avec la bordure vers le bas
			return True

		return False

class CarreBleu:
	def __init__(self,parent,x1,y1,x2,y2, angle):
		self.posX1=x1
		self.posY1=y1
		self.posX2=x2
		self.posY2=y2
		self.vitesse = 5
		self.angleCourant = angle

	def changePos(self):
		self.posX1=(math.cos(self.angleCourant)*self.vitesse)+self.posX1
		self.posY1=(math.sin(self.angleCourant)*self.vitesse)+self.posY1
		self.posX2=(math.cos(self.angleCourant)*self.vitesse)+self.posX2
		self.posY2=(math.sin(self.angleCourant)*self.vitesse)+self.posY2
	
	def collisionAvecMur(self, gauche, droite, haut, bas ):
	#NON-RANDOM METHOD
		if self.posX1 <= gauche:
			if self.angleCourant < math.pi:              	#collision avec la bordure vers la gauche
				self.angleCourant = math.pi/4
			else:
				self.angleCourant = math.pi/4 * 7

		elif self.posX2 >= droite: 
			if self.angleCourant < math.pi:              	#collision avec la bordure vers la droite
				self.angleCourant = math.pi/4 * 3
			else:
				self.angleCourant = math.pi/4 * 5
		
		elif self.posY1 <= haut:                        	#collision avec la bordure vers le haut
			if self.angleCourant > math.pi/2:
				self.angleCourant = math.pi/4 * 3
			else:
				self.angleCourant = math.pi/4 * 7

		elif self.posY2 >= bas: 
			if self.angleCourant > math.pi*1.5:					#collision avec la bordure vers le bas
				self.angleCourant = math.pi/4 * 5
			else:
				self.angleCourant = math.pi/4 * 7

	#RANDOM METHOD
		"""if self.posX1 <= gauche:
			self.angleCourant = random.uniform(math.pi*1.5,math.pi*2.5)	#random.uniform pour accepter les float

		elif self.posX2 >= droite: 
			self.angleCourant = random.uniform(math.pi/2,math.pi*1.5)
		
		elif self.posY1 <= haut:                        	#collision avec la bordure vers le haut
			
			self.angleCourant = random.uniform(0,math.pi)

		elif self.posY2 >= bas: 
			self.angleCourant = random.uniform(math.pi,math.pi*2)"""






	

