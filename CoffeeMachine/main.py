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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def update_report(coffee):
    for values in MENU[coffee]['ingredients']:
        resources[values] -= MENU[coffee]['ingredients'][values]  # removes the values of resources rto make the coffee


def check_resources(coffee):
    """returns true when resources are enough , false otherwise ! """
    for values in MENU[coffee]['ingredients']:
        if MENU[coffee]['ingredients'][values] > resources[values]:
            print(f"Sorry there is not enough {values}.")
            return False
    return True


def process_coins():
    """returns the total calculated from coins inserted. !"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def check_transaction(money, coffee):
    """ it will return false if not enough coins to make the transaction """
    inserted_money = money
    if inserted_money < MENU[coffee]['cost']:  # inserted less than the actual cost
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:  # the money inserted are enough

        global profit
        profit += MENU[coffee]['cost']
        change = round(inserted_money - MENU[coffee]['cost'], 2)  # the change
        print(f"Here is {change} of change.")
        return True


def make_coffee(coffee ):
    """ It make the changes to the resources for making the coffe """
    update_report(coffee)
    print(f"Here is your {coffee}.")

is_on = True
while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == 'off':
        is_on = False
        break
    if user_input == "report":
        for values in resources:
            print(values, ' : ', resources[values])
        print('profit : ', profit.__round__(2))
    else:
        if check_resources(user_input):
            payment = process_coins()
            if check_transaction(payment, user_input):  # needs 2 arguments
                make_coffee(user_input)