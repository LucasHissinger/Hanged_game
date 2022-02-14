#All Imports
from tkinter import *
from tkinter.font import *
from tkinter.messagebox import *
from random import *
from PIL import Image, ImageTk
from math import *
from pickle import dump,load
import os

class Fenetre:
    '''Classe de création de la fenêtre'''

    def __init__(self):
        '''Initialisation de la fenêtre, sa taille et son titre'''

        self.root = Tk()
        self.root.geometry("900x600")
        self.root.title("Pendu")

    def run(self, image, title, police):
        '''Création du background de la fenêtre (Image Western)'''

        self.Canvas = Canvas(self.root, width = 900, height = 600) #Création du Canvas général
        self.Canvas.pack()

        WesternImg = Image.open("Pendu_IMG" + image) #Image du Background
        WesternImg = WesternImg.resize((900,600))
        WesternPhotoImage = ImageTk.PhotoImage(WesternImg)

        self.Canvas.create_image(0, 0, anchor = NW, image = WesternPhotoImage)
        self.Canvas.image = WesternPhotoImage
        self.CanvasTitle = self.Canvas.create_text(450, 40, text = title, font = police) #Titre du Canvas

    def SupFenetreWidgets(self):
        '''Suppression des Widgets de la fenêtre'''

        for widget in self.Canvas.winfo_children():
            widget.pack_forget()
            widget.destroy()

class FenetreStart:
    '''Classe de création de la fenêtreStart'''

    def run():
        '''Initialisation des Widgets de la fenêtre'''

        #Changement de la fenêtre + Titre

        Main.Canvas.destroy()
        Main.run("/western.jpg", "Jeu du Pendu", ("Lucida Grande", 30))

        # Init Button
        FenetreStart.CreationWidgets()

    def CreationWidgets():
        '''Création des Widgets de la fenêtreStart'''

        #Création des Buttons

        Btn_Solo = Button(Main.Canvas, text="Solo",font = ("Lucida Grande", 20), width = 12, height = 3, borderwidth=2, cursor = "hand2", command = lambda:[FenetreStart.Button_Joueur(Btn_Solo, Btn_Multi, 0, "Solo")])
        Btn_Solo.place(x = 100, y = 200)

        Btn_Multi = Button(Main.Canvas, text="Mutli",font = ("Lucida Grande", 20), width = 12, height = 3, borderwidth=2, cursor = "hand2", command = lambda:[FenetreStart.Button_Joueur(Btn_Solo, Btn_Multi, 1, "Multi")])
        Btn_Multi.place(x = 600, y = 200)

        Btn_Valider = Button(Main.Canvas, text="Valider",font = ("Lucida Grande", 20), width = 18, height = 3, borderwidth=2, cursor = "hand2", command = lambda:[FenetreStart.Valider(Btn_Solo, Btn_Multi)])
        Btn_Valider.place(x = 300, y = 460)

    def Button_Joueur(Btn_Solo, Btn_Multi, Nblist, ModeJoueur):
        '''Prend comme argument : Nblist(Si Solo alors 0, Si Multi alors 1), ModeJoueur(Solo ou Multi)
        -met à jour la variable Joueur(Solo, Multi)
        -met à jour le background des bouttons'''

        Joueur.set(ModeJoueur) #Set Joueur : Solo ou Multi

        #Changement du Background des Buttons

        listJoueur = [(SUNKEN, "#DCDBDB"), (RAISED, "#f0f0f0")]
        listJoueur[0], listJoueur[Nblist] = listJoueur[Nblist], listJoueur[0]
        Btn_Solo.config(relief = listJoueur[0][0], bg = listJoueur[0][1])
        Btn_Multi.config(relief = listJoueur[1][0], bg = listJoueur[1][1])

    def Valider(Btn_Solo, Btn_Multi):
        '''Prend comme argument : Btn_Solo, Btn_Multi
        -test si un des bouttons est activé, si non alors il y a un message d'erreur, à l'inverse on lance le script de la fenêtreNoms'''

        if Btn_Solo['relief'] == RAISED and Btn_Multi['relief'] == RAISED:
            showwarning("Attention", "Veuillez choisir un mode de jeu")
        else :
            FenetreNoms.run("", "") #Changement de Fenêtre : FenetreStart -> FenetreNoms

class FenetreNoms:
    '''Classe de création de la fenêtreNoms'''

    def run(MisesTitre, ModesTitre):
        '''Prend comme arguments : MisesTitre, ModesTitre
        -Initialisation de la fenêtreNoms'''

        #Variables

        mot_ordi = ""
        del list_Noms[0 : ]

        Main.SupFenetreWidgets()
        FenetreNoms.CreationWidgets(mot_ordi, MisesTitre, ModesTitre)

    def CreationWidgets(mot_ordi, MisesTitre, ModesTitre):
        '''Prend comme argument : mot_ordi
        -creation des widgets de la fenêtreNoms'''

        #Init  Label
        Main.Canvas.itemconfig(Main.CanvasTitle, text = "Choix des noms", font = ("Lucida Grande", 30)) #Changement du titre de la Fenêtre

        MisesTitre = Main.Canvas.create_text(440, 300, text = "Mise", font = ("Lucida Grande", 20)) #Création Titre des Mises

        if Joueur.get() == "Solo" :

            mot_ordi = FenetreNoms.SearchAleatoire() #Récupère le mot aléatoire dans mots.txt

            #Création des Titres

            ModesTitre = Main.Canvas.create_text(140, 70, text = "", font = ("Lucida Grande", 20))
            TitreCanvas = Label(Main.Canvas, text = "                 Joueurs               0/1", font = ("Lucida Grande", 15), bg = "#d8d8d8")

            Btn_Valider = Button(Main.Canvas, text="Valider",font = ("Lucida Grande", 18), width = 17, height = 2, borderwidth=2, cursor = "hand2", command = lambda:[FenetreNoms.Valider(Btn_Simple, Btn_Double, Btn_Triple, "", "", mot_ordi, MisesTitre, ModesTitre)])


        else:

            #Création des Titres

            ModesTitre = Main.Canvas.create_text(140, 70, text = "Mode de jeu", font = ("Lucida Grande", 20))
            TitreCanvas = Label(Main.Canvas, text = "               Joueurs               0/4", font = ("Lucida Grande", 15), bg = "#d8d8d8")

            #Création des Buttons

            Btn_MotAléa = Button(Main.Canvas, text="Mot aléatoire",font = ("Lucida Grande", 18), width = 15, height = 2, borderwidth=2, cursor = "hand2", command = lambda:[FenetreNoms.Mot_Aléa(Btn_MotAléa, Btn_MotChoix, True, 0)])
            Btn_MotAléa.place(x = 30, y = 100)

            Btn_MotChoix = Button(Main.Canvas, text="Choisir le mot",font = ("Lucida Grande", 18), width = 15, height = 2, borderwidth=2, cursor = "hand2", command = lambda:[FenetreNoms.Mot_Aléa(Btn_MotAléa, Btn_MotChoix, True, 1)])
            Btn_MotChoix.place(x = 30, y = 180)

            Btn_Valider = Button(Main.Canvas, text="Valider",font = ("Lucida Grande", 18), width = 17, height = 2, borderwidth=2, cursor = "hand2", command = lambda:[FenetreNoms.Valider(Btn_Simple, Btn_Double, Btn_Triple, Btn_MotAléa, Btn_MotChoix, mot_ordi, MisesTitre, ModesTitre)])

        TitreCanvas.place(x = 300, y = 75, width = 300, height = 25)
        Btn_Valider.place(x = 315, y = 490)

        #Création Entry

        NomEntry = Entry(Main.Canvas)
        NomEntry.insert(0, "Ecrire un nom...")
        NomEntry.config(fg = "grey")
        NomEntry.bind("<FocusIn>", lambda e: FenetreNoms.NomEntry_Focus(NomEntry))
        NomEntry.bind("<Return>", lambda e: FenetreNoms.ConfirmerNom(JoueurCanvas, TitreCanvas, NomEntry, CanvasNom1, CanvasNom2, CanvasNom3, CanvasNom4))
        NomEntry.place(x = 300, y = 250, height = 22, width = 200)

        #Créations des Buttons

        Btn_Confirmer = Button(Main.Canvas, text="Confirmer",font = ("Lucida Grande", 10), width = 10, height = 1, borderwidth=2, cursor = "hand2", command = lambda:[FenetreNoms.ConfirmerNom(JoueurCanvas, TitreCanvas, NomEntry, CanvasNom1, CanvasNom2, CanvasNom3, CanvasNom4)])
        Btn_Confirmer.place(x = 505, y = 246)

        Btn_Simple = Button(Main.Canvas, text="Simple",font = ("Lucida Grande", 15), width = 15, height = 2, borderwidth=2, cursor = "hand2", command = lambda:[FenetreNoms.Button_Mise(Btn_Simple, Btn_Double, Btn_Triple, 1)])
        Btn_Simple.place(x = 150, y = 350)

        Btn_Double = Button(Main.Canvas, text="Double",font = ("Lucida Grande", 15), width = 15, height = 2, borderwidth=2, cursor = "hand2", command = lambda:[FenetreNoms.Button_Mise(Btn_Simple, Btn_Double, Btn_Triple, 2)])
        Btn_Double.place(x = 350, y = 350)

        Btn_Triple = Button(Main.Canvas, text="Triple",font = ("Lucida Grande", 15), width = 15, height = 2, borderwidth=2, cursor = "hand2", command = lambda:[FenetreNoms.Button_Mise(Btn_Simple, Btn_Double, Btn_Triple, 3)])
        Btn_Triple.place(x = 550, y = 350)

        Btn_Retour = Button(Main.Canvas, text="Retour",font = ("Lucida Grande", 10), width = 10, height = 1, borderwidth=2, cursor = "hand2", command = lambda:[FenetreNoms.Retour(MisesTitre, ModesTitre)])
        Btn_Retour.place(x = 15, y = 560)

        #Création Canvas des joueurs

        CanvasNom1, CanvasNom2, CanvasNom3, CanvasNom4 = Canvas(), Canvas(), Canvas(), Canvas()

        JoueurCanvas = Canvas(Main.Canvas, height = 132, width = 300, bg = "white", bd=0, highlightthickness=0, relief='ridge')
        JoueurCanvas.place(x = 300, y = 100, height = 132,width = 300)

    def SearchAleatoire():
        '''-met à jour la variable MotAleatoire en True
        -choisi un mot aléatoire dans le fichier mots.txt'''

        MotAleatoire.set(True)

        #Prend un mot aléatoire dans mots.txt

        motsFile = open("Pendu_TXT/mots.txt", "r")
        words = [word.strip() for word in motsFile]
        mot_ordi = choice(words)
        motsFile.close()
        return mot_ordi

    def Mot_Aléa(Btn_MotAléa, Btn_MotChoix, bool, Nblist):
        '''Prend comme arguments : Btn_MotAléa, Btn_MotChoix, bool, Nblist
        -met à jour la variable MotAleatoire en bool : True, False
        -met à jour le background des bouttons'''

        MotAleatoire.set(bool)

        #Changement du background des Buttons

        listJoueur = [(SUNKEN, "#DCDBDB"), (RAISED, "#f0f0f0")]
        listJoueur[0], listJoueur[Nblist] = listJoueur[Nblist], listJoueur[0]
        Btn_MotAléa.config(relief = listJoueur[0][0], bg = listJoueur[0][1])
        Btn_MotChoix.config(relief = listJoueur[1][0], bg = listJoueur[1][1])

    def NomEntry_Focus(NomEntry):
        '''Enlève "Ecrire un nom..." dans l'entrée de texte NomEntry'''

        if NomEntry.get() == "Ecrire un nom...":
            NomEntry.delete(0, END)
            NomEntry.insert(0, '')
            NomEntry.config(fg = "black")

    def ConfirmerNom(JoueurCanvas, TitreCanvas, NomEntry, CanvasNom1, CanvasNom2, CanvasNom3, CanvasNom4):
        '''Prend comme arguments : JoueurCanvas, TitreCanvas, NomEntry, CanvasNom1, CanvasNom2, CanvasNom3, CanvasNom4
        -test si le nom entré est valide (si il est vide ou déjà utilisé) si non alors il y a un message d'erreur, si oui on affiche le nom entré dans un canvas'''

        if NomEntry["state"] == "disabled": #Si il y a le nombre max de joueurs inscrit alors:
            showwarning("Attention", "Veuillez supprimer un nom pour en écrire un nouveau")
        elif NomEntry.get() == "" or NomEntry.get() == "Ecrire un nom...": #Si le joueur confirme sans rien écrire dans l'entrée alors:
            showwarning("Attention", "Veuillez écrire un nom")
        elif NomEntry.get() in list_Noms : #Si le nom entré est déjà choisi par un autre joueur alors:
            showwarning("Attention", "Veuillez écrire un nom inutilisé")
        else:
            list_Noms.append(NomEntry.get()) #Ajout du nom entré dans la list des Noms
            if Joueur1.get() == "" :
                Joueur1.set(NomEntry.get()) #La variable Joueur1 = nom entré

                #Création du Canvas contenant le nom du joueur

                CanvasNom1 = Canvas(JoueurCanvas, width = 297, height = 25, bg = "#E5E5E5", bd=1, highlightthickness=1, relief='ridge')
                ButtonNom1 = Button(Main.root, text="X", font= ("Sans","9","bold"), width = 3, cursor = "hand2", command = lambda:[FenetreNoms.SupNom(NomEntry, CanvasNom1, Joueur1), FenetreNoms.RefreshNbJoueurs(TitreCanvas)])
                CanvasNom1.pack(pady = 2)
                CanvasNom1.create_text(10,15, text = NomEntry.get(), font = ("Lucida Grande", 15), anchor = W)
                CanvasNom1.create_window(284, 15, window = ButtonNom1)

            elif Joueur2.get() == "":
                Joueur2.set(NomEntry.get()) #La variable Joueur2 = nom entré

                #Création du Canvas contenant le nom du joueur

                CanvasNom2 = Canvas(JoueurCanvas, width = 297, height = 25, bg = "#E5E5E5", bd=1, highlightthickness=1, relief='ridge')
                ButtonNom2 = Button(Main.root, text="X", font= ("Sans","9","bold"), width = 3, cursor = "hand2", command = lambda:[FenetreNoms.SupNom(NomEntry, CanvasNom2, Joueur2), FenetreNoms.RefreshNbJoueurs(TitreCanvas)])
                CanvasNom2.pack(pady = 2)
                CanvasNom2.create_text(10,15, text = NomEntry.get(), font = ("Lucida Grande", 15), anchor = W)
                CanvasNom2.create_window(284, 15, window = ButtonNom2)

            elif Joueur3.get() == "":
                Joueur3.set(NomEntry.get()) #La variable Joueur3 = nom entré

                #Création du Canvas contenant le nom du joueur

                CanvasNom3 = Canvas(JoueurCanvas, width = 297, height = 25, bg = "#E5E5E5", bd=1, highlightthickness=1, relief='ridge')
                ButtonNom3 = Button(Main.root, text="X", font= ("Sans","9","bold"), width = 3, cursor = "hand2", command = lambda:[FenetreNoms.SupNom(NomEntry, CanvasNom3, Joueur3), FenetreNoms.RefreshNbJoueurs(TitreCanvas)])
                CanvasNom3.pack(pady = 2)
                CanvasNom3.create_text(10,15, text = NomEntry.get(), font = ("Lucida Grande", 15), anchor = W)
                CanvasNom3.create_window(284, 15, window = ButtonNom3)

            else :
                Joueur4.set(NomEntry.get()) #La variable Joueur4 = nom entré

                #Création du Canvas contenant le nom du joueur

                CanvasNom4 = Canvas(JoueurCanvas, width = 297, height = 25, bg = "#E5E5E5", bd=1, highlightthickness=1, relief='ridge')
                ButtonNom4 = Button(Main.root, text="X", font= ("Sans","9","bold"), width = 3, cursor = "hand2", command = lambda:[FenetreNoms.SupNom(NomEntry, CanvasNom4, Joueur4), FenetreNoms.RefreshNbJoueurs(TitreCanvas)])
                CanvasNom4.pack(pady = 2)
                CanvasNom4.create_text(10,15, text = NomEntry.get(), font = ("Lucida Grande", 15), anchor = W)
                CanvasNom4.create_window(284, 15, window = ButtonNom4)

            FenetreNoms.RefreshNbJoueurs(TitreCanvas)

            NomEntry.delete(0, END)

        #Test si le nombre max de joueur est atteint

        if len(list_Noms) >= 4 and Joueur.get() == "Multi":
            NomEntry["state"] = "disabled"
        elif len(list_Noms) >= 1 and Joueur.get() == "Solo":
            NomEntry["state"] = "disabled"

    def RefreshNbJoueurs(TitreCanvas):
        '''Prend comme argument : TitreCanvas
        -actualise le compteur des joueurs dans le TitreCanvas'''

        if Joueur.get() == "Multi" :
            TitreCanvas.config(text = "               Joueurs               "+ str(len(list_Noms)) + "/4")
        else :
            TitreCanvas.config(text = "                Joueurs                "+ str(len(list_Noms)) + "/1")

    def SupNom(NomEntry, CanvasNom, JoueurNom):
        '''Prend comme arguments : NomEntry, CanvasNom, JoueurNom
        -permet de supprimer un joueur'''

        list_Noms.remove(JoueurNom.get())
        JoueurNom.set("")
        CanvasNom.destroy()
        NomEntry["state"] = "normal"

    def Button_Mise(Btn_Simple, Btn_Double, Btn_Triple, nbMise):
        '''Prend comme arguments : Btn_Simple, Btn_Double, Btn_Triple, nbMise
        -met à jour la variable modeMise en nbMise
        -met à jour le background des bouttons de mises'''

        modeMise.set(nbMise) #Set modeMise : 1, 2 ou 3

        listMise = [(SUNKEN, "#DCDBDB"), (RAISED, "#f0f0f0"), (RAISED, "#f0f0f0")]
        listMise[0], listMise[nbMise-1] = listMise[nbMise-1], listMise[0]
        Btn_Simple.config(relief = listMise[0][0], bg = listMise[0][1])
        Btn_Double.config(relief = listMise[1][0], bg = listMise[1][1])
        Btn_Triple.config(relief = listMise[2][0], bg = listMise[2][1])

    def Valider(Btn_Simple, Btn_Double, Btn_Triple, Btn_MotAléa, Btn_MotChoix, mot_ordi, MisesTitre, ModesTitre):
        '''Prend comme arguments : Btn_Simple, Btn_Double, Btn_Triple, Btn_MotAléa, Btn_MotChoix, mot_ordi, MisesTitre, ModesTitre
        -test si les joueurs, les modes et les mises sont valides, si non alors il y a un message d'erreur'''

        if len(list_Noms) == 0: #Si le joueur Valide et qu'il n'y a aucun joueur inscrit
            showwarning("Attention", "Veuillez ajouter des joueurs")
        elif Btn_Simple["relief"] == RAISED and Btn_Double["relief"] == RAISED and Btn_Triple["relief"] == RAISED : #Si le joueur Valide et qu'aucune mise n'est choisie
            showwarning("Attention", "Veuillez choisir une mise")
        else :
            if Joueur.get() == "Multi" :
                if len(list_Noms) <= 1 : #Si le joueur Valide et qu'il y a moins de 2 joueurs inscrit
                    showwarning("Attention", "Veuillez rentrer un minimum de 2 joueurs")
                elif Btn_MotAléa['relief'] == RAISED and Btn_MotChoix['relief'] == RAISED: #Si le joueur Valide et qu'aucun mode de jeu n'est choisi
                    showwarning("Attention", "Veuillez choisir un mode de jeu")
                elif Btn_MotChoix["relief"] == SUNKEN :
                    MotAleatoire.set(False)
                    FenetreChoix.run(MisesTitre, ModesTitre) #Changement de Fenêtre : FenetreNoms -> FenetreChoix
                elif Btn_MotAléa["relief"] ==  SUNKEN :
                    mot_ordi = FenetreNoms.SearchAleatoire()
                    FenetreJeu.run(mot_ordi, "None", MisesTitre, ModesTitre) #Changement de Fenêtre : FenetreNoms -> FenetreJeu
            else :
                FenetreJeu.run(mot_ordi, "None", MisesTitre, ModesTitre) #Changement de Fenêtre : FenetreNoms -> FenetreJeu

    def Retour(MisesTitre, ModesTitre):
        '''Prend comme arguments : MisesTitre, ModesTitre
        -retire les titres MisesTitre et ModesTitres
        -retourne à la fenêtre précédente'''

        Main.Canvas.itemconfig(MisesTitre, text = "")
        Main.Canvas.itemconfig(ModesTitre, text = "")
        FenetreStart.run() #Changement de Fenêtre : FenetreNoms -> FenetreStart


class FenetreChoix:
    '''Classe de création de la fenêtreChoix'''

    def run(MisesTitre, ModesTitre):
        '''Prend comme arguments : MisesTitre, ModesTitre
        -Initialisation de la fenêtreChoix'''

        Main.SupFenetreWidgets()

        #Variables

        Mot_Joueur = StringVar()
        Mot_Joueur.set("")
        JoueurChoisi = choice(list_Noms) #Choix d'un joueur aléatoire
        list_Noms.remove(JoueurChoisi) #Suppression de ce joueur dans la list des Noms

        FenetreChoix.CreationWidgets(Mot_Joueur, MisesTitre, ModesTitre, JoueurChoisi)

    def CreationWidgets(Mot_Joueur, MisesTitre, ModesTitre, JoueurChoisi):
        '''Prend comme arguments : Mot_Joueur, MisesTitre, ModesTitre, JoueurChoisi
        -création des widgets de la fenêtreChoix'''

        #Création des Titres

        Main.Canvas.itemconfig(Main.CanvasTitle, text = "Choix du mot", font = ("Lucida Grande", 25))
        Main.Canvas.itemconfig(MisesTitre, text = "")
        Main.Canvas.itemconfig(ModesTitre, text = "")

        JoueurLabel = Label(Main.Canvas, text = JoueurChoisi + " choisissez un mot", font = ("Lucida Grande", 12), bg = "#d8d8d8")
        JoueurLabel.place(x = 330, y = 129, width = 200, height = 25)

        MotLabel = Main.Canvas.create_text(440, 250, text = "", font = ("Lucida Grande", 20))

        #Création Entry

        MotEntry = Entry(Main.Canvas)
        MotEntry.insert(0, "Ecrire un mot...")
        MotEntry.config(fg = "grey")
        MotEntry.bind("<FocusIn>", lambda e: FenetreChoix.MotEntry_Focus(MotEntry))
        MotEntry.bind("<Return>", lambda e: FenetreChoix.Confirmer(Mot_Joueur, MotEntry, MotLabel))
        MotEntry.place(x = 330, y = 150, width = 200, height = 25)

        #Cration des Buttons

        Btn_Confirmer = Button(Main.Canvas, text="Confirmer",font = ("Lucida Grande", 11), width = 10, height = 1, borderwidth=2, cursor = "hand2", command = lambda:[FenetreChoix.Confirmer(Mot_Joueur, MotEntry, MotLabel)])
        Btn_Confirmer.place(x = 540, y = 149)

        Btn_Valider = Button(Main.Canvas, text="Valider",font = ("Lucida Grande", 18), width = 17, height = 2, borderwidth=2, cursor = "hand2", command = lambda:[FenetreChoix.Valider(Mot_Joueur, JoueurChoisi, MotLabel, MisesTitre, ModesTitre)])
        Btn_Valider.place(x = 315, y = 490)

        Btn_Retour = Button(Main.Canvas, text="Retour",font = ("Lucida Grande", 10), width = 10, height = 1, borderwidth=2, cursor = "hand2", command = lambda:[FenetreChoix.Retour(MotLabel, MisesTitre, ModesTitre)])
        Btn_Retour.place(x = 15, y = 560)

    def Confirmer(Mot_Joueur, MotEntry, MotLabel):
        '''Prend comme arguments : Mot_Joueur, MotEntry, MotLabel
        -test si le mot choisi est valide si non il y a un message d'erreur'''

        accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
        sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
        if len(MotEntry.get()) <= 2: #Si le mot entré est inférieur à 3 lettres alors:
            showwarning("Attention", "Veuillez entrez un mot de minimum 3 lettres")
        elif MotEntry.get().isalpha() : #Si le mot ne contient que des lettres de l'alphabet
            Mot_Joueur.set(MotEntry.get()) #Set Mot_Joueur : mot entré
            for i in range(len(accent)): #Enlève les accents
                Mot_Joueur.set(Mot_Joueur.get().replace(accent[i], sans_accent[i]))
            MotEntry.delete(0, END)
            Main.Canvas.itemconfig(MotLabel, text = "Votre mot est : " + Mot_Joueur.get()) #Création du mot au milieu de l'écran
        else :
            showwarning("Attention", "Veuillez entrez un mot qu'avec des lettres")

    def MotEntry_Focus(MotEntry):
        '''Prend comme arguments : MotEntry
        -Efface "Ecrire un mot..." dans l'entrée MotEntry'''

        if MotEntry.get() == "Ecrire un mot...":
            MotEntry.delete(0, END)
            MotEntry.insert(0, '')
            MotEntry.config(fg = "black")

    def Valider(Mot_Joueur, JoueurChoisi, MotLabel, MisesTitre, ModesTitre):
        '''Prend comme arguments : JoueurChoisi, MotLabel, MisesTitre, ModesTitre
        -test si un mot a bien été pris en compte'''

        if  Mot_Joueur.get() == "" : #Si le joueur confirme sans rien écrire dans l'entrée
            showwarning("Attention", "Veuillez entrer un mot")
        else :
            Main.Canvas.delete(MotLabel) #Efface le mot au milieu de l'écran
            FenetreJeu.run(Mot_Joueur.get(), JoueurChoisi, MisesTitre, ModesTitre) #Changement de Fenêtre : FenetreChoix -> FenetreJeu

    def Retour(MotLabel, MisesTitre, ModesTitre):
        '''Prend comme arguments : MotLabel, MisesTitre, ModesTitre
        -retourne à la fenêtre précédente'''

        Main.Canvas.itemconfig(MotLabel, text = "")
        FenetreNoms.run(MisesTitre, ModesTitre) #Changement de Fenêtre : FenetreChoix -> FenetreNoms



class FenetreJeu:
    '''Classe de création de la fenêtreJeu'''

    def run(mot_pendu, JoueurChoisi, MisesTitre, ModesTitre):
        '''Prend comme arguments : mot_pendu, JoueurChoisi, MisesTitre, ModesTitre
        -Initialisation de la fenêtreJeu'''

        Main.SupFenetreWidgets()

        #Variables

        mot_pendu = mot_pendu.upper()
        lastJoueur = ""
        mot_tiret = (["-" for i in range(len(mot_pendu))]) #mot_tiret = mot_pendu en tiret -
        vies = IntVar()
        vies.set(8)
        lettreDit = []
        CompteurJoueur = IntVar()
        CompteurJoueur.set(randint(0,len(list_Noms)-1)) #Set Compteur : nombre aléatoire selon le nombre de joueurs

        FenetreJeu.CreationWidgets(mot_pendu, JoueurChoisi, mot_tiret, vies, lettreDit, CompteurJoueur, lastJoueur, MisesTitre, ModesTitre)

    def CreationWidgets(mot_pendu, JoueurChoisi, mot_tiret, vies, lettreDit, CompteurJoueur, lastJoueur, MisesTitre, ModesTitre):
        '''Prend comme arguments : mot_pendu, JoueurChoisi, mot_tiret, vies, lettreDit, CompteurJoueur, lastJoueur, MisesTitre, ModesTitre
        -création des widgets de la fenêtreJeu'''

        Main.Canvas.itemconfig(MisesTitre, text = "")
        Main.Canvas.itemconfig(ModesTitre, text = "")

        #Création du Titre

        Main.Canvas.itemconfig(Main.CanvasTitle, text = "Pendu", font = ("Lucida Grande", 20))

        #Création des Labels

        JoueurLabel = Label(Main.Canvas, text = list_Noms[CompteurJoueur.get()], font = ("Lucida Grande", 15), anchor = CENTER, bg = "#d8d8d8")
        JoueurLabel.place(x = 350, y = 535, width = 150)

        LettreLabel = Main.Canvas.create_text(750, 200, text = "", font = ("Lucida Grande", 20))

        #Créatoin des images

        HeartImg, PenduImg = Image.open("Pendu_IMG/Vies.png"), Image.open("Pendu_IMG/Pendu_0.png")
        HeartImg, PenduImg = HeartImg.resize((200,200)), PenduImg.resize((400,324))
        HeartPhotoImage, PenduPhotoImage = ImageTk.PhotoImage(HeartImg), ImageTk.PhotoImage(PenduImg)

        Main.Canvas.create_image(800,90, image = HeartPhotoImage)
        PenduImage = Main.Canvas.create_image(400, 230, image = PenduPhotoImage)
        Main.Canvas.image = Main.Canvas.image, PenduPhotoImage, HeartPhotoImage

        textHeartPrinc = Main.Canvas.create_text(800, 80, text= str(vies.get()), font = ("Lucida Grande", 45)) #Nombre de vies dans le coeur
        Main.Canvas.create_text(800,120, text="vies", font = ("Lucida Grande", 12))

        #Création du Canvas

        JoueurCanvas = Canvas(Main.Canvas, height = 200, width = 200, bg = "white", bd=0, highlightthickness=0, relief='ridge')
        JoueurCanvas.place(x = 40, y = 70)

        #Création du Titre

        TitreCanvas = Label(Main.Canvas, text = "Joueurs", font = ("Lucida Grande", 15), bg = "#d8d8d8")
        TitreCanvas.place(x = 40, y = 45, width = 200, height = 25)

        FenetreJeu.Line(mot_pendu)

        #Création des Canvas des noms des joueurs

        CanvasNom1, CanvasNom2, CanvasNom3, CanvasNom4 = Canvas(Main.Canvas), Canvas(Main.Canvas), Canvas(Main.Canvas), Canvas(Main.Canvas)

        if len(list_Noms) == 1:
            CanvasNom1 = FenetreJeu.CanvasJoueur(JoueurCanvas, CanvasNom1, 0)
        elif len(list_Noms) == 2:
            CanvasNom1, CanvasNom2 = FenetreJeu.CanvasJoueur(JoueurCanvas, CanvasNom1, 0), FenetreJeu.CanvasJoueur(JoueurCanvas, CanvasNom2, 1)
        elif len(list_Noms) == 3:
            CanvasNom1, CanvasNom2, CanvasNom3 = FenetreJeu.CanvasJoueur(JoueurCanvas, CanvasNom1, 0), FenetreJeu.CanvasJoueur(JoueurCanvas, CanvasNom2, 1), FenetreJeu.CanvasJoueur(JoueurCanvas, CanvasNom3, 2)
        else :
            CanvasNom1, CanvasNom2, CanvasNom3, CanvasNom4 = FenetreJeu.CanvasJoueur(JoueurCanvas, CanvasNom1, 0), FenetreJeu.CanvasJoueur(JoueurCanvas, CanvasNom2, 1), FenetreJeu.CanvasJoueur(JoueurCanvas, CanvasNom3, 2), FenetreJeu.CanvasJoueur(JoueurCanvas, CanvasNom4, 3)

        FenetreJeu.SwitchBGJoueur(CanvasNom1, CanvasNom2, CanvasNom3, CanvasNom4, CompteurJoueur)

        #Création du Button

        Btn_Confirmer = Button(Main.Canvas, text="Confirmer",font = ("Lucida Grande", 9), width = 8, height = 1, borderwidth=2, cursor = "hand2", command = lambda:[FenetreJeu.Confirmer(LettreLabel, lettreDit, LettreEntry, vies, CompteurJoueur, JoueurChoisi, mot_pendu, mot_tiret, JoueurLabel, CanvasNom1, CanvasNom2, CanvasNom3, CanvasNom4, textHeartPrinc, PenduImage)])
        Btn_Confirmer.place(x = 505, y = 560)

        #Création Entry

        LettreEntry = Entry(Main.Canvas)
        LettreEntry.place(x = 350, y = 560, width = 150, height = 25)
        LettreEntry.bind("<Return>", lambda e: FenetreJeu.Confirmer(LettreLabel, lettreDit, LettreEntry, vies, CompteurJoueur, JoueurChoisi, mot_pendu, mot_tiret, JoueurLabel, CanvasNom1, CanvasNom2, CanvasNom3, CanvasNom4, textHeartPrinc, PenduImage))

    def SwitchBGJoueur(CanvasNom1, CanvasNom2, CanvasNom3, CanvasNom4, CompteurJoueur):
        '''Prend comme arguments : CanvasNom1, CanvasNom2, CanvasNom3, CanvasNom4, CompteurJoueur
        -change les backgrounds des CanvasNom'''

        listBG = ["#B2B2B2","#E5E5E5", "#E5E5E5", "#E5E5E5"]
        listBG[0], listBG[CompteurJoueur.get()] = listBG[CompteurJoueur.get()], listBG[0]
        CanvasNom1.config(bg = listBG[0])
        CanvasNom2.config(bg = listBG[1])
        CanvasNom3.config(bg = listBG[2])
        CanvasNom4.config(bg = listBG[3])

    def CanvasJoueur(JoueurCanvas, CanvasNom, Nblist):
        '''Prend comme arguments : JoueurCanvas, CanvasNom, Nblist
        -créer un CanvasNom et contient le nom du joueur associé à celui-ci'''

        CanvasNom = Canvas(JoueurCanvas, width = 197, height = 25, bg = "#E5E5E5", bd=1, highlightthickness=1, relief='ridge')
        CanvasNom.pack(pady = 2)
        CanvasNom.create_text(10,15, text = list_Noms[Nblist], font = ("Lucida Grande", 15), anchor = "w")
        return CanvasNom

    def Line(mot_pendu):
        '''Prend comme argument : mot_pendu
        -créer les lignes du pendu'''

        Tiret = ""
        for i in mot_pendu:
            Tiret += "__  "
        Line = Main.Canvas.create_text(450, 470, text = Tiret, font = ("Lucida Grande", 30))

    def Confirmer(LettreLabel, lettreDit, LettreEntry, vies, CompteurJoueur, JoueurChoisi, mot_pendu, mot_tiret, JoueurLabel, CanvasNom1, CanvasNom2, CanvasNom3, CanvasNom4, textHeartPrinc, PenduImage):
        '''Prend comme arguments : lettreDit, LettreEntry, vies, CompteurJoueur, JoueurChoisi, mot_pendu, mot_tiret, JoueurLabel, CanvasNom1, CanvasNom2, CanvasNom3, CanvasNom4, textHeartPrinc, PenduImage
        -test si la lettre ou le mot entré est dans le mot_pendu'''

        if LettreEntry.get() == "": #Si le joueur confirme sans rien écrire dans l'entrée
            showwarning("Attention", "Veuillez entrer une lettre ou un mot")
        else:
            Main.Canvas.itemconfig(LettreLabel, text = "Dernière lettre : " + LettreEntry.get())
        if len(LettreEntry.get()) >= 2 and LettreEntry.get().upper() != mot_pendu: #Si le joueur écrit + d'une lettre et que son mot n'est pas égale au mot_pendu alors:
            LettreEntry.delete(0, END)
            if FenetreJeu.PerdreVie(vies, CompteurJoueur, JoueurChoisi, mot_pendu, textHeartPrinc, PenduImage):
                    return
        elif LettreEntry.get().upper() == mot_pendu:
                FenetreFin.run(vies, list_Noms[CompteurJoueur.get()], JoueurChoisi, mot_pendu)
                return
        else:
            if LettreEntry.get().upper() not in mot_pendu or LettreEntry.get().upper() in mot_tiret: #Si la lettre entré n'est pas dans le mot ou qu'elle a déjà été utilisée
                LettreEntry.delete(0, END)
                if FenetreJeu.PerdreVie(vies, CompteurJoueur, JoueurChoisi, mot_pendu, textHeartPrinc, PenduImage): #Si le joueur perd une vie et qu'il atteint 0 vies alors:
                    return
            else :
                if FenetreJeu.Pendu(LettreEntry, lettreDit, mot_pendu, mot_tiret, CompteurJoueur, JoueurChoisi, vies): #Si le joueur à trouvé le mot_pendu:
                    return
        if len(list_Noms) != 1:

            #Mise à jour du Compteur + du nom afficher

            if CompteurJoueur.get() == len(list_Noms) - 1:
                CompteurJoueur.set(0)
                JoueurLabel.config(text = list_Noms[CompteurJoueur.get()])
            else :
                CompteurJoueur.set(CompteurJoueur.get() + 1)
                JoueurLabel.config(text = list_Noms[CompteurJoueur.get()])
        FenetreJeu.SwitchBGJoueur(CanvasNom1, CanvasNom2, CanvasNom3, CanvasNom4, CompteurJoueur)

    def PerdreVie(vies, CompteurJoueur, JoueurChoisi, mot_pendu, textHeartPrinc, PenduImage):
        '''Prend comme arguments : vies, CompteurJoueur, JoueurChoisi, mot_pendu, textHeartPrinc, PenduImage
        -retire une vie
        -actualise les dessins'''

        vies.set(vies.get() - 1) #Perd une vie

        #Changement des images

        Main.Canvas.itemconfig(textHeartPrinc, text=str(vies.get()))
        PenduImg = Image.open("Pendu_IMG\Pendu_" + str(8 - vies.get()) + ".png")
        PenduImg = PenduImg.resize((400,324))
        PenduPhotoImage = ImageTk.PhotoImage(PenduImg)
        Main.Canvas.itemconfig(PenduImage, image = PenduPhotoImage)
        Main.Canvas.image = Main.Canvas.image, PenduPhotoImage

        if vies.get() == 0:
            FenetreFin.run(vies, list_Noms[CompteurJoueur.get()], JoueurChoisi, mot_pendu) #Changemetn de la fenêtre : FenetreJeu -> FenetreFin
            return True

    def Pendu(LettreEntry, lettreDit, mot_pendu, mot_tiret, CompteurJoueur, JoueurChoisi, vies):
        '''Prend comme arguments : LettreEntry, lettreDit, mot_pendu, mot_tiret, CompteurJoueur, JoueurChoisi, vies
        -recherche la lettre entrée dans le mot
        -affiche la lettre sur sa ligne respective'''

        lettreChoisi = LettreEntry.get().upper() #LettreChoisi = la lettre entrée en majuscule

        for i in range(len(mot_pendu)): #Parcourt les lettres du mot_pendu
            if lettreChoisi == mot_pendu[i]: #Si la lettre entré est la même que celle à l'index i du mot_pendu
                del mot_tiret[i] #Enlève un le tiret à l'index i du mot_tiret
                mot_tiret.insert(i, lettreChoisi) #Ajouter la lettre entrée à l'index i du mot_tiret
                if len(mot_pendu)%2 == 0: #Si le nombre de lettre du mot_pendu est pair
                    if i == ceil(len(mot_pendu)/2): #Si i est égale à l'arrondi au supérieur de la moitié du nombre de lettre du mot_pendu
                        Main.Canvas.create_text(470, 465, text = lettreChoisi, font = ("Lucida Grande", 40))
                    elif i > ceil(len(mot_pendu)/2): #Si i est supérieur à l'arrondi au supérieur de la moitié du nombre de lettre du mot_pendu
                        Main.Canvas.create_text(475+(i-ceil(len(mot_pendu)/2))*65, 465, text = lettreChoisi, font = ("Lucida Grande", 40))
                    elif i == ceil(len(mot_pendu)/2)-1: #Si i est égale à l'arrondi à l'inférieur de la moitié du nombre de lettre du mot_pendu
                        Main.Canvas.create_text(407, 465, text = lettreChoisi, font = ("Lucida Grande", 40))
                    else:
                        Main.Canvas.create_text(470-(ceil(len(mot_pendu)/2)-i)*65, 465, text = lettreChoisi, font = ("Lucida Grande", 40))
                else :
                    if i == ceil(len(mot_pendu)/2): #Si i est égale à l'arrondi au supérieur de la moitié du nombre de lettre du mot_pendu
                       Main.Canvas.create_text(505, 465, text = lettreChoisi, font = ("Lucida Grande", 40))
                    elif i > ceil(len(mot_pendu)/2): #Si i est supérieur à l'arrondi au supérieur de la moitié du nombre de lettre du mot_pendu
                        Main.Canvas.create_text(505+(i-ceil(len(mot_pendu)/2))*65, 465, text = lettreChoisi, font = ("Lucida Grande", 40))
                    elif i == ceil(len(mot_pendu)/2)-1: #Si i est égale à l'arrondi à l'inférieur de la moitié du nombre de lettre du mot_pendu
                        Main.Canvas.create_text(437, 465, text = lettreChoisi, font = ("Lucida Grande", 40))
                    else:
                        Main.Canvas.create_text(500-(ceil(len(mot_pendu)/2)-i)*65, 465, text = lettreChoisi, font = ("Lucida Grande", 40))
        LettreEntry.delete(0, END)
        if mot_tiret.count("-") == 0: #Si il n'y a plus de tiret dans mot_tiret
            FenetreFin.run(vies, list_Noms[CompteurJoueur.get()], JoueurChoisi, mot_pendu) #Changement de fenêtre -> FenetreJeu -> FenetreFin
            return True

class FenetreFin:
    '''Classe de création de la fenêtreFin'''

    def run(vies, lastJoueur, JoueurChoisi, mot_pendu):
        '''Prend comme arguments : vies, lastJoueur, JoueurChoisi, mot_pendu
        -initialisation de la fenêtreFin
        -enregistrement des scores'''

        Main.Canvas.destroy()
        Main.run("\western.jpg", "", ("Lucida Grande", 30))

        #Variables

        #Récupère les scores déjà enregistré et les stock dans dic_Score
        dic_Score = {}
        file = open("Pendu_TXT/Score.txt",'rb')
        if os.stat("Pendu_TXT/Score.txt").st_size > 2:
            dic_Score = load(file)
        file.close()

        dic_Score = FenetreFin.CalculScore(vies, dic_Score, JoueurChoisi, lastJoueur) #Calcul des Scores

        #Enregistrement des Scores
        file=open("Pendu_TXT\Score.txt",'wb')
        dump(dic_Score,file)
        file.close()

        FenetreFin.CreationWidgets(vies, lastJoueur, JoueurChoisi, mot_pendu, dic_Score)

    def CreationWidgets(vies, lastJoueur, JoueurChoisi, mot_pendu, dic_Score):
        '''Prend comme arguments : vies, lastJoueur, JoueurChoisi, mot_pendu, dic_Score
        -création des widgets de la fenêtreFin'''

        #Création des Titres

        if vies.get() != 0:
            Main.Canvas.itemconfig(Main.CanvasTitle, text = "Bravo " + lastJoueur + " !")
        elif MotAleatoire.get():
            Main.Canvas.itemconfig(Main.CanvasTitle, text = "Vous avez perdu")
        else :
            Main.Canvas.itemconfig(Main.CanvasTitle, text = "Bravo " + JoueurChoisi + " !")

        #Création des Images

        PenduImg = Image.open("Pendu_IMG\Pendu_" + str(8 - vies.get()) + ".png")
        PenduImg = PenduImg.resize((400,324))
        PenduPhotoImage = ImageTk.PhotoImage(PenduImg)

        PenduImage = Main.Canvas.create_image(400, 230, image = PenduPhotoImage)
        Main.Canvas.image = Main.Canvas.image, PenduPhotoImage

        ShowMot = Main.Canvas.create_text(450, 450, text = "Le mot était " + mot_pendu, font = ("Lucida Grande", 20))

        #Création des Buttons

        Btn_Rejouer = Button(Main.Canvas, text="Rejouer",font = ("Lucida Grande", 18), width = 12, height = 2, cursor = "hand2", borderwidth=2,command = lambda:[FenetreStart.run()])
        Btn_Rejouer.place(x = 50, y = 500)

        Btn_Arreter = Button(Main.Canvas, text="Arreter",font = ("Lucida Grande", 18), width = 12, height = 2, borderwidth=2, cursor = "hand2", command = lambda:[Main.root.destroy(), quit()])
        Btn_Arreter.place(x = 350, y = 500)

        Btn_Classement = Button(Main.Canvas, text="Classement",font = ("Lucida Grande", 18), width = 12, height = 2, borderwidth=2, cursor = "hand2", command = lambda:[FenetreClassement.run(vies, lastJoueur, JoueurChoisi, mot_pendu, dic_Score)])
        Btn_Classement.place(x = 650, y = 500)

        list_Noms.clear() #Vide la list Noms

    def CalculScore(vies, dic_Score, JoueurChoisi, lastJoueur):
        '''Prend comme arguments : vies, dic_Score, JoueurChoisi, lastJoueur
        -calcul les scores'''

        if vies.get() == 0 and len(list_Noms) != 0: #Si il n'y a plus de vies est que la list Noms n'est pas vide
            for i in range(len(list_Noms)): #Parcourt des joueurs dans la list Noms
                if list_Noms[i] in dic_Score: #Si le joueur existe déjà dans les scores enregistrés
                    dic_Score[list_Noms[i]] -= 10*modeMise.get()
                else :
                    dic_Score[list_Noms[i]] = -10*modeMise.get()
            if not MotAleatoire.get(): #Si le mot_pendu à était choisi par un joueur
                if JoueurChoisi in dic_Score: #Si le joueur qui a choisi le mot existe déjà dans les scores enregistrés
                    dic_Score[JoueurChoisi] += (10 + 2*vies.get()) * modeMise.get()
                else :
                    dic_Score[JoueurChoisi] = (10 + 2*vies.get()) * modeMise.get()
        if vies.get() != 0 and len(list_Noms) != 0: #Si il y a encore des vies est que la list Noms n'est pas vide
            if lastJoueur in dic_Score: #Si le dernier joueur existe déjà dans les scores enregistrés
                dic_Score[lastJoueur] += (10 + 2*vies.get()) * modeMise.get()
                list_Noms.remove(lastJoueur) #Suppression du dernier joueur ds la list Noms
                for i in range(len(list_Noms)): #Parcourt des joueurs dans la list Noms
                    if list_Noms[i] in dic_Score: #Si le joueur existe déjà dans les scores enregistrés
                        dic_Score[list_Noms[i]] -= 10*modeMise.get()
                    else :
                        dic_Score[list_Noms[i]] = -10*modeMise.get()
            else:
                dic_Score[lastJoueur] = (10 + 2*vies.get()) * modeMise.get()
                list_Noms.remove(lastJoueur) #Suppression du dernier joueur ds la list Noms
                for i in range(len(list_Noms)): #Parcourt des joueurs dans la list Noms
                    if list_Noms[i] in dic_Score: #Si le joueur existe déjà dans les scores enregistrés
                        dic_Score[list_Noms[i]] -= 10*modeMise.get()
                    else :
                        dic_Score[list_Noms[i]] = -10*modeMise.get()
            if not MotAleatoire.get(): #Si le mot_pendu à était choisi par un joueur
                if JoueurChoisi in dic_Score: #Si le joueur qui a choisi le mot existe déjà dans les scores enregistrés
                    dic_Score[JoueurChoisi] -= 10*modeMise.get()
                else :
                    dic_Score[JoueurChoisi] = -10*modeMise.get()
        return dic_Score

class FenetreClassement:
    '''Classe de création de la fenêtreClassement'''

    def run(vies, lastJoueur, JoueurChoisi, mot_pendu, dic_Score):
        '''Prend comme arguments : vies, lastJoueur, JoueurChoisi, mot_pendu, dic_Score
        -Initialise la fenêtreClassement'''

        Main.Canvas.destroy()
        Main.run("/Board.png", "", ("", 1))

        #Variables

        list_classement = []
        ScrollNb = IntVar()
        ScrollNb.set(0)

        FenetreClassement.CreationWidgets(vies, lastJoueur, JoueurChoisi, mot_pendu, dic_Score, list_classement, ScrollNb)

    def CreationWidgets(vies, lastJoueur, JoueurChoisi, mot_pendu, dic_Score, list_classement, ScrollNb):
        '''Prend comme arguments : list_classement, ScrollNb
        -création des widgets de la fenêtreClassement'''

        #Création des Images

        PodiumImg = Image.open("Pendu_IMG/Sign.png")
        PodiumImg = PodiumImg.resize((400,500))
        PodiumPhotoImage = ImageTk.PhotoImage(PodiumImg)

        PodiumImage = Main.Canvas.create_image(620,200, image = PodiumPhotoImage)

        PosterImg = Image.open("Pendu_IMG/WantedPoster.png")
        PosterImg = PosterImg.resize((268,402))
        PosterPhotoImage = ImageTk.PhotoImage(PosterImg)

        PosterImage = Main.Canvas.create_image(200,280, image = PosterPhotoImage)

        UpArrowImg, DownArrowImg = Image.open("Pendu_IMG/FlecheHaut.png"), Image.open("Pendu_IMG/FlecheBas.png")
        UpArrowImg, DownArrowImg  = UpArrowImg.resize((26,30)), DownArrowImg.resize((26,30))
        UpArrowPhotoImage, DownArrowPhotoImage = ImageTk.PhotoImage(UpArrowImg), ImageTk.PhotoImage(DownArrowImg)

        UpArrowImage = Main.Canvas.create_image(102,405, image = UpArrowPhotoImage, tag='ChangeCursor')
        DownArrowImage = Main.Canvas.create_image(305,405, image = DownArrowPhotoImage, tag='ChangeCursor')

        Main.Canvas.image = Main.Canvas.image, PodiumPhotoImage, PosterPhotoImage, UpArrowPhotoImage, DownArrowPhotoImage

        #Création des text sur le podium

        Place1Podium = Main.Canvas.create_text(510, 362, text = "", font = ("Lucida Grande", 18), anchor = W)
        Place2Podium = Main.Canvas.create_text(510, 395, text = "", font = ("Lucida Grande", 18), anchor = W)
        Place3Podium = Main.Canvas.create_text(510, 425, text = "", font = ("Lucida Grande", 18), anchor = W)

        #Création des Buttons

        ButtonNom1 = Button(Main.Canvas, font = ("Lucida Grande", 12),height = 1, width = 22, cursor = "hand2", command = lambda: [FenetreClassement.Btn_Nom(0, dic_Score, ScrollNb, ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, Place1Podium, Place2Podium, Place3Podium, "")])
        ButtonNom2 = Button(Main.Canvas, font = ("Lucida Grande", 12),height = 1, width = 22, cursor = "hand2", command = lambda:[FenetreClassement.Btn_Nom(1, dic_Score, ScrollNb, ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, Place1Podium, Place2Podium, Place3Podium, "")])
        ButtonNom3 = Button(Main.Canvas, font = ("Lucida Grande", 12),height = 1, width = 22, cursor = "hand2", command = lambda:[FenetreClassement.Btn_Nom(2, dic_Score, ScrollNb, ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, Place1Podium, Place2Podium, Place3Podium, "")])
        ButtonNom4 = Button(Main.Canvas, font = ("Lucida Grande", 12),height = 1, width = 22, cursor = "hand2", command = lambda:[FenetreClassement.Btn_Nom(3, dic_Score, ScrollNb, ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, Place1Podium, Place2Podium, Place3Podium, "")])

        dic_Score = FenetreClassement.RefreshClassement(dic_Score, ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, Place1Podium, Place2Podium, Place3Podium, ScrollNb)

        Btn_Retour = Button(Main.Canvas, text="Retour",font = ("Lucida Grande", 10), width = 10, height = 1, borderwidth=2, cursor = "hand2", command = lambda:[FenetreFin.run(vies, lastJoueur, JoueurChoisi, mot_pendu)])
        Btn_Retour.place(x = 15, y = 560)

        Main.Canvas.tag_bind('ChangeCursor', '<Enter>', lambda e: Main.Canvas.configure(cursor = "hand2"))
        Main.Canvas.tag_bind('ChangeCursor', '<Leave>', lambda e: Main.Canvas.configure(cursor=''))

        Main.Canvas.tag_bind(UpArrowImage, "<1>", lambda e: FenetreClassement.UpArrow(dic_Score, ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, Place1Podium, Place2Podium, Place3Podium, ScrollNb))
        Main.Canvas.tag_bind(DownArrowImage, "<1>", lambda e: FenetreClassement.DownArrow(dic_Score, ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, Place1Podium, Place2Podium, Place3Podium, ScrollNb))

    def SupJoueur(ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, dic_Score, ScrollNb, Place1Podium, Place2Podium, Place3Podium, Btn_ResetScore):
        '''Prend comme arguments : ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, dic_Score, ScrollNb, Place1Podium, Place2Podium, Place3Podium, Btn_ResetScore
        -permet de supprimer un joueur'''

        list_classement = sorted(dic_Score.items(), key=lambda t: t[1]) #liste les scores des joueur selon leur score en order croissant
        list_classement.reverse() #Inverse l'ordre des scores des joueurs

        if ButtonNom1["relief"] == SUNKEN and ButtonNom1["text"] != "": #Si le joueur 1 est cliqué
            del dic_Score[list_classement[ScrollNb.get()][0]] #Suppression du joueur 1 dans le dic_Score
            ButtonNom1.config(relief = RAISED, bg = '#f0f0f0')
        if ButtonNom2["relief"] == SUNKEN and ButtonNom2["text"] != "": #Si le joueur 2 est cliqué
            del dic_Score[list_classement[ScrollNb.get()+1][0]] #Suppression du joueur 2 dans le dic_Score
            ButtonNom2.config(relief = RAISED, bg = '#f0f0f0')
        if ButtonNom3["relief"] == SUNKEN and ButtonNom3["text"] != "": #Si le joueur 3 est cliqué
            del dic_Score[list_classement[ScrollNb.get()+2][0]] #Suppression du joueur 3 dans le dic_Score
            ButtonNom3.config(relief = RAISED, bg = '#f0f0f0')
        if ButtonNom4["relief"] == SUNKEN and ButtonNom4["text"] != "": #Si le joueur 4 est cliqué
            del dic_Score[list_classement[ScrollNb.get()+3][0]] #Suppression du joueur 4 dans le dic_Score
        Btn_ResetScore.destroy()

        #Reset des relief et du background des Buttons des joueurs

        ButtonNom1.config(relief = RAISED, bg = "#f0f0f0")
        ButtonNom2.config(relief = RAISED, bg = "#f0f0f0")
        ButtonNom3.config(relief = RAISED, bg = "#f0f0f0")
        ButtonNom4.config(relief = RAISED, bg = "#f0f0f0")

        FenetreClassement.RefreshClassement(dic_Score, ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, Place1Podium, Place2Podium, Place3Podium, ScrollNb)

    def AfficherButton(ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, dic_Score, ScrollNb, Place1Podium, Place2Podium, Place3Podium, Btn_ResetScore):
        '''Prend comme arguments : ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, dic_Score, ScrollNb, Place1Podium, Place2Podium, Place3Podium, Btn_ResetScore
        -afficher le boutton pour supprimer un joueur'''

        Btn_ResetScore = Button(Main.Canvas, text = "Supprimer le joueur", font = ("Lucida Grande", 12),height = 1, width = 20,cursor = "hand2", command = lambda:[FenetreClassement.SupJoueur(ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, dic_Score, ScrollNb, Place1Podium, Place2Podium, Place3Podium, Btn_ResetScore)])
        Btn_ResetScore.place(x = 100, y = 500)

    def Btn_Nom(Nblist, dic_Score, ScrollNb, ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, Place1Podium, Place2Podium, Place3Podium, Btn_ResetScore):
        '''Prend comme arguments : Nblist, dic_Score, ScrollNb, ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, Place1Podium, Place2Podium, Place3Podium, Btn_ResetScore
        -change le background des bouttons'''

        listButton = [(SUNKEN, "#DCDBDB"), (RAISED, "#f0f0f0"), (RAISED, "#f0f0f0"), (RAISED, "#f0f0f0")]
        listButton[0], listButton[Nblist] = listButton[Nblist], listButton[0]
        ButtonNom1.config(relief = listButton[0][0], bg = listButton[0][1])
        ButtonNom2.config(relief = listButton[1][0], bg = listButton[1][1])
        ButtonNom3.config(relief = listButton[2][0], bg = listButton[2][1])
        ButtonNom4.config(relief = listButton[3][0], bg = listButton[3][1])
        FenetreClassement.AfficherButton(ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, dic_Score, ScrollNb, Place1Podium, Place2Podium, Place3Podium, Btn_ResetScore)

    def UpArrow(dic_Score, ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, Place1Podium, Place2Podium, Place3Podium, ScrollNb):
        '''Prend comme arguments : dic_Score, ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, Place1Podium, Place2Podium, Place3Podium, ScrollNb
        -défilement des scores vers le haut'''

        if ScrollNb.get() != 0 :
            ScrollNb.set(ScrollNb.get() - 1)
            FenetreClassement.RefreshClassement(dic_Score, ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, Place1Podium, Place2Podium, Place3Podium, ScrollNb)

    def DownArrow(dic_Score, ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, Place1Podium, Place2Podium, Place3Podium, ScrollNb):
        '''Prend comme arguments : dic_Score, ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, Place1Podium, Place2Podium, Place3Podium, ScrollNb
        -défilement des scores vers le bas'''

        list_classement = sorted(dic_Score.items(), key=lambda t: t[1]) #liste les scores des joueur selon leur score en order croissant
        if ScrollNb.get() <= len(list_classement)-5 :
            ScrollNb.set(ScrollNb.get() + 1)
            FenetreClassement.RefreshClassement(dic_Score, ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, Place1Podium, Place2Podium, Place3Podium, ScrollNb)

    def RefreshClassement(dic_Score, ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, Place1Podium, Place2Podium, Place3Podium, ScrollNb):
        '''Prend comme arguments : dic_Score, ButtonNom1, ButtonNom2, ButtonNom3, ButtonNom4, Place1Podium, Place2Podium, Place3Podium, ScrollNb
        -met à jour le classement'''

        #Enregistre les Scores
        file=open("Pendu_TXT\Score.txt",'wb')
        dump(dic_Score,file)
        file.close()

        #Met à jour le classement

        if len(dic_Score) != 0:
            list_classement = sorted(dic_Score.items(), key=lambda t: t[1])
            list_classement.reverse()

            if len(list_classement) >= 1 + ScrollNb.get():
                ButtonNom1.config(text = list_classement[ScrollNb.get()][0] + " : " + str(list_classement[ScrollNb.get()][1]) + " points")
                Main.Canvas.itemconfig(Place1Podium, text = list_classement[0][0] + " : " + str(list_classement[0][1]) + " points")
                Main.Canvas.itemconfig(Place2Podium, text = "")
                Main.Canvas.itemconfig(Place3Podium, text = "")
                ButtonNom1.place(x = 97, y = 215)
                ButtonNom2.config(text = "")
                ButtonNom3.config(text = "")
                ButtonNom4.config(text = "")
                ButtonNom2.place_forget()
                ButtonNom3.place_forget()
                ButtonNom4.place_forget()
            if len(list_classement) >= 2 + ScrollNb.get():
                ButtonNom2.config(text=list_classement[ScrollNb.get()+1][0] + " : " + str(list_classement[ScrollNb.get()+1][1]) + " points")
                Main.Canvas.itemconfig(Place2Podium, text = list_classement[1][0] + " : " + str(list_classement[1][1]) + " points")
                Main.Canvas.itemconfig(Place3Podium, text = "")
                ButtonNom2.place(x = 97, y = 255)
                ButtonNom3.config(text = "")
                ButtonNom4.config(text = "")
                ButtonNom3.place_forget()
                ButtonNom4.place_forget()
            if len(list_classement) >= 3 + ScrollNb.get():
                ButtonNom3.config(text=list_classement[ScrollNb.get()+2][0] + " : " + str(list_classement[ScrollNb.get()+2][1]) + " points")
                Main.Canvas.itemconfig(Place3Podium, text = list_classement[2][0] + " : " + str(list_classement[2][1]) + " points")
                ButtonNom3.place(x = 97, y = 303)
                ButtonNom4.config(text = "")
                ButtonNom4.place_forget()
            if len(list_classement) >= 4 + ScrollNb.get():
                ButtonNom4.config(text=list_classement[ScrollNb.get()+3][0] + " : " + str(list_classement[ScrollNb.get()+3][1]) + " points")
                ButtonNom4.place(x = 97, y = 343)
        else :
            ButtonNom1.place_forget()
            Main.Canvas.itemconfig(Place1Podium, text = "")
        return dic_Score

#Création de la fenêtre

Main = Fenetre()
Main.run("/western.jpg", "Jeu du Pendu", ("Lucida Grande", 30))

#Variables

list_Noms = []
modeMise = IntVar()
MotAleatoire = BooleanVar()
Joueur, Joueur1, Joueur2, Joueur3, Joueur4 = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
Joueur1.set("")
Joueur2.set("")
Joueur3.set("")
Joueur4.set("")


FenetreStart.run()
Main.root.mainloop()