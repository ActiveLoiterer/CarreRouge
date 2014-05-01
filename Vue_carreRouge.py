from tkinter import *
import sys

class Vue():
	def __init__(self):
		self.root = Tk()
		self.root.title('CarreRouge')
		self.canvasPrincipal = Canvas(self.root,width=700,height=700,bg="black")
		self.drawMainMenu()
		self.root.mainloop()

	def actionBoutonPlay(self):
		self.drawSurfaceJeu()

	def actionBoutonQuitter(self):
		sys.exit(0)

	def drawMainMenu(self):
		self.boutonPlay = Button(self.root,text="Jouer",width=20,height=5, command= lambda: self.actionBoutonPlay())
		self.boutonQuit = Button(self.root,text="Quitter",width=20,height=5, command= lambda: self.actionBoutonQuitter())
		self.canvasPrincipal.create_window(350,200,window=self.boutonPlay,tags='Menu')
		self.canvasPrincipal.create_window(350,300,window=self.boutonQuit,tags='Menu')
		self.canvasPrincipal.pack()
	
	def drawSurfaceJeu(self):
		self.canvasPrincipal.delete('all')
		self.canvasPrincipal.create_rectangle(30,30,670,670,fill="white",tags='surfaceJeu')

	def drawCarresEnnemi(self):
		self.canvasPrincipal.create_rectangle(40,40,500,500,fill="blue",tags='carreEnnemi')

if __name__ == '__main__':
    vue = Vue()