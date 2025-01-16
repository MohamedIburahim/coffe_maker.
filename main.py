from coffeeMenu import Menu
from coffeemaker import CoffeeMaker
from moneymachine import VendingMachine

#instance creation
menu = Menu()
coffeemaker = CoffeeMaker()
vendingmachine = VendingMachine()

#report printting


#loop
is_on = True

while is_on:
    print()
    options = menu.get_item()
    choice = input(f"What would you like?({options}): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(coffeemaker.report())
        print(vendingmachine.report())
    else:
        drink = menu.find_drink(choice)
        # drink = MenuItem(name="latte",water=200,milk=150,coffee=24,cost=2.5),
        if drink is None:
            print(f"{drink} not available")
        else:
             is_resource_sufficient = coffeemaker.is_resource_sufficient(drink)
             if is_resource_sufficient and vendingmachine.make_payment(drink.cost): 
                      print(coffeemaker.make_coffee(drink))
                 


