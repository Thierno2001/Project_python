import maskpass
import string
import hashlib
import bcrypt

def Entree_mail():
    while True:
        email = input("Entrez votre e-mail : ")
        if "@" in email and "." in email and "gmail" in email and "com" in email:
            return email
        else:
            print("SVP, entrez une adresse e-mail valide.")

def Entree_pwd():
    while True:
        p = maskpass.askpass()
        if len(p) == 8:
            if any(c in string.digits for c in p):
                if any(c in string.ascii_uppercase for c in p):
                    if any(c in string.ascii_lowercase for c in p):
                        if any(c in string.punctuation for c in p):
                            p_hashed = hashlib.sha256(p.encode()).hexdigest()
                            return p_hashed
                        else:
                            print("SVP, au moins un caractère spécial")
                    else:
                        print("SVP, au moins un caractère minuscule")
                else:
                    print("SVP, au moins un caractère majuscule")
            else:
                print("SVP, au moins un chiffre")
        else:
            print("SVP, le mot de passe doit avoir 8 caractères")

def Authentification():
    email = Entree_mail()
    p_hashed = Entree_pwd()

    with open("Enregistrement.txt", "r") as file:
        cyber = file.read()
        if f"Email: {email}\n" in cyber and f"Pwd: {p_hashed}\n" in cyber:
            print("Authentification réussie.")
            Menu()
        else:
            print("Les identifiants sont incorrects. Veuillez vous enregistrer.")
            enregistrement_utilisateur()
def enregistrement_utilisateur():
    print("Enregistrement de nouvel utilisateur :")
    email = Entree_mail()
    p_hashed = Entree_pwd()

    with open("Enregistrement.txt", "a") as file:
        file.write(f"Email: {email}\nPwd: {p_hashed}\n")

    print("Utilisateur enregistré avec succès.")
    print("authentifiez vous s'il vous plait")
    Authentification()


def Menu():
    while True:
        print("Menu :")
        print("a : Haché le mot par sha256")
        print("b : Haché le mot en générant un salt (bcrypt)")
        print("c : Attaquer par dictionnaire le mot inséré")
        choix = input(" Choisissez une option (a/b/c) ou 'q' pour quitter : ")
        if choix == 'a':
            mot_a_hasher = maskpass.askpass("Entrez le mot à hacher : ")
            sha256_hash = hashlib.sha256(mot_a_hasher.encode()).hexdigest()
            print(f"Hachage SHA-256 : {sha256_hash}")
        elif choix == 'b':
            mot_a_hasher = maskpass.askpass("Entrez le mot à hacher : ")
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(mot_a_hasher.encode(), salt)
            print(f"Hachage bcrypt : {hashed_password}")
        elif choix == 'c':
            mot_a_attaquer = maskpass.askpass("Entrez le mot à attaquer : ")
            if dictionary_attack(mot_a_attaquer):
                print("Mot de passe trouvé dans le dictionnaire.")
            else:
                print("Le mot de passe n'a pas été trouvé dans le dictionnaire.")
        elif choix == 'q':
            break
        else:
            print("Option invalide. Veuillez réessayer.")

def dictionary_attack(target_password):
    with open("Enregistrement.txt", "r") as file:
        for line in file:
            word = line.strip()
            hashed_word = hashlib.sha256(word.encode()).hexdigest()
            if hashed_word == target_password:
                print(f"Mot de passe trouvé dans le dictionnaire : {word}")
                return True
    return False
