from m5stack import *
from m5ui import *
from uiflow import *
lcd.clear()  # Efface l'écran au démarrage

# Variables pour suivre les niveaux et les réponses
niveau = 1
reponse_donnee = False
bad_reponse = False
geo='k4V;hl*24Ype`)Xg~F_.oCm`1mR#3VmR#3^l.f*XmSP0Yo!&-=o#<e-l.6#oo!%4"i|tYzi^1FViz_3li]]+\h>&%Si]]qXe*p!u'

def question1():
    lcd.clear()
    lcd.setTextColor(0x338aff)
    lcd.font(lcd.FONT_DejaVu18)
    lcd.print("Un message a ete code en        decalant chaque lettre de 1            Trouve le message :", 30, 20)
    lcd.print("IFMMP", 140, 90)
    lcd.setTextColor(0xffffff)
    lcd.print("IFMMP", 137, 90)
    lcd.setTextColor(0x338aff)
    lcd.print("Bouton 1: JGOOQ", 87, 120)
    lcd.print("Bouton 2: WORLD", 85, 150)
    lcd.print("Bouton 3: HELLO", 87, 180)
    lcd.setTextColor(0xffffff)
    lcd.print("(1)", 40, 220)
    lcd.print("(2)", 147, 220)
    lcd.print("(3)", 252, 220)

def question2():
    lcd.clear()
    lcd.setTextColor(0x338aff)
    lcd.font(lcd.FONT_DejaVu18)
    lcd.print(" Trouve le mot cache dans                  cette phrase :", 30, 20)
    lcd.print("Les Fichiers LAnces Generent                des erreurs ", 20, 60)
    lcd.print("Bouton 1: Fichiers", 87, 120)
    lcd.print("Bouton 2: FLAG", 87, 150)
    lcd.print("Bouton 3: LAnces", 87, 180)
    lcd.setTextColor(0xffffff)
    lcd.print("(1)", 40, 220)
    lcd.print("(2)", 147, 220)
    lcd.print("(3)", 252, 220)

# Vérification des réponses pour question 1
def reponse1():
    global reponse_donnee, bad_reponse
    if reponse_donnee:
        return
    if btnC.isPressed():  # Bonne réponse
        lcd.clear()
        lcd.setTextColor(0x338aff)
        lcd.print("Bravo !", 130, 110)
        lcd.setTextColor(0xffffff)
        lcd.print("Bravo !", 128, 110)
        wait(2)
        lcd.setTextColor(0xffffff)
        lcd.print("Suivant", 235, 220)
        reponse_donnee = True
    elif btnA.isPressed() or btnB.isPressed():
        lcd.clear()
        lcd.setTextColor(0xFF0000)
        lcd.print("Reponse incorrecte", 80, 110)
        wait(2)
        lcd.setTextColor(0x0000FF)
        lcd.print("Reessayer(maintenir)", 0, 220)
        bad_reponse = True

# Vérification des réponses pour question 2
def reponse2():
    global reponse_donnee, bad_reponse
    if reponse_donnee:
        return
    if btnB.isPressed():  # Bonne réponse
        lcd.clear()
        lcd.setTextColor(0x338aff)
        lcd.print("Bravo !", 130, 110)
        lcd.setTextColor(0xffffff)
        lcd.print("Bravo !", 128, 110)
        wait(2)
        lcd.clear()
        wait(1)
        lcd.setTextColor(0x338aff)
        lcd.print("Vous avez reussi les epreuves", 15, 30)
        lcd.setTextColor(0x338aff)
        lcd.print("A present nous sommes sur que vous avez le niveau requis pour mener a bien votre mission", 0, 80)
        wait(2)
        lcd.setTextColor(0xffffff)
        lcd.print("Suivant", 235, 220)
        wait(3)
        reponse_donnee = True
    elif btnA.isPressed() or btnC.isPressed():
        lcd.clear()
        lcd.setTextColor(0xFF0000)
        lcd.print("Reponse incorrecte", 80, 110)
        wait(2)
        lcd.setTextColor(0x0000FF)
        lcd.print("Reessayer(maintenir)", 0, 220)
        bad_reponse = True

# Réafficher la question si mauvaise réponse
def reessayer():
    global bad_reponse
    if bad_reponse and btnA.isPressed():
        bad_reponse = False
        lcd.clear()
        wait(1)
        if niveau == 1:
            question1()
        elif niveau == 2:
            question2()

# Passer au niveau suivant
def suivant():
    global niveau, reponse_donnee, bad_reponse
    if reponse_donnee and btnC.isPressed():
        reponse_donnee = False
        bad_reponse = False
        niveau += 1
        lcd.clear()

# Fonction pour afficher la fin
def fin():
    lcd.clear()
    lcd.setTextColor(0x338aff)
    lcd.print("Vous pouvez vous connecter au pc du gouvernement en utilisant cette comande :", 0, 50)
    lcd.print("ssh -X etudiant@10.122.0.183", 10, 130)
    lcd.setTextColor(0xffffff)
    lcd.print("ssh -X etudiant@10.122.0.183", 8, 130)
    lcd.setTextColor(0x338aff)
    lcd.print("Et en entrant ce mot de passe :", 10, 180)
    lcd.print("confidentiel", 100, 200)
    lcd.setTextColor(0xffffff)
    lcd.print("confidentiel", 98, 200)

# Afficher la première question
question1()

# Boucle principale
while True:
    if niveau == 1:
        reponse1()
        reessayer()
        if reponse_donnee:
            suivant()
            if niveau == 2:
                question2()
    elif niveau == 2:
        reponse2()
        reessayer()
        if reponse_donnee:
            suivant()
            if niveau == 3:
                fin()
                break
    wait(0.1)