from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
money = MoneyMachine()
menu = Menu()
latte = MenuItem("latte",200,150,24,2.5)
espresso = MenuItem("espresso",50,0,18,1.5)
cappuccino = MenuItem("cappuccino",250,50,24,3)


choice = ""
while choice!="off":
    choice = input("What do you want?: ")
    if choice == "report":
        machine.report()
    if choice == "espresso":
       if machine.is_resource_sufficient(espresso):
           machine.make_coffee(espresso)
           money.make_payment(espresso.cost)
    elif choice == "latte":
        if machine.is_resource_sufficient(latte):
            machine.make_coffee(latte)
            money.make_payment(latte.cost)
    elif choice == "cappuccino":
        if machine.is_resource_sufficient(cappuccino):
            machine.make_coffee(cappuccino)
            money.make_payment(cappuccino.cost)