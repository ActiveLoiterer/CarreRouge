from tkinter import *
from tkinter import messagebox
import sys

class Vue:
	def __init__(self,controlleur):
		self.root = Tk()
		self.root.title('CarreRouge')
		self.controlleur = controlleur
		self.canvasWidth = 500
		self.canvasHeight = 500
		self.canvasPrincipal = Canvas(self.root,width=self.canvasWidth,height=self.canvasHeight,bg="black")
		self.drawMainMenu()
		self.listeNom = []
		self.pret = -1
		self.cliqueSurPion = False
		self.nomJoueur = ""
		self.highscoreOuvert = False
		self.textEntry = Entry(self.canvasPrincipal)
		self.canvasPrincipal.bind("<Button-1>",self.click)
		self.canvasPrincipal.bind("<ButtonRelease>",self.relacheClick)
		self.canvasPrincipal.bind("<Motion>",self.mouseMotion)

	def click(self,event):
		lestags=self.canvasPrincipal.gettags("current")
		if "pion" in lestags:
			self.cliqueSurPion = True

	def mouseMotion(self,event):
		if self.cliqueSurPion and self.controlleur.jeu :
			self.controlleur.jeu.joueur.changePos(event.x,event.y)

	def relacheClick(self,event):
		self.cliqueSurPion = False
			
	def actionBoutonPlay(self):
		self.getNomJoueur()

	def actionBoutonQuitter(self):
		self.canvasPrincipal.delete("all")
		os._exit()

	def actionBoutonFermerHighscore(self):
		self.canvasPrincipal.delete('highscore')
		self.highscoreOuvert = False
		self.drawMainMenu()

	def getNomJoueur(self):
		self.textEntry = Entry(self.canvasPrincipal)
		b = Button(self.canvasPrincipal,text='choisir un nom',command=self.boutonGetJoueur)
		self.canvasPrincipal.create_window(self.canvasWidth/2,self.canvasHeight-100,window=self.textEntry,tags='choixNom')
		self.canvasPrincipal.create_window(self.canvasWidth/2,self.canvasHeight-150,window=b,tags='choixNom')
		self.textEntry.focus_set()

	def boutonGetJoueur(self):
		self.nomJoueur = self.textEntry.get()
		self.pret = 1
		self.controlleur.gameLoop()
		self.drawSurfaceJeu()


	def drawListeNomHighscore(self):
		self.canvasPrincipal.delete('Menu')
		boutonFermerHS = Button(self.root,text="fermer highscore!",width=20,height=2, command= lambda: self.actionBoutonFermerHighscore())
		scrollbar = Scrollbar(self.root)
		listbox = Listbox(self.root,yscrollcommand=scrollbar.set)
		for item in self.listeNom:
			listbox.insert(END,item)
		scrollbar.config(command=listbox.yview)
		self.canvasPrincipal.create_window(self.canvasWidth/2,300,window=listbox,tags='highscore')
		self.canvasPrincipal.create_window(350,300,window=scrollbar,height=160,tags='highscore')
		self.canvasPrincipal.create_window(self.canvasWidth/2,450,window=boutonFermerHS,tags='highscore')


	def actionBoutonHighscore(self):

		# a mettre dans le MODELE juste voir si fonctionne
		if(not self.highscoreOuvert):
			self.controlleur.jeu.lireHighscore()
			self.listeNom = self.controlleur.jeu.getListeNom()
			self.drawListeNomHighscore()
			self.highscoreOuvert = True


	def drawMainMenu(self):
		self.canvasPrincipal.delete('all')
		self.boutonPlay = Button(self.root,text="Jouer",width=20,height=5, command= lambda: self.actionBoutonPlay())
		self.boutonQuit = Button(self.root,text="Quitter",width=20,height=5, command= lambda: self.actionBoutonQuitter())
		self.boutonHighscore = Button(self.root,text="Highscore",width=20,height=5, command= lambda: self.actionBoutonHighscore())
		self.canvasPrincipal.create_window(self.canvasWidth/2,self.canvasHeight-(self.canvasHeight-70),window=self.boutonPlay,tags='Menu')
		self.canvasPrincipal.create_window(self.canvasWidth/2,self.canvasHeight-(self.canvasHeight-270),window=self.boutonQuit,tags='Menu')
		self.canvasPrincipal.create_window(self.canvasWidth/2,self.canvasHeight-(self.canvasHeight-170),window=self.boutonHighscore,tags='Menu')
		self.canvasPrincipal.pack()
	
	def drawSurfaceJeu(self):
		self.canvasPrincipal.delete('all')
		self.canvasPrincipal.create_rectangle(30,30,self.canvasWidth-30,self.canvasHeight-30,fill="white",tags='jeu')
		self.drawPions()

	def drawTemps(self):
		temps = StringVar()
		temps.set(str("{:10.2f}".format(self.controlleur.jeu.getTemps())))
		labelTemps = Label(self.canvasPrincipal,textvariable=temps,fg="black")
		self.canvasPrincipal.create_window(self.canvasWidth/2,15,window=labelTemps,tags='jeu')

	def drawPions(self):
		self.canvasPrincipal.delete('pion')
		self.canvasPrincipal.delete('carreBleu')
		pion = self.controlleur.jeu.joueur
		self.drawTemps()
		self.canvasPrincipal.create_rectangle(pion.posX1,pion.posY1,pion.posX2,pion.posY2,fill="red", tags=("pion"))

		for i in self.controlleur.jeu.listeCarreBleu:
			self.canvasPrincipal.create_rectangle(i.posX1,i.posY1,i.posX2,i.posY2,fill="blue", tags=("carreBleu"))

	def drawDialogRejouer(self):
		if(messagebox.askyesno("nouvelle partie","voulez-vous rejouer une partie?",parent=self.canvasPrincipal)):
			return True
		else:
			return False

