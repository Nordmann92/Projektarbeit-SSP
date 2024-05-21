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




### AP1(**DONE**) Klasse character

Attribute:

- Name
- Punktestand = 0
- Niederlagen = 0
- Siege = 0
- Spielzug (schere, stein, papier) = 0

Methoden
- gib den Punktestand zurück
- gib den Spielzug zurück



### AP2(**DONE**) Funktion für den Spielernamen als Klassenmethode

- Textausgeben die den Spieler auffordert seinen Namen anzugeben
- Objektname vergeben mit Name des Spielers


### AP3(**DONE**) Funktion für Auswahl des Spielzuges

- Textausgeben die den Spieler auffordert seinen "move" anzugeben (schere, stein, papier)
- entsprechendes Objektattribut des spielers anpassen


### AP4(**DONE**) Funktion zufälliger Move für zum Beispiel NPC 

- Funktion schreiben die einen zufälligen Spielzug auswählt und das entsprechende Objektattribut anpasst (.move)


### AP5(**DONE**)Funktion zum wählen des Gewinners und Verlierers

- return Gewinner
- für den Gewinner score +1 und win +1
- für den Verlierer score -1 und lose +1

