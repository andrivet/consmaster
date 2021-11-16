
# Historique

## Consmaster version 0.6

Consmaster a été porté sur PySide6 (Qt6) par Sébastien Andrivet parce que la version précédente utilisait PySide qui ne s'installe plus sur les versions récentes de Linux (Ubuntu, Debian).


## Consmaster version 0.5

Consmaster a été réalisé par Josué Melka, Calev Eliacheff et David Calmeille dans le cadre du projet de L2.

Ce programme a pour but de vous permettre de vous entrainer à manipuler les différentes représentations lisp : listes simples, notation à points et représentation graphique des doublets.


# INSTALLATION (sous ubuntu)

Pour installer Consmaster, décompressez l'archive dans le répertoire de votre choix. Consmaster peut fonctionner en mode portable depuis le répertoire dans lequel vous l'avez mis.

Dans la console, utilisez la commande `cd` pour vous placer dans le répertoire `consmaster`.

Pour installer toutes les dépendances de Consmaster, entrer la commande:

    bash install-ubuntu.sh

Soyez patient, le téléchargement des dépences prend plusieurs minutes.

# REMARQUES GÉNÉRALES

Attention, ne fermez pas la console pendant l'utilisation du programme sinon vous provoquerez son arrêt.

Le logiciel est prévu à l'origine pour fonctionner avec un serveur qui enregistre votre progression, mais la version fournie ici peut très bien fonctionner localement.

Ne faites pas attention aux éventuels messages d'erreur résultant de l'absence de connexion au serveur.

# UTILISATION DU LOGICIEL

Au premier démarrage du programme, n'hésitez pas à vous enregistrer pour conserver votre progression dans les exercices.

## Mode Standard <-> Dotted

Ce mode vous permet de vous entrainer à passer de la notation simple (normal) à la notation à points (dotted). Les expressions sont tantôt données au format "normal", tantôt au format "dotted", à vous de donner l'expression correspondante dans l'autre format.

Attention à la casse (caractères majuscule ou minuscule). Si vous ne respectez pas la casse des caractères, l'expression sera considérée comme fausse.

Consmaster ne corrige pas le pretty print : faites attention à ne pas prendre de mauvaises habitudes...

## Mode Expr -> Graphique

Ce mode vous permet de vous entrainer à passer de la notation simple (normal) à la représentation graphique. Pour ajouter un doublet ou un atome utilisez respectivement les boutons "Add Cons" et "Add Atom". "Remove" supprime l'élément courant (en rouge). "Garbage collector" permet de supprimer du schéma tous les doublets et atomes qui ne sont pas connectés. "Clean All" permet de repartir à zéro. "Auto-layout" permet d'ajuster automatiquement le positionnement des doublets et atomes pour avoir un schéma propre.

Pensez à agrandir la fenêtre si les éléments se chevauchent et le schéma devient illisible...
Utilisez le clic droit (cliquer/glisser) pour créer les liens.
Un double clic sur un atome permet de modifier son contenu.

## Mode Graphique -> Expr

Ce mode vous permet de vous entrainer à passer de la notation graphique à la notation simple (normal).

La aussi le pretty print n'est pas vérifié. Faites attention à bien respecter les espaces entre chaque atome et entre les parenthèses. Attention il n'y a jamais d'espace après une parenthèse ouvrante ou avant une parenthèse fermante.



# UTILISATION DE CONS_DRAWING POUR CREER DES SCHEMAS

Pour créer des schémas pour répondre aux exercices du cours de lisp, vous pouvez lancer le programme Cons_drawing :

Placez-vous une fois de plus dans le répertoire `src` de `consmaster` :

    cd consmaster/src

Puis lancez :

    python3 cons_drawing.py

Vous pouvez dessiner votre schéma correspondant avec les mêmes outils que dans Consmaster. Vous pouvez alors enregistrer le schéma en cliquant sur le bouton "prendre une capture". Choisissez un nom et un emplacement pour enregistrer l'image.
Vous pouvez ensuite importer cette image dans votre traitement de texte favori pour rédiger les réponses aux exercices.
