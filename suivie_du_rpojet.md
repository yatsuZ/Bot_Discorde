# Mon journal de bord

## 1

---

19/04/2023 :
j'ai ajoutée des fonction telle qui son :

- on_message        -> quand un user envoie un message alors le bot repond en fonction.
- on_member_join    -> quand un nous veaux membre viens le bot le shouaite la bievenue.
- on_typing         -> quand quelqun mets plus de 10seconde pour repondre alors le bot reagis.
- on_ready          -> quand le bot est pres et viens detre demarer envoie un message au serveur,
et sur le discodre.
- delete            -> quand un user fais la commande "!king_krimson" -> surpimer les 10 dernier message.

et quelque petit modification du code.

---

## 2

---

20/04/2023 :
Je me pose des questions sur comment implementer un historique.
Car si je dois faire ajouter une ligne de code pour chaque fonction c'est pas inteligement code.
Et dans mon cahier des charger je dois stockée les historique de commande dans l'une structure de
ces structure -> une liste chainée, une pile ou une file.

Ma solution -> Crée une structure puis dans message verifier si c'est une commande et qu'elle exite
puis on ajoute.
