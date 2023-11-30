




class Device:
    nev = ' '
    allapot = False


    def __init__(self, nev):
        self.nev = nev
        

    def bekapcsol(self):
        self.allapot = True

    def kikapcsol(self):
        self.allapot = False

    def milyenAllapot(self):
        if self.allapot:
            return 'bekapcsolva'
        else:
            return 'kicsapcsolva'
        
    def __str__(self):
        return f"{self.nev} ({self.milyenAllapot()})"       
        

dev1 = Device('Egér')
dev1.bekapcsol()
dev2 = Device('Párhuzamos port')

eszkozok = [
    dev1,
    dev2,
    Device('Monitor'),
    Device('Rajztábla')
]

eszkozok[3].bekapcsol()
eszkozok[0].kikapcsol()

for e in eszkozok:
    print(e)

print(dev1.milyenAllapot())










