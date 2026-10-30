class Account:
    def __init__(self, ac_num, name):
        self.ac_num = ac_num
        self.name = name
        self.balance = 0

    def ac_detail(self):
        return print(f"{self.ac_num}, {self.name}, {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            return print("Invalid amount")
        if amount > self.balance:
           return print("Insufficient balance")
        self.balance -= amount

punit_account = Account(2281514479, "Punit Tiwari")
punit_account.ac_detail()
punit_account.deposit(500)
punit_account.ac_detail()
punit_account.withdraw(700)
punit_account.ac_detail()