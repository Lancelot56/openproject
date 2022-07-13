Ceci est un utilitaire de scraping du site exemple http://books.toscrape.com/index.html.

Il extrait les donn�es des 1000 livres du site et les enregistre dans des fichiers csv (un fichier par cat�gorie de livres). 
Tous ces fichiers csv sont rang�s dans un dossier fichiers_csv dans le m�me r�pertoire que le fichier extract_book.py.
Les images des livres sont �galement t�l�charg�es et stock�es dans un dossier fichiers_img dans ce m�me r�pertoire.
Enregistrer l'ensemble des fichiers dans un dossier local de votre choix.

Dans le terminal se mettre dans ce dossier local

Environnement virtuel
https://docs.python.org/fr/3/library/venv.html?highlight=venv

Cr�er un environnement virtuel:

python -m venv env

Activer cet environnement virtuel: sur windows :
env/Scripts/activate 

sur mac ou linux:
source env/bin/activate 

Packages

Puis installer les modules n�cessaires:
python -m pip -r requirements.txt

Ex�cution

Ex�cuter le fichier principal dans cet environnement virtuel.

Python main.py