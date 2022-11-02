class Account:
    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name
        self.address = "null"
        self.phone_number = 0
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)
