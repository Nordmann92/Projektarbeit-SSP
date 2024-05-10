# Projektarbeit-SSP
wir bauen ein einfaches Schere Stein Papier Spiel in Python

## Anforderungen


- spielen gegen Computer
- Namen des Spielers wählbar
- es soll der Punktestand gespeichert werden

## Programmablauf

- Begrüßung
- Name wählen
- Spielzug festlegen? Schere oder Stein oder Papier
- Vergleichen mit Computer 
- Gewinner ausgeben




### AP1) Klasse character **DONE**

Attribute:

- Name
- Punktestand = 0
- Niederlagen = 0
- Siege = 0
- Spielzug (schere, stein, papier) = 0

Methoden
- gib den Punktestand zurück
- gib den Spielzug zurück



### AP2) Funktion für den Spielernamen als Klassenmethode **DONE**

- Text ausgeben die den Spieler auffordert seinen Namen anzugeben
- Objektname vergeben mit Name des Spielers


### AP3) Funktion für Auswahl des Spielzuges **DONE**

- Text ausgeben die den Spieler auffordert seinen "move" anzugeben (schere, stein, papier)
- entsprechendes Objektattribut des spielers anpassen


### AP4) Funktion zufälliger Move für zum Beispiel NPC **DONE**  

- Funktion schreiben die einen zufälligen Spielzug auswählt und das entsprechende Objektattribut anpasst (.move)


### Funktion zum wählen des Gewinners und Verlierers **In Progress**

- return Gewinner
- für den Gewinner score +1 und win +1
- für den Verlierer score -1 und lose +1

