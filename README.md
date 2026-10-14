Pour l’utiliser, mets ranger.bat et ranger.py à la racine du dossier à trier, puis double-clique sur le .bat. Il faut que Python soit installé.

Déplacement : les fichiers sont déplacés, pas copiés.
Noms en double : si deux fichiers ont le même nom, le second devient nom_1.ext, pour ne rien écraser.
Sans extension : ces fichiers vont dans SANS_EXTENSION.
Fichiers ignorés : le script, le .bat et le dossier fichier ranger ne sont jamais déplacés.
Sous-dossiers : par défaut, seuls les fichiers à la racine sont rangés. Pour trier aussi ceux des sous-dossiers, passe RECURSIF = True en haut de ranger.py. 
Attention : ça peut casser un projet dont les fichiers dépendent de leur emplacement.
Fichiers C# : ils vont dans le dossier CS, puisque l’extension est .cs.
