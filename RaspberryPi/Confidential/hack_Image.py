import os
import subprocess
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox

# Répertoire contenant les images
image_directory = "./DontLook/"  # Change selon ton chemin réel
image_defaut = 1  # Numéro de l'image à afficher au démarrage (ex: 1.jpg)
output_file = "file.txt"  # Nom du fichier à extraire

# Vérifier si le répertoire existe
if not os.path.exists(image_directory):
    messagebox.showerror("Erreur", f"Le répertoire {image_directory} n'existe pas.")
    exit()

# Fonction pour extraire file.txt avec steghide
def extraire_steghide(image_num, password="iloveyou"):
    image_path = os.path.join(image_directory, f"{image_num}.jpg")

    if os.path.exists(image_path):
        try:
            # Supprimer l'ancien fichier s'il existe
            if os.path.exists(output_file):
                os.remove(output_file)

            # Exécuter steghide extract pour récupérer file.txt
            result = subprocess.run(
                ["steghide", "extract", "-sf", image_path, "-p", password, "-xf", output_file],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )

            # Vérifier si le fichier a bien été extrait
            if os.path.exists(output_file):
                messagebox.showinfo("Extraction réussie", f"Le fichier {output_file} a été extrait avec succès.")
            else:
                messagebox.showerror("Erreur", f"Échec de l'extraction: {result.stderr}")

        except FileNotFoundError:
            messagebox.showerror("Erreur", "Steghide n'est pas installé ou introuvable.")
    else:
        messagebox.showerror("Erreur", f"L'image {image_num}.jpg n'existe pas dans {image_directory}")

# Charger une seule image (l'image par défaut)
def charger_image(image_num):
    image_path = os.path.join(image_directory, f"{image_num}.jpg")
    if os.path.exists(image_path):
        img = Image.open(image_path)
        img = img.resize((1200, 800))  # Redimensionnement unique
        return ImageTk.PhotoImage(img)
    else:
        messagebox.showerror("Erreur", f"L'image {image_num}.jpg n'existe pas dans {image_directory}")
        exit()

# Initialiser Tkinter
window = tk.Tk()
window.title(f"Image {image_defaut}")

# Charger et afficher l'image par défaut
image = charger_image(image_defaut)
label = tk.Label(window, image=image)
label.pack()

# Exécuter steghide pour extraire file.txt
extraire_steghide(image_defaut)

# Lancer l'application
window.mainloop()
