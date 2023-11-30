





class Vehicle:
    def __init__(self, rendszam):
        self.rendszam = rendszam
        self.mozog = False

    def start(self):
        if not self.mozog:
            print(f"{self.rendszam} elindult.")
            self.mozog = True
        else:
            print(f"{self.rendszam} már mozog.")

    def stop(self):
        if self.mozog:
            print(f"{self.rendszam} megállt.")
            self.mozog = False
        else:
            print(f"{self.rendszam} már áll.")

# Példa használat
auto = Vehicle("ABC123")
auto.start()
auto.stop()
auto.start()







