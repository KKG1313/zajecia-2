class Logger:
    """Menedżer kontekstu wypisujący początek i koniec sekcji logowania."""

    def __enter__(self):
        print("Start sekcji logowania")
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Koniec sekcji logowania")
        return False


with Logger():
    print("Wykonuje obliczenia")