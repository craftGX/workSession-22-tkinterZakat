from tkinter import *
from tkinter import messagebox


# definition de la fonction calcul
def calculZakat():
    try:
        epargne = int(entree_somme.get())
        zakat = (epargne * 2.579) / 100
        if epargne > 1500:
            resultat_somme.delete(0, END)
            resultat_somme.insert(0, zakat)
        else:
            messagebox.showinfo(title="ATTENTION!", message="Vous ne payerez pas de Zakat cette année!")
    except:
        messagebox.showerror(title="ERREUR!", message="Vous avez mal rempli le formulaire")


# creation de la fenetre
fenetre = Tk()
fenetre.geometry("500x300")
fenetre.title("Calcul Zakat")
fenetre.resizable(0, 0)
fenetre.config(bg="#B4FB4D")
# titre de la fenetre
presentation = Label(fenetre, text="Bienvenue sur mon application de calcul zakat al maal", bg="#96FC02")
presentation.pack(fill=X)
# entree de la somme epargnée
somme_epargne = Label(fenetre, text="Veuillez entrer la somme épargné svp :", bg="#96FC02")
somme_epargne.place(x=25, y=50)
entree_somme = Entry(fenetre)
entree_somme.place(x=25, y=80)
# creation du bouton valider
valider = Button(fenetre, text="ZAKAT", bg="green", command=calculZakat)
valider.place(x=25, y=110)
# resultat du calcul
resultat_calcul = Label(fenetre, text="vous devez payer : ", bg="#96FC02")
resultat_calcul.place(x=25, y=150)
resultat_somme = Entry(fenetre)
resultat_somme.place(x=25, y=180)
# loop
fenetre.mainloop()
