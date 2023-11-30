import random




class MathOperations:

    def __init__(self, szam1, szam2):
        self.szam1 = szam1
        self.szam2 = szam2

    def add(self):
        return self.szam1 + self.szam2

    def sub(self):
        return self.szam1 - self.szam2

    def multi(self):
        return self.szam1 * self.szam2
    
    def div(self):
        return self.szam1 / self.szam2

    def __str__(self):
        return f"A két szám: {self.szam1} és {self.szam2}\nÖsszeadás: {self.add()}\nKivonás: {self.sub()}\nSzorozva: {self.multi()}\nElosztva: {self.div()}"
    



szamok = []
def peldany():
    for item in range(5):
        szam1 = random.randint(1,10)
        szam2 = random.randint(1,10)
        mat = MathOperations(szam1, szam2)
        szamok.append(mat)
    print(mat)



def main():
    peldany()
main()


