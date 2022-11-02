class Product:
    def __init__(self, product_id, price, amount, name, comments):
        self.product_id = product_id
        self.price = price
        self.amount = amount
        self.name = name
        self.comments = comments

    def add_comment(self, comment):
        self.comments.append(comment)
