class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water":300,
            "milk": 200,
            "coffee": 100
        }
    def report(self):
        return (f"Current Level of Water:{self.resources['water']} ml"
                f"\nCurrent Level of Milk:{self.resources['milk']} ml"
                f"\nCurrent Level of coffee:{self.resources['coffee']} g")
    def is_resource_sufficient(self,drink):
        #drink variable hold latte object
        #test the resources
        for item in self.resources:#'water'
            if self.resources[item]<drink.ingredients[item]:
                # MenuItem(name="latte",water=200,milk=150,coffee=24,cost=2.5).ingridents['water']
                print(f"Sorry, not enough {item}.")
                return False
        return True
    def make_coffee(self,drink:object):
        #deduct resources after checking 
        for item in drink.ingredients:
            self.resources[item]-=drink.ingredients[item]
        return f"Here is your {drink.name} ☕.Enjoy"
        
#Latte_coffee
class Latte:
    def __init__(self):
        #name and ingredients
        self.name = "latte"
        self.ingridents = {'water':200,'milk':150,'coffee':24}

#espresso coffee
class Espresso:
    def __init__(self):
        #name and ingredients
        self.name = "Espresso"
        self.ingridents = {'water':50,'milk':0,'coffee':18}
#CoffeeMachineSystem
class CoffeeMachineSystem:
    def __init__(self,drinks:list):
        self.c_m_obj = CoffeeMaker()
        self.drink_list = drinks
    
    def add_drink(self,drink):#latte
        self.drink_list.append(drink)
    
    def process_order(self,drink_name):#latte
        #find the drink object by name
        for drink in self.drink_list:
            if drink.name.lower() == drink_name.lower():
                if self.c_m_obj.is_resource_sufficient(drink):
                    return self.c_m_obj.make_coffee(drink)
        return f"Sorry, we don't have {drink_name} on the menu"











