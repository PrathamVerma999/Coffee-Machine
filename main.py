import os
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

money = 0


def main():
    global money
    while True:

        coffee = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
        if coffee == "off":
            exit()

        if coffee == "report":
            print(f"Water:{resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}gm")
            print(f"Money: ${money}")
            main()

        try:
            resource_sufficiency, resource = sufficient_resources(coffee)

            if resource_sufficiency:
                print("Please insert coins.")
                try:
                    quarters = float(input("How many quarters?: "))
                    dimes = float(input("How many dimes?: "))
                    nickles = float(input("How many nickles?: "))
                    pennies = float(input("How many pennies?: "))
                except ValueError:
                    print("You need to enter a number!")
                    main()
                price_sufficiency, change = price_check(coffee, quarters, dimes, nickles, pennies)
                if price_sufficiency:
                    print(f"Here is ${change:.2f} dollars in change.")
                    money += MENU[coffee]["cost"]
                    if coffee == 'espresso':
                        resources['water'] = resources['water'] - MENU[coffee]['ingredients']['water']
                        resources['coffee'] = resources['coffee'] - MENU[coffee]['ingredients']['coffee']
                    elif coffee == 'latte' or coffee == 'cappuccino':
                        resources['milk'] = resources['milk'] - MENU[coffee]['ingredients']['milk']
                        resources['water'] = resources['water'] - MENU[coffee]['ingredients']['water']
                        resources['coffee'] = resources['coffee'] - MENU[coffee]['ingredients']['coffee']
                    print(f"Here is your {coffee}. Enjoy!")
                    os.system('clear')
                    main()
                else:
                    print("Sorry that's not enough money. Money refunded.")
                    main()
            else:
                print(f"Sorry there is not enough {resource}.")
                main()
        except KeyError:
            print("Please choose a coffee from the given options")
            main()


def sufficient_resources(drink):
    resources_req = MENU[drink]['ingredients']
    final = True
    lacking = None

    for resource in resources_req:
        if resources_req[resource] > resources[resource]:
            final = False
            lacking = resource
    return final, lacking


def price_check(drink, quarters, dimes, nickles, pennies):
    quarter_val = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    final = True
    change = 0

    if quarter_val < MENU[drink]["cost"]:
        final = False
    else:
        change = quarter_val - MENU[drink]["cost"]

    return final, change


main()
