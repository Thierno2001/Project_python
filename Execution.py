import Programe_principal
import art
import colorama

if __name__ == "__main__":

    print("bienvenu dans l'application")
    print("Choissisez 1 : pour s'authentifier")
    print("Choisissez 2 : pour s'enregistrer")
    choix = input("1 ou 2  ")
    if choix == "1" :
            email = Programe_principal.Entree_mail()
            p_hashed = Programe_principal.Entree_pwd()
            with open("Enregistrement.txt", "r") as file:
                 Enregistrement = file.read()
            if f"Email: {email}\n" in Enregistrement and f"Pwd: {p_hashed}\n" in Enregistrement:
                 Programe_principal.Menu()
            else:
                 print("veillez vous enregistrer")
                 Programe_principal.enregistrement_utilisateur()
    else:
            choix == "2"
            Programe_principal.enregistrement_utilisateur()
