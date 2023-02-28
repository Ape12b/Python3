from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino/):”
# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
# TODO 3. Print report.
# TODO 4. Check resources sufficient?
# TODO 5. Process coins.
# TODO 6. Check transaction successful?
# TODO 7. Make Coffee.

curr_menu = Menu()
office_coffee_maker = CoffeeMaker()
office_money = MoneyMachine()

choice = input(f"What would you like? ({curr_menu.get_items()}): ").lower()

while not choice == "off":
    if choice == "report":
        office_coffee_maker.report()
        office_money.report()
    else:
        chosen_item = curr_menu.find_drink(choice)
        if chosen_item is not None:
            office_money.money_received = 0
            if office_coffee_maker.is_resource_sufficient(chosen_item):
                if office_money.make_payment(chosen_item.cost):
                    office_coffee_maker.make_coffee(chosen_item)

    choice = input(f"What would you like? ({curr_menu.get_items()}): ").lower()
