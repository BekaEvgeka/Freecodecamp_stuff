import re
import operator
class Category:

            
    def __init__(self, nam):

        self.name = nam
        # print(self.name, "added")
        self.ledger = list()
        self.balance = 0
        self.withdrawed_amount = 0
    

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
            self.withdrawed_amount += amount
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
            self.withdrawed_amount += amount    
            whereto.deposit(amount, ("Transfer from " + str(self.name)))
            amount = amount * (-1) 
            withdrawed = {"amount": round(amount, 2), "description": ("Transfer to " + str(whereto.name))}
            self.ledger.append(withdrawed)     
            return True
        else:
            return False
    
    def __str__(self) -> str:
        firstline = '{:*^30}'.format(str(self.name)) + "\n"
        ben = ""
        for item in self.ledger:
           ben = ben + (str(item["description"][:23]) + (" " * (30 - len("{:.2f}".format((item["amount"]))) - len(str(item["description"][:23]))) +  "{:.2f}".format((item["amount"])))) + "\n" 
           
        total = "Total: " + str(self.balance)
        to_print = firstline + ben + total
        return to_print
    

def create_spend_chart(list):  
    percents = []
    totalspent = 0
    deviderline = "    "
    firstline = "Percentage spent by category"
    print(firstline)
    for item in list:
        totalspent += item.withdrawed_amount
    for item in list:
        percentspent = 0
        percentspent = round(round((item.withdrawed_amount / totalspent), 2) * 100, -1)
        percents.append({"Category" : item.name, "Amount" : percentspent})
    
    for i in range (0, 11):
        number = str(100 - (i*10))
        line = " " * (3 - (len(number))) +  number + "|"
        for item in percents:            
            if item["Amount"] >= int(number):
                line = line + " o "
                
        print (line)
    amounttoadd = ([m.start() for m in re.finditer('o', line)])
    deviderline = deviderline + ("---" * len(amounttoadd))
    print(deviderline)
    maxlen = 0
    percents.sort(key=operator.itemgetter('Amount'), reverse=True)
    for item in percents:
        if len(item["Category"]) > maxlen:
            maxlen = len(item["Category"])
        else:
            pass

    for i in range(0, maxlen + 1):
        line = "     "
        for item in percents:
            try:
                line = line + item["Category"][i] + "  "
            except:
                line = line + "   "
        print(line)



    