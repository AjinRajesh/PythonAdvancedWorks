class Category:
    def __init__(self):
        self.category_name=input("Enter category name: ")

    def show_category(self):
        print("Category:",self.category_name)

class Product(Category):
    def __init__(self):
        super().__init__()
        self.product_name=input("Enter product name: ")
        self.price=int(input("Enter price of one product: "))
        self.quantity=int(input("Enter Quantity: "))
        print()

    def total_price(self):
        net_price=self.price * self.quantity
        print("Total price of product:",net_price)
        print()

p=Product()
p.show_category()
p.total_price()