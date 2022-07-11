#-*- coding: utf-8 -*-

"""

Created on Sun Jun 26 05:29:08 2022

Module Main

"""

import os # pour navigation système sur arborescence fichiers
from settings.constantes import URL_INDEX # pour url de travail
from fonctions.categories import extractions # pour fonction de classement par catégories


#    Main  #


if __name__ == "__main__":

    

    # programme principal

    print(' Extraction en cours, veuillez patienter....')
    url_site = URL_INDEX + "index.html"
    extractions(url_site)
    print('Extraction terminée, veuillez consulter les dossiers csv et img !')