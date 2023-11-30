



class Media:
    listen = False

    def __init__(self, cim, eloado,):
        self.cim = cim 
        self.eloado = eloado

    def star(self):
        self.listen = True

    def stop(self):
        self.listen = False

    def milyenAllapot(self):
        if self.listen:
            return 'hallható'
        else:
            return 'elnémúlt'

    def __str__(self):
        return f"Az előadó: {self.eloado}\nA zene címe: {self.cim}\nÁllapot: {self.milyenAllapot()}"
    
music = Media("Zámbó Jimmy", "Egy jó asszony mindnet meg bocsájt")
print(music)








