CTF TOPSECRET 
Guide de l'Organisateur

Ce fichier README est destiné aux organisateurs du CTF. Il vous guidera à travers les étapes de mise en place du jeu, la configuration des appareils, et l'organisation des différents éléments pour que le CTF se déroule sans problème.
1. Matériel Nécessaire

    M5Stack Core2 (avec écran tactile)
    Raspberry Pi avec Raspbian installé
    PC pour la connexion SSH au Raspberry Pi
    Câbles de connexion (si nécessaire)
    Image et fichiers pour le CTF (contenus dans les dossiers ci-dessous)

2. Structure du Projet
Raspberry Pi - Structure des Fichiers

Sur le Raspberry Pi, vous trouverez les dossiers et fichiers suivants :

    Confidential
        DontLook/
            1.jpg : L'image contenant un fichier caché.
        hack_Image.py : Le programme Python permettant d'extraire un fichier caché dans l'image via steghide.
        readme.txt : Instructions pour lancer le programme Python.

    PiFmRds
        doc/ : Ce dossier est vide et est utilisé pour brouiller les pistes.
        LICENSE : Fichier inutile.
        README.md : Fichier de documentation pour le PiFmRds.
        src/ : Dossier de code source, non utilisé directement.

    Instructions :
        instructions.txt : Le fichier à lire une fois la connexion SSH établie. Il contient les commandes et les détails pour continuer le jeu.

M5Stack Core2 - Fichiers

    enigme_m5stack.py : Code Python pour le M5Stack Core2. Ce fichier contient les énigmes et la logique pour guider les participants à travers les étapes initiales du CTF.

Autres Fichiers

    AUDIO.wav : Fichier audio utilisé pour la radio à diffuser avec la commande pi_fm_rds sur le Raspberry Pi.

3. Configuration du M5Stack Core2
1. Préparation du M5Stack Core2 :

    Téléchargez et installez l'IDE Arduino si vous ne l'avez pas déjà fait.
    Ouvrez le fichier enigme_m5stack.py dans l'IDE Arduino.
    Sélectionner le bon modèle : Dans l'IDE Arduino, sélectionnez le modèle M5Stack Core2.
        Allez dans Outils > Carte > M5Stack Core2.
    Assurez-vous que les drivers USB sont installés pour pouvoir connecter votre M5Stack Core2 à l'ordinateur via USB.
    Téléversez le code sur le M5Stack Core2.

2. Fonctionnement du M5Stack Core2 :

    Lors de la mise sous tension, l'écran tactile du M5Stack Core2 affichera les énigmes. Les participants devront répondre correctement aux deux questions en appuyant sur les options à l'écran.
    Après avoir répondu correctement, un message de confirmation apparaîtra, avec une commande SSH pour se connecter au Raspberry Pi.
    Les participants devront entrer cette commande sur leur PC pour se connecter au Raspberry Pi via SSH.

4. Étapes de Jeu
1. Phase Initiale - M5Stack Core2 :

    Les participants commenceront par lire l'affiche d'intrigue pour comprendre l'histoire du CTF.
    Sur le M5Stack Core2, les énigmes s'afficheront sur l'écran tactile. Les participants devront appuyer sur les bonnes options pour répondre aux questions.
    Si les réponses sont correctes, un message affichera la commande SSH pour se connecter au Raspberry Pi.

2. Phase de Connexion au Raspberry Pi :

    Une fois la commande SSH affichée sur le M5Stack, les participants se connecteront au Raspberry Pi via SSH en utilisant un PC.
    Une fois connectés, ils trouveront deux dossiers principaux :
        Confidential : Le dossier contenant l'image cachée et les instructions pour extraire un fichier.
        PiFmRds : Le dossier avec un fichier README.md et le code source pour diffuser de l'audio avec pi_fm_rds.

3. Extraction du Fichier Caché :

    Une fois dans le dossier Confidential, les participants ouvriront le dossier DontLook pour trouver l'image 1.jpg.

    Ils devront exécuter le programme Python hack_Image.py (comme décrit dans readme.txt) pour extraire un fichier caché file.txt.
        Note importante : Le fichier file.txt est généré par l'exécution du programme hack_image.py. Ce programme utilise steghide pour extraire le fichier caché de l'image 1.jpg.

4. Recherche de la Radio Cachée :

    Dans le fichier file.txt, les participants trouveront une indication leur disant de chercher la radio cachée avant de pouvoir lancer la diffusion audio. Le texte dans file.txt indiquera explicitement :

    Laissez-vous guider par la voix dans l'appareil, il vous conduira à ce que vous cherchez.
    Une fois l'appareil trouvé, rendez-vous dans le dossier PiFmRds et utilisez cette commande:
    sudo .pi_fm_rds -ps Radio_Secrete -audio AUDIO.wav -freq 100.0M

    Une fois qu'ils auront trouvé la radio cachée (un appareil physique dissimulé dans la salle), ils pourront alors passer à l'étape suivante.

5. Diffusion de l'Audio :

    Une fois la radio trouvée, les participants devront se rendre dans le dossier PiFmRds et utiliser la commande suivante pour lancer la diffusion audio :

    sudo .pi_fm_rds -ps Radio_Secrete -audio AUDIO.wav -freq 100.0M

    Cette commande lancera la diffusion audio. Les participants devront écouter attentivement pour localiser un Raspberry Pi caché dans la salle.

6. Localisation du Raspberry Pi Caché :

    En écoutant la diffusion, les participants devront se rapprocher du Raspberry Pi caché dans la salle. Une fois trouvé, ils découvriront un document avec le texte de fin du CTF.

7. Texte de Fin :

    Le texte de fin, trouvé sous le Raspberry Pi caché, contient un message Top Secret, marquant la fin du CTF.

5. Résumé du Déroulement

    Les participants résolvent deux énigmes sur le M5Stack Core2.
    Ils obtiennent une commande SSH pour se connecter au Raspberry Pi.
    Ils cherchent la radio cachée dans la salle.
    Ils extraient un fichier caché à partir de l'image dans le dossier Confidential grâce à l'exécution de hack_image.py.
    Ils diffusent un fichier audio via la commande pi_fm_rds.
    En écoutant l'audio, ils localisent un Raspberry Pi caché, avec un document final pour marquer la fin du CTF.

6. Conseils pour les Organisateurs

    Vérification préalable : Assurez-vous que tous les appareils (M5Stack Core2, Raspberry Pi, PC) sont configurés et fonctionnent correctement avant le début du CTF.

    Surveillance : Soyez disponible pour répondre aux questions des participants et les aider s'ils se retrouvent bloqués.

    Encouragement : Maintenez une atmosphère de soutien et d'encouragement pour que les participants puissent se concentrer et profiter du jeu.

Important

N'oubliez pas de tester toutes les étapes en amont pour vous assurer que tout fonctionne correctement, y compris le programme sur le M5Stack et la configuration SSH pour le Raspberry Pi.
