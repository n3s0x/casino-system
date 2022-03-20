from random import randint


def bienvenue():
    global bank_account

    bank_account = 1000

    print('-----[JEU DE LA ROULETTE]-----')
    print('-----Bienvenue !-----')
    print('-----Créé par Tristan-----')
    print('--------------------------')
    # global bank_account
    # bank_account=1000
    print("Vous avez", bank_account, 'jetons')


def mise():
    global Q1
    global Q2
    global choix_Q1
    global choix_Q2
    global mise_Q1
    global mise_Q2
    global bank_account

    Q1 = str(input("Voulez vous choisir un numéro ? 'oui'/'non'"))
    if Q1 == 'oui':
        choix_Q1 = int(input("Choissisez un numéro entre 1 et 37 "))
        if choix_Q1 >= 1 and choix_Q1 <= 37:
            mise_Q1 = int(input("Montant de la mise ? "))
            if mise_Q1 <= bank_account:
                bank_account = bank_account - mise_Q1
                print('-------')
                print("Le numéro du joueur est", choix_Q1, "il a misé", mise_Q1, "jetons")
                print('-------')
            else:
                print("Vous n'avez pas assez de jetons")
                print(bank_account)
                quit()
        else:
            print("Merci de rentrez une valeur entre 1 et 37")
            quit()
    elif Q1 == 'non':
        print('-------')
        print("Vous ne jouez pas de numéro")
        print('-------')

    elif Q1 != 'non' or 'oui':

        print('-----------')
        print("ERREUR : Vous avez rentrée une valeur interdite")
        quit()

    Q2 = str(input("voulez vous choisir une couleur ? 'oui'/'non' "))
    if Q2 == 'oui':
        choix_Q2 = str(input("Choissisez 'red' ou 'black' ?"))
        if choix_Q2 == 'red' or choix_Q2 == 'black':
            mise_Q2 = int(input("Montant de la mise ? "))
            if mise_Q2 <= bank_account:
                bank_account = bank_account - mise_Q2
                print('-------')
                print("La couleur du joueur est", choix_Q2, "il a misé", mise_Q2, "jetons")
                print('-------')
            else:
                print("Vous n'avez pas assez de jetons")
                quit()
        else:
            print("Couleur non acceptée, annulation")
            quit()

    elif Q2 == 'non':
        print('-------')
        print("Vous ne jouez pas de couleur")
        print('-------')

    elif Q1 != 'non' or 'oui':

        print('-----------')
        print("ERREUR : Vous avez rentrée une valeur interdite")
        quit()


def roll():
    global roll
    global color
    red_list = [3, 9, 12, 18, 21, 27, 30, 36, 5, 14, 23, 32, 1, 7, 16, 25, 28, 34]
    roll = randint(1, 37)

    if roll in red_list:
        color = 'red'
    else:
        color = 'black'

    print("La roulette à tournée !")
    print('-------')
    print("Numéro:", roll)
    print('-------')
    print("Couleur:", color)
    print('-------')


def gain():
    global bank_account
    global gainQ1
    global gainQ2
    global mise_Q1
    global mise_Q2

    gainQ1 = 0
    gainQ2 = 0

    if Q1 == 'oui':
        if choix_Q1 == roll:
            gainQ1 = mise_Q1 * 10
    else:
        pass

    if Q2 == 'oui':
        if choix_Q2 == color:
            gainQ2 = mise_Q2 * 1.5
    else:
        pass

    if Q1 == 'oui' and Q2 == 'oui':
        gain_total = gainQ1 + gainQ2
        mise_total = mise_Q1 + mise_Q2
        benefice_total = gain_total - mise_total
        bank_account = bank_account + gain_total
        print("Activité du tour :", benefice_total, 'jetons')
        print("-------------")
        print("Le solde de votre compte est désormais de", bank_account)

    elif Q1 == 'oui' and Q2 == 'non':
        gain_total = gainQ1
        mise_total = mise_Q1
        benefice_total = gain_total - mise_total
        bank_account = bank_account + gain_total
        print("Activité du tour :", benefice_total, 'jetons')
        print("-------------")
        print("Le solde de votre compte est désormais de", bank_account)

    elif Q1 == 'non' and Q2 == 'oui':
        gain_total = gainQ2
        mise_total = mise_Q2
        benefice_total = gain_total - mise_total
        bank_account = bank_account + gain_total
        print("Activité du tour :", benefice_total, 'jetons')
        print("-------------")
        print("Le solde de votre compte est désormais de", bank_account)

    elif Q1 == 'non' and Q2 == 'non':
        print("Vous n'avez fait aucune mise")
        print("-------------")
        print("Le solde de votre compte est de", bank_account)