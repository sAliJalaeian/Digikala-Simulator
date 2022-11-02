from Account import Account
from Digikala import Digikala
from Product import Product

accounts = []
products = []

user1 = Account("abolix", "98143001", "Abolfazl")
user2 = Account("ali20", "981434", "Ali Reza")
user3 = Account("mmd", "mmd", "mohamad")
user4 = Account("taghii", "123456", "taghi")
user5 = Account("rezaii", "124aa", "Reza")
user6 = Account("mostafa20", "987654a", "mostafa")
user7 = Account("eh20", "eh123", "ehsana")
user8 = Account("maryam.b", "208020", "maryam")
user9 = Account("zahra.z", "z1234", "zahra")
user10 = Account("azar.-.kh", "298137", "azar")

accounts.append(user1)
accounts.append(user2)
accounts.append(user3)
accounts.append(user4)
accounts.append(user5)
accounts.append(user6)
accounts.append(user7)
accounts.append(user8)
accounts.append(user9)
accounts.append(user10)

comments1 = []
comments2 = []
comments3 = []
comments4 = []
comments5 = []
comments6 = []
comments7 = []
comments8 = []
comments9 = []
comments10 = []

comments1.append("Nice")
comments1.append("Good")
comments2.append("Nice")
comments2.append("Good")
comments2.append("very good")
comments3.append("Nice")
comments3.append("Good")
comments3.append("bad")
comments4.append("Nice")
comments5.append("Nice")
comments5.append("Good")
comments5.append("don like")
comments5.append("best")
comments6.append("best")
comments6.append("Good")
comments7.append("Nice")
comments7.append("Good")
comments8.append("Nice")
comments8.append("best")
comments9.append("ok")
comments9.append("Good")
comments10.append("Nice")
comments10.append("bad")

product1 = Product(981420, 120000, 12, "Hard ssd", comments1)
product2 = Product(981421, 15520, 100, "Usb", comments2)
product3 = Product(981422, 13000000, 20, "lap top", comments3)
product4 = Product(981423, 1400000, 10, "monitor", comments4)
product5 = Product(981424, 100000, 26, "LED", comments5)
product6 = Product(981425, 6000, 13, "pen", comments6)
product7 = Product(981426, 200000, 102, "shirt", comments7)
product8 = Product(981427, 50000000, 41, "iphone 13 pro", comments8)
product9 = Product(981428, 30000000, 30, "iphone 12 pro", comments9)
product10 = Product(981429, 1320000, 60, "samsung a71s", comments10)

products.append(product1)
products.append(product2)
products.append(product3)
products.append(product4)
products.append(product5)
products.append(product6)
products.append(product7)
products.append(product8)
products.append(product9)
products.append(product10)

digikala = Digikala(accounts, products)
digikala.main()
