# ZipZip - 50 points

Le zip fourni pour ce challenge est protégé par un mot de passe, pour le craquer on va utiliser le tool fcrackzip, avec les options 'u' pour être certain que le mot de passe ouvre l'archive, 'D' pour une attaque par dictionnaire et 'p' pour indiquer le chemin du dictionnaire à utiliser :

```
fcrackzip topsecret.zip -u -D -p  rockyou.txt
	PASSWORD FOUND!!!!: pw == girlpower007
```

on peut maintenant ouvrir l'archive avec ce mot de passe :

```
unzip -P girlpower007 topsecret.zip
```

on obtient un fichier texte `FAN-DE-JAMES-BOND.txt`  qu'il faut lire attentivement pour y trouver la ligne :

````
"Un jour un informaticien m'a dit : pour capturer le drapeau de ce challenge il suffira de saisir 'L3_gr4s_c_3st_la_v1e'
````



