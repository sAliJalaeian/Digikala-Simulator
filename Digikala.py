def welcome():
    print("Welcome to DIGIKALA")


def profile_page(account):
    print("Your data.....")
    print("Your name: " + str(account.name))
    print("Your phone number: " + str(account.phone_number))
    print("Your address: " + str(account.address))
    return account


class Digikala:
    def __init__(self, accounts, products):
        self.accounts = accounts
        self.products = products

    def main(self):
        welcome()
        self.selection_list(profile_page(self.login_page()))

    def selection_list(self, account):
        print("""

******* Selection List *******
Enter 1 to show products
Enter 2 to show your cart
Enter 0 to quit
   
""")
        num = int(input("Please enter a number: "))
        if num == 1:
            self.show_products(account)
        elif num == 2:
            self.cart(account)
        elif num == 0:
            self.Exit()

    def login_page(self):
        while True:
            username = str(input("Please enter the username: "))
            password = str(input("Please enter the password: "))
            if self.check_accounts(username, password) != -1:
                break
            print("Not in database!! OR Wrong password!!")
        print("Your logging in.....")
        return self.check_accounts(username, password)

    def Exit(self):
        num = int(input("Press \"0\" to exit OR press \"1\" to go to the login page: "))
        if num == 1:
            self.main()

    def cart(self, account):
        print("Your products you want to buy....\n")
        for product in account.cart:
            print(str(product.name) + "\t\t\t" + str(product.product_id) + "\t\t\t" + str(product.price))
        self.selection_list(account)

    def check_accounts(self, username, password):
        for account in self.accounts:
            if account.username == username and account.password == password:
                return account
        return -1

    def show_products(self, account):
        for product in self.products:
            print(str(product.name) + "\t\t\t" + str(product.product_id) + "\t\t\t" + str(product.price))
        print("""


******* Selection List *******
Enter product id to show this product
Enter 0 to quit

""")
        number = int(input("Please enter a number: "))
        if number == 0:
            self.selection_list(account)
        for product in self.products:
            if product.product_id == number:
                print("Name: " + str(product.name) + "\t\t\tId: " + str(product.product_id) + "\t\t\tPrice: " +
                      str(product.price) + "\t\t\tAmount: " + str(product.amount))
                print("\nComments for this product....\n")
                for comment in product.comments:
                    print(comment + "\t\t\t")
                print("""


******* Selection List *******
Enter 1 to add this product to your cart
Enter 0 to quit
           
""")
                number = int(input("Please enter a number: "))
                if number == 1:
                    product.amount = product.amount - 1
                    account.add_to_cart(product)
                    product.add_comment(str(input("Please type your comment for buying this product: ")))
                    print("Done....")
                    self.selection_list(account)
                elif number == 0:
                    self.show_products(account)

