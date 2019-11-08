import datetime
from openpyxl import load_workbook
from os import path


def GetDate():
    """
    récupère la date d'aujourdi'hui
    """
    Date = ''
    Temps = ''

    Temps = datetime.datetime.now().time()
    Date = datetime.datetime.now().date()
    return Date, Temps


def sauvDonnee(Chemin, Info, NomFeuille):
    if path.isfile(Chemin):
        date, temps = GetDate()
        #breakpoint()
        try:
            Classeur = load_workbook(Chemin)

            Feuille = Classeur[NomFeuille]

            Feuille.append(Info)

        except PermissionError:

            print("Fichier ouvert")

    else:
        print('Fichier n\'existe plus')

    Classeur.save(Chemin)


def testLigne(listeLigne, valDefaut):
    res = ""
    ligne = ""

    for ligne in listeLigne:
        if ligne != valDefaut:
            res = ligne
        else:
            pass
    return res


def testSfc(SfcaTeste):
    Res = 0
    Err = ""
    #breakpoint()
    try:
        Sfc = int(SfcaTeste)
        Res = Sfc
        Err = "Ras"
    except ValueError:
        Err = "n contient pas que des nombres"

    return Res, Err
