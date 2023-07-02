MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resource_check(w, m, c, cost):
    if w <= resources["water"]:
        if m <= resources["milk"]:
            if c <= resources["coffee"]:
                if payment(cost):
                    resources["water"] = resources.get("water") - w
                    resources["milk"] = resources.get("milk") - m
                    resources["coffee"] = resources.get("coffee") - c
            else:
                print("Not enough coffee")
        else:
            print("Not enough milk")
    else:
        print("Not enough water")


def payment(cost):
    coins = {
        "1p": 0.01,
        "2p": 0.02,
        "5p": 0.05,
        "10p": 0.10,
        "20p": 0.20,
        "50p": 0.50,
        "£1": 1.00,
        "£2": 2.00,
    }
    total = 0
    for coin in coins:
        user = int(input(f"How many {coin}'s: "))
        total = (user * coins.get(coin)) + total

    if total < cost:
        print("not enough money")
        return False
    else:
        change = total - cost
        print(f"Here is your change: £{change}")

    return True


choice = ""
while choice != "off":
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        for item, value in resources.items():
            print(item, value)
    elif choice == "off":
        break
    elif choice == "espresso":
        resource_check(MENU["espresso"]["ingredients"]["water"],0,
                       MENU["espresso"]["ingredients"]["coffee"], MENU["espresso"]["cost"])
    elif choice == "latte":
        resource_check(MENU["latte"]["ingredients"]["water"], MENU["latte"]["ingredients"]["milk"],
                       MENU["latte"]["ingredients"]["coffee"], MENU["latte"]["cost"])
    elif choice == "cappuccino":
        resource_check(MENU["cappuccino"]["ingredients"]["water"], MENU["cappuccino"]["ingredients"]["milk"],
                       MENU["cappuccino"]["ingredients"]["coffee"], MENU["cappuccino"]["cost"])
    else:
        print("error")
print("OFF")