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
        self.balance += round(float(amount), 2)
        self.balance = round(self.balance, 2)
        deposited = {"amount": round(float(amount), 2) , "description": str(description)}
        self.ledger.append(deposited)
        # print(self.ledger)
        
        # print(str(self.balance))
        
    def withdraw(self, amount, description = ""):

        if Category.check_funds(self, amount):
            self.balance -= round(float(amount), 2)
            self.balance = round(self.balance, 2)
            amount = float("-" + str(amount))
            withdrawed = {"amount": round((amount), 2), "description": str(description)}
            self.ledger.append(withdrawed)
            # print(self.ledger)
            
            return True
        else:
            return False
    
    def get_balance(self):
        self.balance = round(self.balance, 2)
        return self.balance
    

    def transfer(self, amount, whereto):
        if Category.check_funds(self, amount):
            self.balance -= round(float(amount), 2)
            self.balance = round(self.balance, 2)            
            whereto.deposit(amount, ("Transfer from " + str(self.name)))
            amount = amount * (-1) 
            withdrawed = {"amount": round(amount,2), "description": ("Transfer to " + str(whereto.name))}
            self.ledger.append(withdrawed)     
            return True
        else:
            return False
    
    def __str__(self) -> str:
        firstline = '{:*^30}'.format(str(self.name)) + "\n"
        ben = ""
        for item in self.ledger:
           ben = ben + (str(item["description"][:23]) + (" " * (30 - len(str(item["amount"])) - len(str(item["description"][:23]))) +  str(item["amount"]))) + "\n" 
           
        total = "Total: " + str(self.balance)
        to_print = firstline + ben + total
        return to_print