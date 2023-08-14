from decimal import Decimal
class Category:

            
    def __init__(self, nam):

        self.name = nam
        # print(self.name, "added")
        self.ledger = list()
        self.balance = 0
    
    

    def check_funds(self, amount):
            if self.balance < amount:
                return False
            else:
                return True
            
    def deposit(self, amount, description = ""):

        deposited = str(amount) + " " + str(description)
        self.ledger.append(deposited)
        # print(self.ledger)
        self.balance += round(Decimal(amount), 2)
        # print(str(self.balance))
        
    def withdraw(self, amount, description = ""):

        if Category.check_funds(self, amount):
            withdrawed = "-" + str(amount) + " " + str(description)
            self.ledger.append(withdrawed)
            # print(self.ledger)
            self.balance -= round(Decimal(amount), 2)
            return True
        else:
            return False
    
    def get_balance(self):

        return (str(self.balance))

    def transfer(self, amount, whereto):
        if Category.check_funds(self, amount):
            withdrawed = "-" + str(amount) + " " + "Transfer to " + str(whereto.name)
            self.ledger.append(withdrawed)
            self.balance -= round(Decimal(amount), 2)
            whereto.deposit(amount, ("Transfer from " + str(self.name)))

            return True
        else:
            return False
    
    def __str__(self) -> str:
        firstline = '{:*^30}'.format(str(self.name)) + "\n"
        ben = ""
        counter = len(self.ledger)
        for item in self.ledger:
            splitted = item.split(" ", 1)
            counter -= 1
            ben = ben + splitted[1][:23] + " " * (30 - (len(str(splitted[1][:23])) + len(str(splitted[0]))))  +splitted[0] + "\n"
           
        total = "Total: " + str(self.balance)
        to_print = firstline + ben + total
        return to_print