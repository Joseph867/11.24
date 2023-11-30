





class Cat:
    def __init__(self, nev, life):
        self.nev = nev
        self.life = life

    def death(self):
        while self.life != 0:
            if self.life > 0:
                self.life -= 1
                print(f"{self.nev}-nak ennyi élete van: {self.life}")
                if self.life == 0:
                    print("Neo elvesztette az összes életét")
            else:
                print("Neonak el fogytak az életei")
            



szisza = Cat("neo", 9)
szisza.death()







