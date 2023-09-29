import subprocess

# Odśwież listę repozytoriów
def odswiez_liste_repozytoriow():
    subprocess.run(["sudo", "apt", "update"])

# Zaktualizuj system
def zaktualizuj_system():
    subprocess.run(["sudo", "apt", "upgrade", "-y"])

if __name__ == "__main__":
    print("Rozpoczynam odświeżanie listy repozytoriów...")
    odswiez_liste_repozytoriow()

    print("Rozpoczynam aktualizację systemu...")
    zaktualizuj_system()

    print("Aktualizacja zakończona.")
