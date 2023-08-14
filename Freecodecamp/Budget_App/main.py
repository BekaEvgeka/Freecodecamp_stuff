import budget
import decimal
from budget import Category
food = Category("xdx")
food.deposit(10, "Initial deposit")
food.deposit(450)
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
auto = Category("auto")
# food.transfer(10, auto)
auto.deposit(1000, "deposit for food new car")
auto.withdraw(1500, "First payment")
auto.transfer(150, food)
print(str(food))