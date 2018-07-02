class Store:

    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            "name": name,
            "price": price
        })

        #item = {'name': name, 'price': price}
        #self.items.append(item)


    def stock_price(self):
        return sum([item["price"] for item in self.items])

bonch = Store("Bonch's Store")
bonch.add_item("milk", 1050)
bonch.add_item("egg", 70)
bonch.add_item("rice", 50)
bonch.add_item("nuts", 30)
print(bonch.stock_price())