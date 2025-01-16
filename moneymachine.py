#corrected
class VendingMachine:
    currency = "$"#class level Attribute
    def __init__(self):
        self.coin_values={
            "quarters": 0.25, 
            "dimes": 0.10, 
            "nickels": 0.05,
            "pennies": 0.01
        }
        self._profit = 0
        self.money_received = 0
    def report(self):
        """print the current profit"""
        return f"Money: {self._profit}{self.currency}"
    def get_profit(self):
        return f"Current profit:{self._profit}"
    def process_coins(self):
        add_value = 0
        print("Please insert coins:  ")
        for coin in self.coin_values:#'Quarters'
            coin_count = int(input(f'How many {coin}?:  '))
            add_value+=coin_count*self.coin_values[coin]
        return add_value            
    def make_payment(self,cost):#2.0
        self.money_received = self.process_coins()#user cash
        #cost-->price of item
        if self.money_received>=cost:
            change_ = round(self.money_received-cost,2)#round changes to 2 decimel places
            self._profit+=cost
            print(f"Payment accepted.Here your change {change_}{self.currency}")
            self.money_received = 0
            return True
          
        else: 
            refund_cash = round(self.money_received,2)
            self.money_received = 0
            print(f"OOPS!,Insufficient cash!please take your {refund_cash}{self.currency} back")
            return False
          



