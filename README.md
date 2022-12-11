# LoL Champ Select Stats

## PREREQUIS

Ces scripts utilisent python, il va donc sans dire qu'il faut l'avoir d'installé sur son ordinateur pour le bon fonctionnement
des scripts, vous pouvez télécharger la dernière version à cette adresse :  [Télécharger Python](https://www.python.org/downloads/).
Il est probable que vous deviez redémarrer votre pc pour que l'installation soit opérationnelle.

## UTILISATION

Vous trouverez 2 scripts:
**lol_lobby_position.py** : est à lancer à chaque début de partie, il prend la position que vous occupez dans votre lobby et l'écrit
dans le fichier *data_lol.txt*, qui s'il n'est pas déjà créé, le sera automatiquement

**script.py** : est le fichier d'analyse des données recueillies dans le fichier *data_lol.txt*, il est bon à savoir qu'un bon échantillon
pour ce genre de donnée est commence à partir de 500, voir 1000 parties. Cependant vous pouvez voir la progression de vos statistiques
quand bon vous sembles.

Si vous avez oublié de lancer le script mais que vous vous souvenez de votre position dans le lobby, vous pouvez rajouter la valeur à la main dans le
fichier *data_lol.txt* se trouvant sur votre bureau (si vous suivez mes recommendations ci-dessous), et ajouter votre position à la fin de la chaine de
nombre, sans ajouter d'espace, ni rien, simplement le nombre (first pick = 1 et last pick = 5).

Le premier script n'est malheureusement pas (encore) automatique, il faut donc penser à le lancer à chaque début de partie.

Je conseille donc la création d'un fichier en .bat contenant le code donné ci-dessous. Pour créer un fichier .bat, créez
simplement un fichier texte sur votre bureau dont vous renomerez l'extension de .txt → .bat.

## CREATION FICHIERs .BAT

Pour le fichier **script.py** :

```bat
[emplacement de votre executif python*] [emplacement global de script.py] 
cmd /k
```

Pour le fichier **lol_lobby_position.py** :

```bat
[emplacement de votre executif python*] [emplacement global de script.py]
```

*généralement situé à l'addresse suivante : ```C:/Users/[nom_user]/AppData/Local/Programs/Python/Python[version_python]/python.exe```
(penser évidemment à ne pas copier le lien tel quel et à adapter le texte entre ```[]``` à ce qui vous correspond)

### ATTENTION

**NE PAS SUPPRIMER OU RENOMMER LE FICHIER *data_lol.txt* APPARAISSANT SUR LE BUREAU**, dans le cas échéant, le fichier sera recrée à la
prochaine exécution du script, sans les données précedemment insérées.
