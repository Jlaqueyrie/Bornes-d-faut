from tkinter import Tk
from tkinter import Label
from tkinter import OptionMenu
from tkinter import Button
from tkinter import Radiobutton
from tkinter import StringVar
from tkinter import LabelFrame
from tkinter import Entry
from Fonction import sauvDonnee, testLigne, testSfc
from tkinter import messagebox
from tkinter import N, E, W, S
from tkinter import ACTIVE, DISABLED


class MyFirstGUI():

    def __init__(self, master):
        self.master = master
        "----------------------------Constant---------------------------------"
        Classeur = r'C:\Users\jlaqueyr\Documents\MyNoteBook\ScriptPython\BorneDefaut\Feuille.xlsx'
        FeuilleDefaut = r'Liste des saisies'

        LBL_Z_INFO = 'Information générale'
        LARGEUR_FRAME = 485
        TITRE = 'Borne défaut'
        DIMENSION_FENETRE = '500x350+30+30'
        LBL_SFC = 'SFC'
        LBL_OPERATEUR = 'Nom'
        LBL_Z_LIGNE = 'Sur quel ligne est apparu le défaut ?'
        LBL_Z_DEF = 'Description du défaut'
        LBL_Z_DEF_INT = 'Intégration'
        LBL_Z_DEF_UFT = 'UFT et CADS'
        LBL_Z_DEF_ETI = 'Etiquettes'
        LBL_Z_DEF_CHOIX = "Choisir le défaut"

        NOM_LIGNE1 = 'Ligne Principale'
        NOM_LIGNE2 = 'Ligne Secondaire'
        PADX_INFO = 5
        PADX_LBL_INFO = 5
        PADY_INFO = 20
        PADX_BTN_LIGNE = 40
        PADY_BTN_LIGNE = 15
        PADX_ZN_DEF = 5
        PADY_ZN_DEF = 10
        MSG_SAUV_TITRE = "Ticket sauvegardé"
        MSG_SAUV_CONTENU = "Ticket défaut sauvegardé"
        VAL_DEF_CHOIX = 'Choix X'

        nomOperateur = StringVar(master)
        sfc = StringVar(master)
        master.title(TITRE)
        master.geometry(DIMENSION_FENETRE)
        "---------------------------Fonction----------------------------------"
        def callback(*args):
            print("tkvar changed")
            popupMenu2.configure(state='disable')
            popupMenu3.configure(state='disable')

        def callback2(*args):
            print("tkvar changed 1")
            popupMenu1.configure(state='disable')
            popupMenu3.configure(state='disable')

        def callback3(*args):
            print("tkvar changed 2")
            popupMenu1.configure(state='disable')
            popupMenu2.configure(state='disable')

        def testDefaut(listeDefaut, valDefaut):
            breakpoint()
            defaut = ""

            for defaut in listeDefaut:

                if defaut != valDefaut:
                    defFinal = defaut
                    break
                else:
                    pass

            return defFinal

        def RecupValeur():
            ListeInfo = []

            print(
                self.txtSfc.get(),
                self.txtNomOperateur.get(),
                Ligne1Var.get(),
                Ligne2Var.get(),
                self.tkvar.get())

            listeLigne = [Ligne1Var.get(), Ligne2Var.get()]
            resultatLigne = testLigne(listeLigne, 'off')

            resultatSfc, ErrSfc = testSfc(sfc.get())
            breakpoint()
            self.listeDef = [self.tkvar.get(),
                             self.tkvar1.get(),
                             self.tkvar2.get()]

            resultatDefaut = testDefaut(self.listeDef, VAL_DEF_CHOIX)

            ListeInfo = [
                resultatSfc,
                self.txtNomOperateur.get(),
                resultatLigne,
                resultatDefaut]

            sauvDonnee(Classeur, ListeInfo, FeuilleDefaut)

            self.txtSfc.delete(0, 'end')
            self.txtNomOperateur.delete(0, 'end')
            self.btnLigne1.deselect()
            self.btnLigne2.deselect()

            popupMenu1.configure(state='active')
            popupMenu1.selection_clear()

            popupMenu2.configure(state='active')
            popupMenu2.selection_clear()

            popupMenu3.configure(state='active')
            popupMenu3.selection_clear()

            messagebox.showinfo(MSG_SAUV_TITRE, MSG_SAUV_CONTENU)

        "------------------Information sur le produit-------------------------"
        self.ZoneInfoGen = LabelFrame(
            master,
            text=LBL_Z_INFO,
            width=LARGEUR_FRAME,
            height=80)
        self.ZoneInfoGen.grid(row=0, column=1, sticky=N + S + W + E)
        self.ZoneInfoGen.grid_propagate(0)

        self.lblSfc = Label(self.ZoneInfoGen, text=LBL_SFC)
        self.txtSfc = Entry(self.ZoneInfoGen, textvariable=sfc)
        self.txtSfc.focus_set()
        self.lblNomOperateur = Label(self.ZoneInfoGen, text=LBL_OPERATEUR)
        self.txtNomOperateur = Entry(
            self.ZoneInfoGen, textvariable=nomOperateur)

        self.lblSfc.grid(row=0, column=1, padx=PADX_LBL_INFO, pady=PADY_INFO)
        self.txtSfc.grid(
            row=0,
            column=2,
            ipadx=25,
            padx=PADX_INFO,
            pady=PADY_INFO)
        self.lblNomOperateur.grid(
            row=0, column=3, padx=PADX_LBL_INFO, pady=PADY_INFO)
        self.txtNomOperateur.grid(
            row=0, column=4, ipadx=25, padx=PADX_INFO, pady=PADY_INFO)

        "----------Information sur la ligne qui a produit le défaut-----------"
        self.ZoneLigne = LabelFrame(
            master,
            text=LBL_Z_LIGNE,
            width=LARGEUR_FRAME,
            height=80)
        self.ZoneLigne.grid(row=1, column=1)
        self.ZoneLigne.grid_propagate(0)

        Ligne1Var = StringVar(value="off")
        self.btnLigne1 = Radiobutton(
            self.ZoneLigne,
            text=NOM_LIGNE1,
            variable=Ligne1Var,
            indicatoron=False,
            value="Ligne1")

        Ligne2Var = StringVar(value="off")
        self.btnLigne2 = Radiobutton(
            self.ZoneLigne,
            text=NOM_LIGNE2,
            variable=Ligne2Var,
            indicatoron=False,
            value="Ligne2")

        self.btnLigne1.grid(
            row=0,
            column=1,
            ipadx=30,
            padx=PADX_BTN_LIGNE,
            pady=PADY_BTN_LIGNE)
        self.btnLigne2.grid(
            row=0,
            column=3,
            ipadx=30,
            padx=PADX_BTN_LIGNE,
            pady=PADY_BTN_LIGNE)

        if self.btnLigne2.state():
            print(self.btnLigne2.state)

        if not self.btnLigne1.select():
            print(self.btnLigne1.get())
        "------------------Information sur le type de défaut-------------------"
        self.ZoneDefaut = LabelFrame(
            master,
            text=LBL_Z_DEF,
            width=LARGEUR_FRAME,
            height=130)
        self.ZoneDefaut.grid(row=2, column=1, sticky='NW')
        self.ZoneDefaut.grid_propagate(0)

        self.ZoneDefautInt = LabelFrame(
            self.ZoneDefaut,
            text=LBL_Z_DEF_INT,
            height=80,
            width=150)
        self.ZoneDefautInt.grid(
            row='0',
            column='1',
            padx=PADX_ZN_DEF,
            pady=PADY_ZN_DEF)
        self.ZoneDefautInt.grid_propagate(0)

        self.tkvar = StringVar(master)
        choices = {'Choix 1', 'Choix 2', 'Choix 3', 'Choix 4', 'Choix 5'}
        self.tkvar.set(VAL_DEF_CHOIX)
        popupMenu1 = OptionMenu(self.ZoneDefautInt, self.tkvar, *choices)
        Label(
            self.ZoneDefautInt,
            text=LBL_Z_DEF_CHOIX).grid(
            row=1,
            column=1)
        popupMenu1.grid(row=2, column=1, ipadx=30)

        self.ZoneDefautUFT = LabelFrame(
            self.ZoneDefaut,
            text=LBL_Z_DEF_UFT,
            height=80,
            width=150)

        self.ZoneDefautUFT.grid(
            row='0',
            column='2',
            padx=PADX_ZN_DEF,
            pady=PADY_ZN_DEF)
        self.ZoneDefautUFT.grid_propagate(0)
        self.tkvar1 = StringVar(master)
        choices = {'Choix 1', 'Choix 2', 'Choix 3', 'Choix 4', 'Choix 5'}
        self.tkvar1.set(VAL_DEF_CHOIX)
        popupMenu2 = OptionMenu(self.ZoneDefautUFT, self.tkvar1, *choices)
        Label(
            self.ZoneDefautUFT,
            text=LBL_Z_DEF_CHOIX).grid(
            row=1,
            column=1)
        popupMenu2.grid(row=2, column=1, ipadx=30)

        self.ZoneDefautEti = LabelFrame(
            self.ZoneDefaut,
            text=LBL_Z_DEF_ETI,
            height=80,
            width=150)
        self.ZoneDefautEti.grid(
            row='0',
            column='3',
            padx=PADX_ZN_DEF,
            pady=PADY_ZN_DEF)
        self.ZoneDefautEti.grid_propagate(0)

        self.tkvar2 = StringVar(master)
        choices = {'Choix 1', 'Choix 2', 'Choix 3', 'Choix 4', 'Choix 5'}
        self.tkvar2.set(VAL_DEF_CHOIX)
        popupMenu3 = OptionMenu(self.ZoneDefautEti, self.tkvar2, *choices)
        Label(
            self.ZoneDefautEti,
            text=LBL_Z_DEF_CHOIX).grid(
            row=1,
            column=1)
        popupMenu3.grid(row=2, column=1, ipadx=30)

        self.btnValider = Button(
            master,
            text="Valider",
            relief="raised",
            command=RecupValeur)

        self.btnValider.grid(row=3, column=1)

        self.tkvar.trace("w", callback)
        self.tkvar1.trace('w', callback2)
        self.tkvar2.trace('w', callback3)


def main():
    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
