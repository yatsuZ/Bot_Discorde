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

---

## 3

---

24/04/2023 :

Ecrire exactement Ce que je dois faire.
J'ai fais une partie de la tache 1 mais je shouaite l'ameliorier.

| !last_commande :
Affichera la derniere commande du History generale avec la mention du dernier auteur.
Et
Affichera la derniere commande du History de l'auteur.

Toutes les commandes rentrée par un utilisateur depuis sa première connexion
+
De quoi se déplacer dans cet historique (en avant et en arrière):

| !Show_historie_of "user mention":
Affichera les 10 derniere commande du "user mention".
Si pas de parametre est mis alors sa sera l'Historie Generale.
On pourras naviguer dans l'historique avec les reactions.

Vider l'historique:

| !Delet_My_history "int":

Suprime les dernieres commande de l'auteur dans son Historique perso + publique.
Si int est null sa surpime juste la derniere commande.
Si int est egale a -1 surpimme TOUT.
Sinon Surprime les derniers "int" si int est superieur aux nombre d'historique Surpime tout.

TO DO:
    - Faire une UML simplifier sur comment sera gerer mes donnée USER et Historique.
    - Code les fonction.
