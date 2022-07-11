# -*-coding:Utf-8 -*
"""

Created on Sun Jun 26 05:52:10 2022

Module navigation et stockage

"""

import os  # module système pour navigation dans arborescence dossiers

# Pour mettre en forme le nom des fichiers image avec un nb limité de mots
from math import ceil



# **********   Navigation entre fichiers de sauvegarde des données   *********** #

def navigation_dossier(type):
    """
    
    Fonction permettant la navigation vers un dossier fichier_type.
    
    En paramètre, une chaine de caractère.
    Si le dossier n'existe pas, il est créé.
    
    Args:
        string: désigne le type de fichiers rangés dans ce dossier. 'csv' 
        pour un fichier d'extension csv ou img pour une image d'extension img.
    Raises:
        FileNotFoundError: dans le cas où le dossier n'existe pas encore.
        Il est alors créé.
    """
    # Bloc try/excepttry navigation essai atteindre dossier de sauvegarde
    try:
        os.chdir("fichiers_" + type)
    # si échec alors création du dossier puis navigation vers ce dossier
    except FileNotFoundError:
        os.mkdir("fichiers_" + type)
        os.chdir("fichiers_" + type)


def dossiers_images(cat):
    """
    Fonction permettant la navigation vers un dossier image
    associé à la catégorie de livre.
    Le paramètre de la fonction indique la catégorie de livres.
    Si le dossier n'existe pas encore il est créé.
    Args:
        string: la catégorie de livre
    Raises:
        FileNotFoundError: dans le cas où le dossier n'existe pas encore.
        Il est alors créé.
    """
    try:
        os.chdir(cat)
    # si échec créer dossier puis navigation
    except FileNotFoundError:
        os.mkdir(cat)
        os.chdir(cat)


def titre_fichier_image(titre):
    """
    Cette fonction met en forme le titre du livre récupéré parmi les données
    sur la page du livre.
    Le résultat doit servir de nom de fichier au fichier image téléchargé
    
    Args:
        string : titre récupéré sur la page de description du livre
    
    Return:
        string: titre raccourci(maxi 5 mots), sans carcatères non autorisés
    """
    # Liste de caractères indésirables dans le nom de fichier de l'image
    filtre_caracteres = [',', ';', '’', '/', '\\',
                         ':', '*', '?', '"', '<', '>', '|']
    for caractere in filtre_caracteres:
        titre = titre.replace(caractere, '')  # Nettoie le titre
    title_liste = titre.split()
    # Détermine le nombre de mots du nom de l'image
    if len(title_liste) > 10:
        nb_mots_title_img = 5
    elif len(title_liste) > 6:
        nb_mots_title_img = ceil(len(title_liste)/2)
    else:
        nb_mots_title_img = len(title_liste)
    # Reconstruit un titre avec maximum les 5 premiers mots et des underscore
    title_img = "_".join(title_liste[:nb_mots_title_img])
    return(title_img)


def entete_csv_cat(fichier_csv_cat):
    """
    Cette fonction permet l'écriture de l'entête du fichier csv pour une
    catégorie de livre.
    """
    navigation_dossier('csv')  # Navigation vers le dossier fichiers_csv
    with open(fichier_csv_cat, "w", encoding="utf-8") as fichier_book:
        fichier_book.write("product_page_url, " +
                           "universal_ product_code (upc), " +
                           "title, " +
                           "price_including_tax, " +
                           "price_excluding_tax, " +
                           "number_available, " +
                           "product_description, " +
                           "category, " +
                           "review_rating, image_url\n")
    os.chdir(os.pardir)