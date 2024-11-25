class Bussiness:
    name = "John"
    sales = 5000
    profit = 1000
    product = "lassan"
    marketing = 500

    def show_data(self):
        print(f"Name = {self.name}")
        print(f"Sales = {self.sales}")
        print(f"Profit = {self.profit}")
        print(f"Product = {self.product}")
        print(f"Marketing = {self.marketing}")


p1 = Bussiness()
p2 = Bussiness()

p2.name = "Rahul"
p2.sales = 7000
p2.profit = 2000
p2.product = "Adrak"
p2.marketing = 700

p1.show_data()
p2.show_data()

# print("John")
# print(f"Name = {p1.name}")
# print(f"Sales = {p1.sales}")
# print(f"Profit = {p1.profit}")
# print(f"Product = {p1.product}")
# print(f"Marketing = {p1.marketing}")

# print("Rahul")
# print(f"Name = {p2.name}")
# print(f"Sales = {p2.sales}")
# print(f"Profit = {p2.profit}")
# print(f"Product = {p2.product}")
# print(f"Marketing = {p2.marketing}")

