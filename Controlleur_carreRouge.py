import Vue_carreRouge
import Modele_carreRouge

class Controlleur:
	def __init__(self):
		self.vue = Vue_carreRouge.Vue(self)
		self.jeu = Modele_carreRouge.Jeu()
		self.gameLoop()
		self.vue.root.mainloop()

	def gameLoop(self):
		if(self.vue.pret == 1):
			self.creerJeu()
			#manque le update des carreBleu	
			if(self.jeu.joueur.isDead()):
				self.jeu.calculTempsTotal()
				self.jeu.ecrireHighscore()
				print(self.jeu.tempsFinal)
				self.vue.pret = 0
				self.vue.drawMainMenu()
				self.jeu = Modele_carreRouge.Jeu()
			else:
				self.jeu.calculTempsTotal()
				self.jeu.updateCarreBleu()
				self.jeu.checkRedSqCollision()
				self.vue.drawPions()
				self.vue.root.after(50,self.gameLoop)

	def creerJeu(self):
		if not self.jeu or self.jeu.nomJoueur is "default" :
			self.jeu = Modele_carreRouge.Jeu(self.vue.nomJoueur)
			self.jeu.startTimer()


if __name__ == '__main__':
    c=Controlleur()