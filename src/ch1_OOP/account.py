class Account:
    def __init__(self, ac_num, name):
        self.ac_num = ac_num
        self.name = name
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def ac_detail(self):
        return print(f"a/c num: {self.ac_num}, name: {self.name}, balance: {self._balance}")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            return print("Invalid amount")
        if amount > self._balance:
           return print("Insufficient balance")
        self._balance -= amount

    def transfer(self, account, transferred_amount):
        if transferred_amount <= 0:
            return print("Invalid amount")
        if transferred_amount > self._balance:
            return print("Insufficient balance")
        account._balance += transferred_amount
        self._balance -= transferred_amount
        

punit_account = Account(2281514479, "Punit Tiwari")
punit_account.ac_detail()
punit_account.deposit(500)
print(punit_account.balance)
punit_account.balance = 4000
