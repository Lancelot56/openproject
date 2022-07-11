# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 05:48:13 2022

Module catégories

"""


import os  # module système pour navigation dans arborescence dossiers
import bs4  # import tout bs4 pour test type objet
import time  # Pour ajout d'un délai dans exécution requete avec timesleep

from settings.constantes import URL_INDEX # URL de travail en constantes

from fonctions.requete import validation_url
from fonctions.navigation_stockage import navigation_dossier
from fonctions.one_book import data_one_book


#       Gestion des catégories de livres   #


def entete_csv_cat(fichier_csv_cat):
    """
    
    Fonction permettant d'écrire l'entête du fichier csv pour une
    catégorie de livre donnée.
    
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


def list_book_cat(soup, liste):
    
    """
    Fonction stockant dans un objet de type liste les url des livres
    d'une catégorie donnée.
    """
    # Recherche des url de chaque livre
    book_links = soup.find_all("div", {'class': 'image_container'})
    # on rajoute l'url de chaque livre à la liste des url de cette catégorie
    for div in book_links:
        a = div.find('a')
        liste.append('http://books.toscrape.com/catalogue/' + a['href'].replace("../", ''))
    return(liste)


def nombre_page_categorie(soup):
    
    """
    Fonction calculant le nombre de pages pour une catégorie donnée.
 
    """
   
    # Recherche s'il y a plusieurs pages
    nb_page = soup.find("li", {"class": "current"})
    # Si il y a plusieurs pages, nb_page est du type bs4.element.Tag
    if isinstance(nb_page, bs4.element.Tag):
        # On récupère le nombre de pages:
        nb_page = int(nb_page.get_text().strip()[-1])
    else:
        nb_page = 1
    return(nb_page)


def extractions(url_site):
    
    """
    Fonction procédant à l'extraction de l'ensemble des livres par catégorie,
    répartis éventuellement sur plusieurs pages.
    
    Pour chaque livre, La fonction lance ensuite l'extraction 
    des données demandées.
          
    """
   
    # Gestion des exceptions sur la requête
    
    valid_url, response = validation_url(url_site)
    
    if valid_url:
       
        # Parser lxml BeautiFul Soup pour analyse du html
        
        soup_index = bs4.BeautifulSoup(response.text, "lxml")
        
        # Sélection
        
        liste_li = soup_index.find('ul', {'class': "nav nav-list"}).find('ul').find_all('li')
        
        # On boucle sur toutes les catégories
        
        for li in liste_li:
            a = li.find('a')
            cat = a.get_text().strip()
            url_cat = URL_INDEX + a['href']
            
            # Création du fichier csv pour une catégorie
            
            entete_csv_cat(cat + '.csv')  # Ecriture entêtes dans fichier csv
            
            # Initialisation liste des url des livres pour cette catégorie
            
            url_book_cat = []
            valid_url, response = validation_url(url_cat)
            if valid_url:
                soup_cat = bs4.BeautifulSoup(response.text, "lxml")
                # Recherche du nombre de pages:
                nombre_pages = nombre_page_categorie(soup_cat)

                if nombre_pages > 1:
                    # Pour chaque page on récupère les url des livres dans une liste
                    for i in range(1, nombre_pages + 1):
                        # Mise en forme url de la page i:
                        url_cat_p = url_cat.replace("index.html", '') + "page-" + str(i) + ".html"
                        valid_url_p, response = validation_url(url_cat_p)
                        if valid_url_p:
                            # Parser lxml BeautiFul Soup pour analyse du html
                            soup_cat = bs4.BeautifulSoup(response.text, "lxml")
                            # On récupère en liste les url des livres de cette catégorie
                            url_book_cat = list_book_cat(soup_cat, url_book_cat)
                # Si nb_page n'est pas du type bs4.elemnt.Tag: il n'y a qu'une page
                else:
                    # On récupère en liste les url des livres de cette catégorie
                    url_book_cat = list_book_cat(soup_cat, url_book_cat)

            # Récupération des données de tous les livres d'une catégorie
            for url in url_book_cat:
                # Ecriture des données pour ce livre
                data_one_book(url, cat)
                time.sleep(0.3)  # Delai imposé pour éviter blocage du site
            