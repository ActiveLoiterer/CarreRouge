import Vue_carreRouge
import Modele_carreRouge

class Controlleur:
	def __init__(self):
		self.vue = Vue_carreRouge.Vue(self)
		self.jeu = None
		#self.jeu = Modele_carreRouge.Jeu(self.vue.nomJoueur)
		self.gameLoop()
		self.vue.root.mainloop()

	def gameLoop(self):
		if(self.vue.pret == 1):
			self.creerJeu()
			#manque le update des carreBleu	
			self.jeu.updateCarreBleu()
			self.jeu.checkRedSqCollision()
			self.vue.drawPions()
			self.vue.root.after(50,self.gameLoop)

	def creerJeu(self):
		if not self.jeu:
			self.jeu = self.jeu = Modele_carreRouge.Jeu(self.vue.nomJoueur)
			# STARTTIME


if __name__ == '__main__':
    c=Controlleur()