#corrected
class MenuItem:
    def __init__(self,name,water,milk,coffee,cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water":water,
            "milk":milk,
            "coffee":coffee
        }
class Menu:
    def __init__(self):
        self.m_i_obj = [
            MenuItem(name="latte",water=200,milk=150,coffee=24,cost=2.5),
            MenuItem(name="espresso",water=150,milk=100,coffee=19,cost=2.0),
            MenuItem(name="sunrise",water=90,milk=130,coffee=17,cost=1.9),
        ]
    def get_item(self):
        options = ""
        for item in self.m_i_obj:
            options+=f"{item.name}/"
        return options
    def find_drink(self,order_name):
        for item in self.m_i_obj:
            if item.name==order_name:
                return item   
                #MenuItem(name="latte",water=200,milk=150,coffee=24,cost=2.5),
        return None



