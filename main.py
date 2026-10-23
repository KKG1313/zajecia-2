class Logger:
    """Menedżer kontekstu wypisujący początek i koniec sekcji logowania."""

    def __enter__(self):
        print("Start sekcji logowania")
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Koniec sekcji logowania")
        return False


with Logger():
    print("Wykonuję obliczenia")


class FileWriter:
    """Menedżer kontekstu otwierający plik do zapisu i zawsze go zamykający."""

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = open(self.path, "w")
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file.close()
        if exc_type is not None:
            print(f"Błąd podczas zapisu: {exc_value}")
        return False


# Zadanie 2: zapis bez błędu
with FileWriter("eksperyment.txt") as file:
    file.write("Próbka 1\n")
    file.write("Próbka 2\n")
print("Zapisano plik eksperyment.txt")

# Zadanie 3: zapis z błędem
try:
    with FileWriter("eksperyment_blad.txt") as file:
        file.write("Próbka 3\n")
        raise ValueError("brak odczynnika")
except ValueError:
    print("Wyjątek nie został stłumiony: program go zauważył")