# bend_control

The Bend Control project
=======================
![GUI](https://user-images.githubusercontent.com/74402649/173091997-91704721-b7f8-4ba4-814e-5833e5d7094b.png)

Ziel dieses Projektes ist es eine einfache Steuerung für eine Schwenkbiegemaschine bereit zu stellen. Der Benutzer kann auf der Benutzeroberfläche einen Winkel einstellen und dieser wird mit dem Betätigen des Startbutton angefahren. Außerdem kann der Biegevorgang auch mit einer Fernbedienung gestartet beziehungsweise gestoppt werden.

Als Basis dient ein Raspberry Pi 3B+, an welchen für Winkel und Anschlag ein Drehgeber (Rotary Encoder) angeschlossen ist. Die Maschine wird über eine Relaiskarte, welche am Raspberry Pi angeschlossen ist gesteuert.

![Blockschaltbild](https://user-images.githubusercontent.com/74402649/173093690-f0c3f352-85b0-4417-9725-6c1419003c65.png)

Da die Maschine eine zusätzliche Erweiterung des Blechanschlages erhalten hat, können 4 verschiedene Anschläge ausgewählt werden. Die Positionen der Anschläge sind in den folgenden Darstellung zu sehen.

![Anschlagsübersicht](https://user-images.githubusercontent.com/74402649/173094121-9cffd107-f323-4961-802a-e0d004216b90.png)

In der Datei Setting.ini können die Offsets der einzelnen Anschläge und der maximale Winkel geändert werden. Zusätzlich wird der letzte eingespeicherte Soll-Winkel abgespeichtert.

In dem folgenden Link ist das Projekt dokumentiert und die Benutzung der Software erklärt:

Youtube:



