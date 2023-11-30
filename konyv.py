




class Book:
    cim = " "
    szerzo = " "
    kiadas = 0 

    def __init__(self, cim, szerzo, kiadas):
        self.cim = cim 
        self.szerzo = szerzo
        self.kiadas = kiadas 

konyvek = []
def peldany():
    konyvek.append(Book("Harry Potter", "J.K. Rowling", 1997))
    konyvek.append(Book("Hobbit", "J.R.R. Tolkein", 1938))
    konyvek.append(Book("Trónok harca", "Marton George R.R.", 1996))
    for item in konyvek:
        print(f"Cím: {item.cim}, Szerző: {item.szerzo}, Kiadási év: {item.kiadas}")



def main():
    peldany()
main()




