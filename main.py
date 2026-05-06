

# 23-m
class Product:
    def __init__(self, price, stock):
        self._price = price
        self._stock = stock

    def buy(self, n):
        self._stock -= n

    def discount(self, x):
        self._price -= x

    def info(self):
        print(f"Stock:{self._stock}")
        print(f"Price:{self._price}")


pr1 = Product(100, 10)

pr1.buy(1)
pr1.info()

pr1.discount(10)
pr1.info()


# 24-m
class SecureAccount:
    def __init__(self, password):
        self.__password = password

    def login(self, pw):
        print(pw == self.__password)

    def change_password(self, old, new):
        if old == self.__password:
            self.__password = new
            print("Password updated")


a1 = SecureAccount("1234")

a1.login("1234")
a1.change_password("1234", "5678")

