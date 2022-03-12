# IAMBATMAN - 100 points

Ce challenge nous fournit quelques fichiers issus de l'AppData d'un compte admin d'une machine :

 - `AppData/S-1-5-21-2000028255-643743919-4201201913-1001/620946c8-8a36-486b-b667-ba6658a0c5c4`: ce fichier provient de l'emplacement suivant : `C:\Users\$USER\AppData\Roaming\Microsoft\Protect\$SUID\$GUID`. Il contient la MasterKey DPAPI de l'utilisateur, chiffré grâce à son mot de passe et son SUID.
 - `AppData/D17EECDD173964A24FDC683EFFB80A06`: ce fichier provient soit de `C:\Users\$USER\AppData\Local\Microsoft\Credentials\` soit de `C:\Users\$USER\AppData\Local\Microsoft\Credentials\`. C'est un Blob DPAPI, il a était chiffré avec un MasterKey.

Comme l'on connaît le mot de passe de l'utilisateur, et que le SUID est dans le chemin du fichier, il est possible de déchiffrer la MasterKey avec un script présent dans Impacket :

```
dpapi.py masterkey -file ./AppData/S-1-5-21-2000028255-643743919-4201201913-1001/620946c8-8a36-486b-b667-ba6658a0c5c4 -sid "S-1-5-21-2000028255-643743919-4201201913-1001" -password "iambatman"

Impacket v0.9.25.dev1+20220105.151306.10e53952 - Copyright 2021 SecureAuth Corporation

[MASTERKEYFILE]
Version     :        2 (2)
Guid        : 620946c8-8a36-486b-b667-ba6658a0c5c4
Flags       :        5 (5)
Policy      :       15 (21)
MasterKeyLen: 000000b0 (176)
BackupKeyLen: 00000090 (144)
CredHistLen : 00000014 (20)
DomainKeyLen: 00000000 (0)

Decrypted key with User Key (SHA1)
Decrypted key: 0xd4aff235ce4baa4b9a02a53f14ddd10624901bc913c5b354be4bdfb0801cbcc4f8a6ee2056a260d6313c6f1275b301a54309c3df11c0e2351456c2b0c56b027f
```

Maintenant que l'on connaît la MasterKey, il est possible de déchiffrer le Blob :

```
dpapi.py credential -file ./AppData/D17EECDD173964A24FDC683EFFB80A06 -key "0xd4aff235ce4baa4b9a02a53f14ddd10624901bc913c5b354be4bdfb0801cbcc4f8a6ee2056a260d6313c6f1275b301a54309c3df11c0e2351456c2b0c56b027f"

Impacket v0.9.25.dev1+20220105.151306.10e53952 - Copyright 2021 SecureAuth Corporation

[CREDENTIAL]
LastWritten : 2022-03-01 12:20:27
Flags       : 0x00000030 (CRED_FLAGS_REQUIRE_CONFIRMATION|CRED_FLAGS_WILDCARD_MATCH)
Persist     : 0x00000003 (CRED_PERSIST_ENTERPRISE)
Type        : 0x00000002 (CRED_TYPE_DOMAIN_PASSWORD)
Target      : Domain:target=hacksecureims.eu
Description : 
Unknown     : 
Username    : Administrateur
Unknown     : HSR{KuSK!64@7fy9qR@8dUt#6S%}
```
Le flag est : HSR{KuSK!64@7fy9qR@8dUt#6S%}


## Quelques liens utiles pour aller plus loin sur le sujet :

- Un rappel sur le fonctionnement de DPAPI : https://www.synacktiv.com/ressources/synacktiv_DPAPI_Sthack.pdf
- Tool utilisé pour résoudre ce challenge : https://github.com/SecureAuthCorp/impacket/blob/master/examples/dpapi.py
- Tool possible pour résoudre ce challenge sous Windows : https://github.com/ParrotSec/mimikatz
- Tool pour l'exploitation automatisée (Présenté lors des conférences) : https://github.com/login-securite/DonPAPI
- Fonctionnement, configuration et structures de fichiers détaillés de DPAPI : https://www.passcape.com/index.php?section=docsys&cmd=details&id=28
