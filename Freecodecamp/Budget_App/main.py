from budget import *
food = Category("food")
food.deposit(10, "Initial deposit")
food.deposit(450)
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
auto = Category("auto")
# food.transfer(10, auto)
auto.deposit(1000, "deposit for new car")
auto.withdraw(1500, "First payment")
auto.transfer(150, food)
# print(food)
# print(auto)
food.transfer(300, auto)

entertainment = Category("entertainment")
entertainment.deposit(5000, "Initial deposit")
entertainment.withdraw(455, "Amusement park")

create_spend_chart([food, auto, entertainment])