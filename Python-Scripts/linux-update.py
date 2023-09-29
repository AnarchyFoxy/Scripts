import subprocess

# Odśwież listę repozytoriów
def odswiez_liste_repozytoriow():
    subprocess.run(["sudo", "apt", "update"])

# Zaktualizuj system
def zaktualizuj_system():
    subprocess.run(["sudo", "apt", "upgrade", "-y"])

# Zaktualizuj snap
def zaktualizuj_snap():
    subprocess.run(["sudo", "snap", "refresh"])

# Zaktualizuj flatpak
def zaktualizuj_flatpak():
    subprocess.run(["flatpak", "update", "-y"])

if __name__ == "__main__":
    print("Rozpoczynam odświeżanie listy repozytoriów...")
    odswiez_liste_repozytoriow()

    print("Rozpoczynam aktualizację systemu...")
    zaktualizuj_system()

    print("Rozpoczynam aktualizację snapów...")
    zaktualizuj_snap()

    print("Rozpoczynam aktualizację flatpaka...")
    zaktualizuj_flatpak()

    print("Aktualizacja zakończona.")
