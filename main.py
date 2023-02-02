from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

off = False
while not off:
	response = input(f"What would you like? ({menu.get_items()}): ")

	if response == "off":
            off = True
	elif response == "report":
		coffee_maker.report()
		money_machine.report()
	else:
		drink = menu.find_drink(response)

		if coffee_maker.is_resource_sufficient(drink):
			if money_machine.make_payment(drink.cost):
				coffee_maker.make_coffee(drink)
			else:
				print("Sorry that's not enough money. Money refunded.")

		else:
			print("Sorry there is not enough water")
