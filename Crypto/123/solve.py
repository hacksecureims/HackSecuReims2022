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
