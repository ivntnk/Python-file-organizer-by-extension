import shutil
from pathlib import Path

NOM_DOSSIER_SORTIE = "fichier ranger"
SANS_EXTENSION = "SANS_EXTENSION"
RECURSIF = False # True = range aussi les fichiers des sous-dossiers

RACINE = Path(__file__).resolve().parent
DOSSIER_SORTIE = RACINE / NOM_DOSSIER_SORTIE
FICHIERS_IGNORES = {"ranger.py", "ranger.bat"}


def lister_fichiers():
    candidats = RACINE.rglob("*") if RECURSIF else RACINE.glob("*")
    for chemin in candidats:
        if not chemin.is_file():
            continue
        if chemin.name.lower() in FICHIERS_IGNORES:
            continue
        if DOSSIER_SORTIE in chemin.parents:
            continue
        yield chemin


def chemin_libre(destination: Path) -> Path:
    if not destination.exists():
        return destination
    compteur = 1
    while True:
        essai = destination.with_name(f"{destination.stem}_{compteur}{destination.suffix}")
        if not essai.exists():
            return essai
        compteur += 1


def main():
    fichiers = list(lister_fichiers())
    if not fichiers:
        print("Aucun fichier à ranger.")
        return

    DOSSIER_SORTIE.mkdir(exist_ok=True)
    compteurs = {}

    for fichier in fichiers:
        extension = fichier.suffix.lstrip(".").upper() or SANS_EXTENSION
        dossier_ext = DOSSIER_SORTIE / extension
        dossier_ext.mkdir(exist_ok=True)

        destination = chemin_libre(dossier_ext / fichier.name)
        shutil.move(str(fichier), str(destination))
        compteurs[extension] = compteurs.get(extension, 0) + 1

    print(f"{len(fichiers)} fichier(s) rangé(s) dans « {NOM_DOSSIER_SORTIE} » :\n")
    for extension in sorted(compteurs):
        print(f"  {extension:<20} {compteurs[extension]}")


if __name__ == "__main__":
    main()
