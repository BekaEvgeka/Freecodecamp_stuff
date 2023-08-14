ledger = [{"amount": 10, "description": "Initial deposit"}, {"amount": 450, "description": ""}, {"amount": -10.15, "description": "groceries"}, {"amount": -15.89, "description": "restaurant and more food for dessert"}, {"amount": 150, "description": "Transfer from auto"}]

testledger = {"amount": 900,    "description": "deposit"}



# for item in ledger:
#     splitted = item.split(" ", 1)
#     line = splitted[1][:23] + " " * (30 - (len(str(splitted[1][:23])) + len(str(splitted[0]))))  +splitted[0]
#     print(line)
ben = ""
for item in ledger:
    ben = ben + (str(item["description"][:23]) + (" " * (30 - len(str(item["amount"])) - len(str(item["description"][:23]))) +  str(item["amount"]))) + "\n"    

print(ben)