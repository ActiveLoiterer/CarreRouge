import time
import random
import math
import threading

class Jeu:
	def __init__(self):
		self.nomJoueur = "Anonymous"

		self.limiteX = 500
		self.limiteY = 500

		self.joueur = Pion(self,self.limiteX/2 - 20,self.limiteY/2 - 20,self.limiteX/2 + 20,self.limiteY/2 + 20)
		self.listeCarreBleu = []

		#coords carre 1 100,100,160,160
		#coords carre 2 500,85,560,135
		#coords carre 3 85,570,105,630
		#coords carre 4 475,580,575,600

		#Set method
		self.carrebleu1 = CarreBleu(self,100,100,160,160,math.pi/4)
		self.carrebleu2 = CarreBleu(self,300,85,360,135,math.pi/4*3)
		self.carrebleu3 = CarreBleu(self,85,350,115,410,math.pi/4*7)
		self.carrebleu4 = CarreBleu(self,355,340,455,360,math.pi/4*5)

		self.listeCarreBleu.append(self.carrebleu1)
		self.listeCarreBleu.append(self.carrebleu2)
		self.listeCarreBleu.append(self.carrebleu3)
		self.listeCarreBleu.append(self.carrebleu4)

		#Random method
		self.initCarreBleuRandom(self.listeCarreBleu)

		self.listeNom = self.lireHighscore() #pour les highscore
		self.tempsDepart = None # pour le temps ou commence la partie
		self.tempsFinal = None #total du temps du joueur
		self.var = 0

	def setNom(self,nom):
		self.nomJoueur = nom;

	def startTimer(self):
		self.tempsDepart = time.time()
		#self.incremVitesse()

	def calculTempsTotal(self):
		tempsFin = time.time()
		self.tempsFinal = tempsFin - self.tempsDepart

	def getTemps(self):
		return self.tempsFinal

	def getListeNom(self):
		return self.listeNom

	def lireHighscore(self):
		highscoreFile = open( "highscore.txt", "r" )
		listeNoms = []
		for line in highscoreFile:
			listeNoms.append(line.splitlines())
		highscoreFile.close()
		return listeNoms

	def ecrireHighscore(self):
		highscoreFile = open("Highscore.txt", "a")
		toWrite =  str("{:10.2f}".format(self.tempsFinal)+"\n")
		highscoreFile.write(self.nomJoueur + " " + toWrite )
		highscoreFile.close()

	def updateCarreBleu(self):
		for i in self.listeCarreBleu:
			i.changePos()
			i.collisionAvecMur(0,self.limiteX,0,self.limiteY)
		self.incremVitesse()

	def updateJeu(self):
		self.calculTempsTotal()
		self.updateCarreBleu()
		self.checkRedSqCollision()

	def incremVitesse(self):
		for i in self.listeCarreBleu:
			i.vitesse += 0.1
			self.var += 1
		#threading.Timer(5,self.incremVitesse).start()

	def checkRedSqCollision(self):
		for i in self.listeCarreBleu:
			if self.joueur.posX2 >= i.posX1 and self.joueur.posX2 < i.posX2:
				if self.joueur.posY1 >= i.posY1 and self.joueur.posY1 <= i.posY2:
					self.joueur.dead = True
				
				if self.joueur.posY2 <= i.posY2 and self.joueur.posY2 > i.posY1:
					self.joueur.dead = True

			if self.joueur.posX1 >= i.posX1 and self.joueur.posX1 <= i.posX2:
				if self.joueur.posY1 >= i.posY1 and self.joueur.posY1 <= i.posY2:
					self.joueur.dead = True
				
				if self.joueur.posY2 <= i.posY2 and self.joueur.posY2 > i.posY1:
					self.joueur.dead = True

		self.joueur.isOutOfBounds(30,self.limiteX - 30,30,self.limiteY - 30)

	def initCarreBleuRandom(self, listeCarre):
                #Area = forme 2d (carré dans notre cas) ou un carré bleu peut apparaitre
                #Area 1 = (0,0) to (limiteX/2,limiteY/2)
                #Area 2 = (limiteX/2,0) to (limiteX,limiteY/2)
                #Area 3 = (0,limiteY/2) to (limiteX/2, limiteY)
                #Area 4 = (limiteX/2,limiteY/2), (limiteX, limiteY)
                #Il faut aussi prendre en compte la bordure et le carré du milieu

                #Premier carré peut apparaitre dans Area 1
                listeCarre[0].posX1 = random.randrange(30,self.limiteX/2-130)
                listeCarre[0].posX2 = random.randrange(listeCarre[0].posX1+10,listeCarre[0].posX1+100)
                listeCarre[0].posY1 = random.randrange(30,self.limiteY/2-130)
                listeCarre[0].posY2 = random.randrange(listeCarre[0].posY1+10,listeCarre[0].posY1+100)


                #Deuxième carré peut apparaitre dans Area 2
                listeCarre[1].posX1 = random.randrange(self.limiteX/2+30,self.limiteX-110)
                listeCarre[1].posX2 = random.randrange(listeCarre[1].posX1+10,listeCarre[1].posX1+100)
                listeCarre[1].posY1 = random.randrange(30,self.limiteY/2-130)
                listeCarre[1].posY2 = random.randrange(listeCarre[1].posY1+10,listeCarre[1].posY1+100)

                #Troisième carré peut apparaitre dans area 3
                listeCarre[2].posX1 = random.randrange(30,self.limiteX/2-130)
                listeCarre[2].posX2 = random.randrange(listeCarre[2].posX1+10,listeCarre[2].posX1+100)
                listeCarre[2].posY1 = random.randrange(self.limiteY/2+30, self.limiteY-130)
                listeCarre[2].posY2 = random.randrange(listeCarre[2].posY1+10,listeCarre[2].posY1+100)

                #Quatrième carré peut apparaitre dans Area 4
                listeCarre[3].posX1 = random.randrange(self.limiteX/2+30,self.limiteX-130)
                listeCarre[3].posX2 = random.randrange(listeCarre[3].posX1+10,listeCarre[3].posX1+100)
                listeCarre[3].posY1 = random.randrange(self.limiteY/2+30, self.limiteY-130)
                listeCarre[3].posY2 = random.randrange(listeCarre[3].posY1+10,listeCarre[3].posY1+100)

                
		#carre.posX1 = random.randrange(30,self.limiteX - 130)
		#carre.posY1 = random.randrange(30,self.limiteY - 130)
		#carre.posX2 = random.randrange(carre.posX1+10,carre.posX1+100)
		#carre.posY2 = random.randrange(carre.posY1+10,carre.posY1+100)

		#while((carre.posX1 >= self.limiteX/2 - 150 and carre.posX2 <= self.limiteX/2 + 150) or (carre.posY1 >= self.limiteY/2 - 150 and carre.posY2 <= self.limiteX/2 + 150)):
			#carre.posX1 = random.randrange(30,self.limiteX - 130)
			#carre.posY1 = random.randrange(30,self.limiteY - 130)
			#carre.posX2 = random.randrange(carre.posX1+10,carre.posX1+100)
			#carre.posY2 = random.randrange(carre.posY1+10,carre.posY1+100)


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
		if self.posX1 <= gauche:                                       #collision avec la bordure vers la gauche
			self.dead = True
		
		elif self.posX2 >= droite:                                       #collision avec la bordure vers la droite
			self.dead = True
        
		elif self.posY1 <= haut:                                       #collision avec la bordure vers le haut
			self.dead = True
        
		elif self.posY2 >= bas:                                       #collision avec la bordure vers le bas
			self.dead = True

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
		"""if self.posX1 <= gauche:
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
				self.angleCourant = math.pi/4 * 7"""

	#RANDOM METHOD
		if self.posX1 <= gauche:
			self.angleCourant = random.uniform(math.pi*1.5,math.pi*2.5)	#random.uniform pour accepter les float

		elif self.posX2 >= droite: 
			self.angleCourant = random.uniform(math.pi/2,math.pi*1.5)
		
		elif self.posY1 <= haut:                        	#collision avec la bordure vers le haut			
			self.angleCourant = random.uniform(0,math.pi)

		elif self.posY2 >= bas: 
			self.angleCourant = random.uniform(math.pi,math.pi*2)
