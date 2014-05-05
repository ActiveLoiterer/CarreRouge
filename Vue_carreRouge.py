from tkinter import *
from tkinter import messagebox
import sys

class Vue():
	def __init__(self):
		self.root = Tk()
		self.root.title('CarreRouge')
		self.canvasPrincipal = Canvas(self.root,width=700,height=700,bg="black")
		self.drawMainMenu()
		self.listeNom = []
		self.root.mainloop()

	def actionBoutonPlay(self):
		self.drawSurfaceJeu()

	def actionBoutonQuitter(self):
		sys.exit(0)

	def actionBoutonFermerHighscore(self):
		self.canvasPrincipal.delete('highscore')

	def drawListeNomHighscore(self):
		boutonFermerHS = Button(self.root,text="fermer highscore!",width=20,height=2, command= lambda: self.actionBoutonFermerHighscore())
		scrollbar = Scrollbar(self.root)
		listbox = Listbox(self.root,yscrollcommand=scrollbar.set)
		for item in self.listeNom:
			listbox.insert(END,item)
		scrollbar.config(command=listbox.yview)
		self.canvasPrincipal.create_window(550,300,window=listbox,tags='highscore')
		self.canvasPrincipal.create_window(630,300,window=scrollbar,height=160,tags='highscore')
		self.canvasPrincipal.create_window(565,420,window=boutonFermerHS,tags='highscore')


	def actionBoutonHighscore(self):

		# a mettre dans le modele juste tests ici
		highscoreFile = open( "highscore.txt", "r" )
		for line in highscoreFile:
			self.listeNom.append(line.splitlines())
		highscoreFile.close()
		self.drawListeNomHighscore()


	def drawMainMenu(self):
		self.canvasPrincipal.delete('jeu')
		self.boutonPlay = Button(self.root,text="Jouer",width=20,height=5, command= lambda: self.actionBoutonPlay())
		self.boutonQuit = Button(self.root,text="Quitter",width=20,height=5, command= lambda: self.actionBoutonQuitter())
		self.boutonHighscore = Button(self.root,text="Highscore",width=20,height=5, command= lambda: self.actionBoutonHighscore())
		self.canvasPrincipal.create_window(350,200,window=self.boutonPlay,tags='Menu')
		self.canvasPrincipal.create_window(350,400,window=self.boutonQuit,tags='Menu')
		self.canvasPrincipal.create_window(350,300,window=self.boutonHighscore,tags='Menu')
		self.canvasPrincipal.pack()
	
	def drawSurfaceJeu(self):
		self.canvasPrincipal.delete('all')
		self.canvasPrincipal.create_rectangle(30,30,670,670,fill="white",tags='jeu')
		self.drawCarresEnnemi()
		self.drawDialogRejouer()

	def drawJoueur(self):
		pass

	def drawCarresEnnemi(self):
		#tests need real objects
		self.canvasPrincipal.create_rectangle(50,50,150,70,fill="blue",tags='jeu')
		self.canvasPrincipal.create_rectangle(120,120,150,75,fill="blue",tags='jeu')
		self.canvasPrincipal.create_rectangle(500,500,650,600,fill="blue",tags='jeu')
		#self.canvasPrincipal.create_rectangle(60,60,10,10,fill="blue",tags='jeu')
		#self.canvasPrincipal.create_rectangle(15,60,10,10,fill="blue",tags='jeu')

	def drawDialogRejouer(self):
		if(messagebox.askyesno("nouvelle partie","voulez-vous rejouer une partie?",parent=self.canvasPrincipal)):
			self.drawSurfaceJeu()
		else:
			self.drawMainMenu()


if __name__ == '__main__':
    vue = Vue()