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




### Klasse character

Attribute:

- Name
- Punktestand = 0
- Niederlagen = 0
- Siege = 0
- Spielzug (schere, stein, papier) = 0

Methoden
- gib den Punktestand zurück
- gib den Spielzug zurück



### Funktion für den Spielernamen

(def select_player():)

- Text ausgeben die den Spieler auffordert seinen Namen anzugeben
- Objekt erstellen mit Name des Spielers
- objekt zurück geben

### Funktion für den Spieler-move

- Text ausgeben die den Spieler auffordert seinen "move" anzugeben (schere, stein, papier)
- Objekt des spieler anpassen in der move zugewiesen wird


# Next ToDos

## NPC erstellen

-- Name vergeben
-- zufälliger move

## Funktion für Spiel gegen NPC

- return winner
- return loser