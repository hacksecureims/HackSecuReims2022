# Bas les masques ! - 40 points

Ce challenge est une substitution poly-alphabétique (vignère) pour chaque lettre du message, on a été appliqué un décalage dans l'alphabet différent. Pour ce challenge, le début de la clé est fournie par l'énoncé : "Ami, entends tu le vol noir des corbeaux" c'est le premier vers du chant des partisans.

```python
enc = "LMOYRKVRHKMXPGGOCRSKFPQWECEWINOKGOJQSNDYSURXLRQVSGKICOSGYYEUVZWFSDLVVSYIXRCXVYQGYRTAOCGIGAIHTRVPWSQSDJMFDMJASGCEKWNGLWHWOCADMVFXTIWBITEMBAPQXNOAOJMLGECIFLMQXNWNFUYOLIFDCVEXDQDYTRPXMGIQVGNXWLGECUIROIHNOYLMGNMUTQAMAQXDWDCTRBMIEEIRWWWQLMKQBWCCWPSFOKRVMEFHPZJGJHBNFQWFLNZMFWLIXVNAIHDADMMJMXYINKZFTKEZOTVTEHNXHVHHRLLFBHQFVHLNLPBGOXRSISEJQLHXUFHREOGDXVCVSIVRYEUHBDRZDOFGWYLJOEUICYZKEDAVVYSRKIXOJGSEJEXCIFZMKEKRZIYZSZVXYLWWGYALIYEJADHMPVUFRSGGFNPUZMSQZIVKMRHYFTCFGGYAIMDXHEAJRFVNBUHWDSBFISEUXIFFUPEFLVCVFUWIQWMKMRXUVCEQCRLHVESNWZRMLSZFRRUFPZQIKAELTVYTMEZKGQUMBCZWMMGVHCJWJMMGJDEFSMCTQMWPOZMFDBYGRDBZANRANWMHMNTYPXQOVWABSEWUUUXSUDQEHDWNNOCOAUSYVYITHOCDHURGWTLMZPVOGNRVZBAEIHCKDVGKBQBEXSZROZWXBYWCLNZQGOUYUFWJTKROZARSIYVILGQGVKIFSWVNPPSNFVYMSOIGWVCGECASCABRGGETMQIDQKLVYJEHEXHEINHWBBOURHEAFOQEMKUXPEHELWAK"
key = "Ami, entends-tu le vol noir des corbeaux sur nos plaines Ami, entends-tu les cris sourds du pays qu'on enchaîne Ohé, partisans, ouvriers et paysans c'est l'alarme Ce soir l'ennemi connaîtra le prix du sang et des larmes Montez de la mine, descendez des collines, camarades, Sortez de la paille les fusils, la mitraille, les grenades, Ohé, les tueurs, à vos armes et vos couteaux, tirez vite, Ohé, saboteurs, attention à ton fardeau, dynamite. C'est nous qui brisons les barreaux des prisons pour nos frères La haine à nos trousses et la faim qui nous pousse, la misère II y a des pays où les gens au creux des lits font des rêves Ici, nous, vois-tu, nous on marche, nous on tue ou on crève. Ici, chacun sait ce qu'il veut, ce qu'il fait quand il passe Ami, si tu tombes, un ami sort de l'ombre à ta place, Demain du sang noir séchera au grand soleil sur nos routes Chantez, compagnons, dans la nuit la liberté nous écoute. Ami, entends-tu les cris sourds du pays qu'on enchaîne Ami, entends-tu le vol noir du corbeau sur la plaine"

# supprimer les espaces, etc., remplacer les lettres accentuées, puis tout mettre en majuscules.
key = key.replace(" ","").replace(",","").replace("'","").replace("-","").replace(".","").replace("à","a").replace("é","e").replace("è","e").replace('î','i').upper()

# appliquer le décalage dans l'alphabet en fonction de la valeur de la clé
msg = ""
ref = ord('A')
for i in range(len(enc)):
	c = ord(enc[i]) - ref
	m = ord(key[i]) - ref
	msg += chr((c - m)%26 + ref)
print(msg)
```

Le message déchiffré :

LA GUERRE EST DECLAREE COMME CONVENU NOUS DEVONS METTRE NOTRE PLAN EN ACTION APRES AVOIR EFFECTUER TOUTES TES TACHES DAPPROVISIONNEMENT TU DEVRAS METTRE EN ACTION LE PLAN B J ESPERE QUE TU T EN SOUVIENS C EST LE PLAN QUI VIENT JUSTE APRES LE PLAN A ET JUSTE AVANT LE PLAN C JE TE TROLL MAIS L HEURE EST GRAVE TU DEVRAS DONC ME REJOINDRE DEVANT LA MAIRIE DU VILLAGE FRANCAIS PORTANT LE NOM LE PLUS LONG J ESPERE QUE TU LE TROUVERA RAPIDEMENT CAR LA SOLUTION DE CE CHALLENGE EST JUSTEMENT LE NOM DE CE VILLAGE JE TE SOUHAITE BONNE CHANCE MON JEUNE AMI ENCORE UNE CHOSC PEUX TU M APPORTER DES KINDER BUENO NUAND TU IRA EN COURSE J ADORE CA J ARRETE LE TROLL DESOLE MAIS CETTE GUERRE ME STRESS TERRIBLEMENT J ESPERE QUE L ON EN VIENDRA VITE ABOUT VU QUE JE NE SAIS PLUS QUOI DIRE J EN AI PAS D AUTRE CHOIX QUE DE FAIRE DU PADDING LE PADDING CONSISTE A MEUBLER LA FIN DUN MESSAGE AFIN QUE CELUI CI RESPECTE LA LONGUEUR DESIREE ICI MON TEXTE DE DECHIFFREMENT EST LONG DONC MON MESSAGE EST LONG



Après quelques recherches on trouve le flag : "Saint-Remy-en-Bouzemont-Saint-Genest-et-Isson"
