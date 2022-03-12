#! /bin/python3
enc = "LMOYRKVRHKMXPGGOCRSKFPQWECEWINOKGOJQSNDYSURXLRQVSGKICOSGYYEUVZWFSDLVVSYIXRCXVYQGYRTAOCGIGAIHTRVPWSQSDJMFDMJASGCEKWNGLWHWOCADMVFXTIWBITEMBAPQXNOAOJMLGECIFLMQXNWNFUYOLIFDCVEXDQDYTRPXMGIQVGNXWLGECUIROIHNOYLMGNMUTQAMAQXDWDCTRBMIEEIRWWWQLMKQBWCCWPSFOKRVMEFHPZJGJHBNFQWFLNZMFWLIXVNAIHDADMMJMXYINKZFTKEZOTVTEHNXHVHHRLLFBHQFVHLNLPBGOXRSISEJQLHXUFHREOGDXVCVSIVRYEUHBDRZDOFGWYLJOEUICYZKEDAVVYSRKIXOJGSEJEXCIFZMKEKRZIYZSZVXYLWWGYALIYEJADHMPVUFRSGGFNPUZMSQZIVKMRHYFTCFGGYAIMDXHEAJRFVNBUHWDSBFISEUXIFFUPEFLVCVFUWIQWMKMRXUVCEQCRLHVESNWZRMLSZFRRUFPZQIKAELTVYTMEZKGQUMBCZWMMGVHCJWJMMGJDEFSMCTQMWPOZMFDBYGRDBZANRANWMHMNTYPXQOVWABSEWUUUXSUDQEHDWNNOCOAUSYVYITHOCDHURGWTLMZPVOGNRVZBAEIHCKDVGKBQBEXSZROZWXBYWCLNZQGOUYUFWJTKROZARSIYVILGQGVKIFSWVNPPSNFVYMSOIGWVCGECASCABRGGETMQIDQKLVYJEHEXHEINHWBBOURHEAFOQEMKUXPEHELWAK"
key = "Ami, entends-tu le vol noir des corbeaux sur nos plaines Ami, entends-tu les cris sourds du pays qu'on enchaîne Ohé, partisans, ouvriers et paysans c'est l'alarme Ce soir l'ennemi connaîtra le prix du sang et des larmes Montez de la mine, descendez des collines, camarades, Sortez de la paille les fusils, la mitraille, les grenades, Ohé, les tueurs, à vos armes et vos couteaux, tirez vite, Ohé, saboteurs, attention à ton fardeau, dynamite. C'est nous qui brisons les barreaux des prisons pour nos frères La haine à nos trousses et la faim qui nous pousse, la misère II y a des pays où les gens au creux des lits font des rêves Ici, nous, vois-tu, nous on marche, nous on tue ou on crève. Ici, chacun sait ce qu'il veut, ce qu'il fait quand il passe Ami, si tu tombes, un ami sort de l'ombre à ta place, Demain du sang noir séchera au grand soleil sur nos routes Chantez, compagnons, dans la nuit la liberté nous écoute. Ami, entends-tu les cris sourds du pays qu'on enchaîne Ami, entends-tu le vol noir du corbeau sur la plaine"
key = key.replace(" ","").replace(",","").replace("'","").replace("-","").replace(".","").replace("à","a").replace("é","e").replace("è","e").replace('î','i').upper() # supprimer les espaces, etc, remplacer les lettres accentué, puis tout mettre en majuscule.

msg = ""
ref = ord('A')
for i in range(len(enc)):
	c = ord(enc[i]) - ref
	m = ord(key[i]) - ref
	msg += chr((c - m)%26 + ref)
print(msg)
