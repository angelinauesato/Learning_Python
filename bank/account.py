class Account:
    # Only special account will need to send the limit as parameter. Default: 1000
    def __init__(self, number, owner, balance, limit=1000.00):
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    @staticmethod
    def bank_code():
        return '001'

    @staticmethod
    def banks_codes():
        return {'BMO':'001','Scotiabank':'002','RBC':'003'}

    @property
    def balance(self):
        return self.__balance

    @property
    def limit(self):
        return self.__limit

    @property
    def owner(self):
        return self.__owner

    @property
    def number(self):
        return self.__number

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    def statment(self):
        print(f"Owner: {self.__owner}\nBalance: {self.__balance}")

    def deposit(self, amount):
        self.__balance += amount

    def __allow_widrawal(self, amount_to_withdrawal):
        amount_available = self.__balance + self.__limit
        return amount_to_withdrawal <= amount_available

    def withdrawal(self, amount):
        if self.__allow_widrawal(amount):
            self.__balance -= amount
        else:
            print(f"The amount {amount} is bigger than your limit.")

    def transfer(self, amount, destination):
        self.withdrawal(amount)
        destination.deposit(amount)
