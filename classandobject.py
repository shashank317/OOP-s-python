class car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display(self):
        print(f"Car Brand: {self.brand}, Year: {self.year}")

c1 = car("BMW", 2020)
c2 = car("Audi", 2021)
c1.display()
c2.display()