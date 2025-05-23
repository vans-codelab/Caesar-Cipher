
# Caesar Cipher - Verschlüsselung von Nachrichten
Die Caesar-Verschlüsselung (Caesar Cipher) ist eine der ältesten und bekanntesten Verschlüsselungsmethoden, benannt nach Julius Caesar, der sie selbst verwendet hat, um geheime Botschaften zu verschicken.


### Funktionsweise
Bei der Caesar-Verschlüsselung werden die Zeichen im Text um eine festgelegte Zahl verschoben. Diese Verschiebung erzeugt einen neuen, verschlüsselten Text. Die Methode basiert auf einer einfachen, aber effektiven Technik, bei der jedes Zeichen des Originaltextes durch ein Zeichen ersetzt wird, das eine bestimmte Anzahl von Stellen im Alphabet weiter vorne oder zurück liegt.

**Beispiel:** Der Text 'abc' wird mit einer Verschiebung von 3 Stellen zu 'def'.


### Erweiterung des Zeichensatzes
Um die Verschlüsselung noch komplexer zu gestalten, wurde in diesem Projekt der Zeichensatz erweitert. Neben den klassischen Buchstaben des lateinischen Alphabets wurden auch Zahlen und Sonderzeichen mit einbezogen, sodass eine größere Vielfalt an Zeichen verschlüsselt werden kann. Diese Erweiterung erhöht die Sicherheit und den Umfang der Verschlüsselung, sodass eine größere Vielfalt an Zeichen verschlüsselt werden kann.

### Vorteile der Caesar-Verschlüsselung
- **Einfachheit:** Die Caesar-Verschlüsselung ist leicht zu verstehen und umzusetzen.
- **Erweiterter Zeichensatz:** Durch die Erweiterung des Zeichensatzes wird der verschlüsselte Text schwieriger zu knacken.
- **Einstiegsniveau:** Ideal für Anfänger und alle, die in die Welt der Kryptografie einsteigen möchten.

### Anforderungen
- **Programmiersprache:**
Das Projekt wurde mit Python 3.11 entwickelt und getestet. 
Python kann von der offiziellen Website herunterladen und installiert werden: https://www.python.org/downloads/

- **Python-Pakete**
Das Projekt verwendet nur die Standardbibliothek von Python. Es sind keine externen Bibliotheken erforderlich.


### Nutzung
1. **Dateien herunterladen:**
   
   Klicke auf den grünen Button "Code" auf GitHub und lade das Repository als ZIP-Datei herunter.
   Entzippe den Ordner und stelle sicher, dass alle Python-Dateien im gleichen Ordner liegen.
   
3. **Programm ausführen:**
   
   Öffne die Eingabeaufforderung und navigiere in das Verzeichnis, in dem sich die Dateien befinden.
   
   Beispiel:

       cd "C:\Caesar-Cipher\"
   
   Führe **main.py** aus, um das Programm zu starten.

       python main.py
   
3. **Text verschlüsseln oder entschlüsseln:**
   
   Wähle aus, ob der Text verschlüsselt ("encode") oder entschlüsselt ("decode") werden soll. Gib dann den Text und die gewünschte Verschiebung ein, um den Text zu verschlüsseln oder zu entschlüsseln.


### Kontext
Dieses Projekt wurde im Rahmen des „100 Days of Code - The Complete Python Pro Bootcamp“-Kurses von Angela Yu auf Udemy entwickelt, in dem ich die grundlegenden Konzepte der Python-Programmierung erlernt habe. Im Anschluss entschloss ich mich, das Projekt weiter auszubauen, indem ich zusätzliche Funktionen hinzufügte und z.b. ermöglichte, nicht nur Buchstaben, sondern auch Zahlen und Sonderzeichen im Text zu verschlüsseln. Für mehr Übersichtlichkeit und eine bessere Lesbarkeit wurden außerdem ausgewählte Codeblöcke in Funktionen zusammengefasst und diese in ein separates Modul ausgelagert. Auch habe ich mögliche fehlerhafte Benutzereingaben berücksichtigt und den Code entsprechend angepasst, um diese abzufangen. 


