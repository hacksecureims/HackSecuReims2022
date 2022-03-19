# Review the basics - 150 points

La structure du message ressemble à deux colonnes de hash suivi d'un caractère. Si l'on prête attention, on remarque que certains hashs se répètent dans les colonnes, ce qui nous donne un indice sur la taille potentielle du message d'origine de chacun de ces hashs (quelques lettres tout au plus). De plus les lignes qui font des répétitions sur la colonne de gauche se trouvent au même endroit sur la colonne de droite, ce qui indique que les messages des deux colonnes sont très probablement le même.

Il faut essayer de trouver le format des hashs, pour cela j'ai utilisé l'utilitaire hash-identifier présent par défaut sous Kali :

```
hash-identifier 0e11e37cc1f49780e021a014634b7164

   #########################################################################
   #     __  __                     __           ______    _____           #
   #    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
   #    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
   #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
   #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
   #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
   #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
   #                                                             By Zion3R #
   #                                                    www.Blackploit.com #
   #                                                   Root@Blackploit.com #
   #########################################################################
--------------------------------------------------

Possible Hashs:
[+] MD5
[+] Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))

Least Possible Hashs:
[+] RAdmin v2.x
[+] NTLM
[+] MD4
[+] MD2
[+] MD5(HMAC)
[+] MD4(HMAC)
[+] MD2(HMAC)
[+] MD5(HMAC(Wordpress))
[+] Haval-128
[+] Haval-128(HMAC)
[+] RipeMD-128
[+] RipeMD-128(HMAC)
[+] SNEFRU-128
[+] SNEFRU-128(HMAC)
[+] Tiger-128
[+] Tiger-128(HMAC)
[+] md5($pass.$salt)
[+] md5($salt.$pass)
[+] md5($salt.$pass.$salt)
[+] md5($salt.$pass.$username)
[+] md5($salt.md5($pass))
[+] md5($salt.md5($pass))
[+] md5($salt.md5($pass.$salt))
[+] md5($salt.md5($pass.$salt))
[+] md5($salt.md5($salt.$pass))
[+] md5($salt.md5(md5($pass).$salt))
[+] md5($username.0.$pass)
[+] md5($username.LF.$pass)
[+] md5($username.md5($pass).$salt)
[+] md5(md5($pass))
[+] md5(md5($pass).$salt)
[+] md5(md5($pass).md5($salt))
[+] md5(md5($salt).$pass)
[+] md5(md5($salt).md5($pass))
[+] md5(md5($username.$pass).$salt)
[+] md5(md5(md5($pass)))
[+] md5(md5(md5(md5($pass))))
[+] md5(md5(md5(md5(md5($pass)))))
[+] md5(sha1($pass))
[+] md5(sha1(md5($pass)))
[+] md5(sha1(md5(sha1($pass))))
[+] md5(strtoupper(md5($pass)))
--------------------------------------------------
```

Il faut isoler les hashs dans un fichier pour essayer de les brut-force avec hashcat en mode incrémental en essayant les formats les plus courants :

```bash
# md5
hashcat -m 0 -a 3 -i -o output.txt hash.txt ?a?a?a?a?a?a?a
# ntlm
hashcat -m 1000 -a 3 -i -o output.txt hash.txt ?a?a?a?a?a?a?a
```

Les hashs de la colonne de droite sont des md5 et la colonne de gauche sont des ntlm et correspondent chacun à une seule lettre.

Il faut maintenant remplacer les hash par la lettre auquel ils correspondent : 

```
 H|HS//
 S|SF//
 R|RN//
 {|{S//
 Y|Ye//
 o|o0//
 u|ul//
 _|_f//
 m|mb//
 u|uD//
 s|sB//
 t|t2//
 _|_M//
 t|t1//
 r|r9//
 y|yX//
 _|_a//
 6|6W//
 4|45//
 t|tk//
 i|iM//
 m|mH//
 e|ed//
 s|sT//
 _|_X//
 h|hz//
 a|aE//
 r|rx//
 d|dO//
 e|ei//
 r|rl//
 }|}9//
```

On lit dans les colonnes : "HSR{You_must_try_64times_harder}", ce qui n'est pas le flag.

Pour trouver le flag il faut maintenant lire la colonne de caractère supplémentaire : "SFNSe0lfbDB2M19XaW5kMHdTXzExOil9" puis le décoder comme une base64 :

```
echo "SFNSe0lfbDB2M19XaW5kMHdTXzExOil9" | base64 -d
```

Ce qui donne le flag : "HSR{I_l0v3_Wind0wS_11:)}
