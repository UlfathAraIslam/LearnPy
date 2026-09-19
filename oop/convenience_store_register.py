class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def scan(self):
        print(f"Scanned: {self.name} - {self.price}")
        return self.price

