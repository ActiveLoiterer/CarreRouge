import Vue_carreRouge
import Modele_carreRouge

class Controlleur:
	def __init__(self):
		self.jeu = Modele_carreRouge.Jeu()
		self.vue = Vue_carreRouge.Vue(self.jeu,self)
		self.vue.root.mainloop()

	def gameLoop(self):
		if(self.vue.pret == 1):
			if( not self.jeu.joueur.isDead()):
				self.jeu.startTimer()
				self.jeu.calculTempsTotal()
				self.jeu.updateCarreBleu()
				self.jeu.checkRedSqCollision()
				self.vue.updateVue()
				self.vue.root.after(50,self.gameLoop)
			else:
				self.vue.drawMainMenu()
				self.jeu.ecrireHighscore()
				
				
				#self.jeu.ecrireHighscore()

	def refairePartie(self):
		self.jeu = None
		self.jeu = Modele_carreRouge.Jeu()


if __name__ == '__main__':
    c=Controlleur()