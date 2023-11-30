


class Employee:
    nev = " "
    fizetes = 0 


    def __init__(self, nev, fizetes):
        self.nev = nev 
        self.fizetes = fizetes


    def fizuemeles(self):
        self.fizetes += 500000

    def __(self):
        return f"{self.nev} - {self.fizetes} Ft"

alkalmazott = Employee("Sanyi", 200000)
print(alkalmazott.nev)
alkalmazott.fizuemeles()

print(alkalmazott.fizetes)
    





