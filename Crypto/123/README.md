# 1,2,3...- 20 points

comme son nom l'indique pour déchiffré le message il faut pour chaque mot réaliser un décalage dans l'alphabet (ROT) de 1 lettre pour le premiers mot, de 2 lettre pour le second mot, de 3 lettre pour le derniers mot.

```python
enc = "aqzun nmsp qolrsbo hw njgpodji piom wxoxs ugfuslwfwj cvj fhucyuhui atiigth rs pundhr yaf op mo vnbbjpn"
decalage=1
msg = ""
for char in enc:
	if char == ' ': # fin de mot
		decalage += 1
		msg += ' '
		continue
	char = ord(char) - ord('a')
	char += decalage
	char %= 26
	char += ord('a')
	msg += chr(char)
print(msg)
```

Attention un espace c'est glissé avant le derniers mot, il faut le supprimer manuellement pour que le script fonctionne

Ce qui donne le message : "bravo pour trouver la solution vous devez concatener les premieres lettres de chaque mot de ce message"

le flag est donc : bptlsvdclldcmdcm
