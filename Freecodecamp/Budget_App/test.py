ledger = []
ledger.append('10 Initial deposit')
ledger.append('450 ')
ledger.append('-10.15 groceries')
ledger.append('-15.89 restaurant and more food for dessert')
print(ledger)


for item in ledger:
    splitted = item.split(" ", 1)
    line = splitted[1][:23] + " " * (30 - (len(str(splitted[1][:23])) + len(str(splitted[0]))))  +splitted[0]
    print(line)