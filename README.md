# AZERTYtoDigiKeyboard
Permet de transformer un string en AZERTY pour le rendre compatible avec DigiKeyboard.h natif.

Supporte la grande majorité des caractères requis.

Il suffit d'ajouter en argument le string AZERTY pour qu'il soit directement converti en instruction.

EX: `./main.py powershell -noexit -command "[console]::WindowWidth=100; [console]::WindowHeight=50; [console]::BufferWidth=[console]::WindowWidth"`

Sortie : 
```ino
  DigiKeyboard.print("pozershell 6noexit 6co;;qnd 3");
  DigiKeyboard.sendKeyStroke(KEY_5, MOD_ALT_RIGHT);
  DigiKeyboard.print("console");
  DigiKeyboard.sendKeyStroke(45, MOD_ALT_RIGHT);
  DigiKeyboard.print("..ZindozZidth=!, ");
  DigiKeyboard.sendKeyStroke(KEY_5, MOD_ALT_RIGHT);
  DigiKeyboard.print("console");
  DigiKeyboard.sendKeyStroke(45, MOD_ALT_RIGHT);
  DigiKeyboard.print("..ZindozHeight=!, ");
  DigiKeyboard.sendKeyStroke(KEY_5, MOD_ALT_RIGHT);
  DigiKeyboard.print("console");
  DigiKeyboard.sendKeyStroke(45, MOD_ALT_RIGHT);
  DigiKeyboard.print("..BufferZidth=");
  DigiKeyboard.sendKeyStroke(KEY_5, MOD_ALT_RIGHT);
  DigiKeyboard.print("console");
  DigiKeyboard.sendKeyStroke(45, MOD_ALT_RIGHT);
  DigiKeyboard.print("..ZindozZidth3");
  DigiKeyboard.println();
```
