# -*-coding:Utf-8 -*

"""

Created on Sun Jun 26 05:58:13 2022

Module requêtes url

"""
import requests  # module qui permet d'interagir avec une url


#      Requête sur une url, avec gestion de quelques exceptions  #


def validation_url(url):

    """
    fonction vérifiant la validité de l'url entrée en paramètre.
    
    Un message est renvoyé si une exception est levée.
    Différents types d'erreur sont détectés.
    
    Args:
        string : url de la page testée
    Return:
        bool : True si la requête s'est bien passée, False dans le cas
        contraire
        response : résultat de la requête. Résultat vide si la requête
        s'est mal passée
    Raises:
        InvalidSchema:  si l'url saisie est invalide.
                        Il manque http:// ou https:// au début
        InvalidURL:  l'url saisie n'est pas reconnue comme une url
        Timeout:  si aucun début de réponse à la requête au bout de 3s
        HTTPError: La page n'existe pas ou bien le serveur ne répond pas.
                  Erreurs de type 40X ou 50X.
        ConnectionError: problème de connexion au réseau
    """
    
    # Par défaut la requête est invalidée, elle ne sera validée que si tout est ok
    
    valide = False
   
    # Initialisation de la réponse de la requête.
    
    resp = requests.models.Response()
    
    try:
        resp = requests.get(url, timeout=3)
        resp.raise_for_status()  # Lève l'exception HTTPError
    except requests.exceptions.InvalidSchema:
        print("L'adresse saisie est invalide")
    except requests.exceptions.InvalidURL:
        print("L'adresse saisie est invalide")
    except requests.exceptions.Timeout:
        print('La requête est trop longue. Le site ne répond pas.')
    except requests.exceptions.HTTPError as e:
        print("La page n'existe pas ou le serveur ne réponds pas. Erreur:", e)
    except requests.exceptions.ConnectionError:
        print("La connexion au réseau a échouée")
    else:
        if resp.ok:  # le code de statut est 200
            valide = True
    return(valide, resp)


URL_INDEX = 'http://books.toscrape.com/' # URL sélectionnée valide