class CoffeeMachine:
    def __init__(self, water: int, milk: int, coffee_beans: int, money:float) -> None:
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.money = money

    brew_types = {
        "Espresso":{"cost":1.00,
                    "water_needed":50, "milk_needed":0, "coffee_beans_needed":100},
        "Latte Macchiato":{"cost":3.50,"water_needed":100, "milk_needed":200, "coffee_beans_needed":70},
        "Capuccino":{"cost":3.25,"water_needed":150, "milk_needed":150, "coffee_beans_needed":120},
        "Black Coffee":{"cost":1.50, "water_needed":300, "milk_needed":0, "coffee_beans_needed":200},
        "Tea":{"cost":1.00,"water_needed":300, "milk_needed":100, "coffee_beans_needed":0}
        }

    def get_report(self) -> None: 
        """Display a report showing he current resource levels and money."""
        print("Amount of water (mL): ", self.water)
        print("Amount of milk (mL): ", self.milk)
        print("Amount of coffee beans (g): ", self.coffee_beans)
        print("Amount of money ($): ", self.money)
    
    def turn_off(self):
        print(f"Returning money: {self.money}")
        print("Shutting down...")
        self.money = 0
        return True

    def check_resources(self, water_needed, milk_needed, beans_needed):
        if self.water < water_needed or self.milk < milk_needed or self.coffee_beans < beans_needed:
            print("Not enough resources! Call Support!")
            return False
        else:
            return True

    def make_coffee(self, coffee_type, cost, water_needed, milk_needed):
        print(f"Making {coffee_type}...")
        self.water -= water_needed
        self.milk -= milk_needed
        self.money -= cost

        pass

    def insert_coins(self):
        # accepted = []
        try:
            self.money += float(input("Insert Coins"))
        except:
            ValueError
            print("Something went wrong")
    
    # def check_transaction(self, cost):
        
    #     pass

    def give_change(self,cost):
        change = self.money - cost
        print("Your change: ", change)
        self.money = 0

    # def serve_coffee(self, coffee_type):
    #     pass

    def refill(self):
        self.water = 1000
        self.milk = 1000
        self.coffee_beans = 1000
        print("Refilled")
    
    def check_resource_alert(self):
        if self.water < 200 or self.milk < 200 or self.coffee_beans < 200:
            print("Resources running low!")
        refill = input("Can you refill the machine? (y/n) ")
        if refill == "y":
            refill()

    







def coffee_machine_init():
    coffee_machine = CoffeeMachine(1000,1000,1000,0)
    quit = False
    
    while quit == False:
        brew = None
        # Getting user input: make coffee or check resources
        print("Options: brew coffee | show resources")
        option = input("What do you want to do?: ")
        if option == "brew coffee":
             
            while brew == None:
                coffee = input("Espresso | Latte Macchiato | Capuccino | Black Coffee | Tea\n")
                if coffee in coffee_machine.brew_types:
                    brew = coffee
                else:
                    print("Trying to guess what you mean...")
        elif option == "show resources":
            coffee_machine.get_report()
        else: 
            "Trying to guess what you want to do..."

        
        if brew:
            # Checking resources for brew
            resources_needed = coffee_machine.brew_types[brew]
            water_needed = resources_needed["water_needed"]
            milk_needed = resources_needed["milk_needed"]
            coffee_beans_needed = resources_needed["coffee_beans_needed"]
            cost = resources_needed["cost"]
            enough_resources = coffee_machine.check_resources(water_needed, milk_needed, coffee_beans_needed)
            
            # getting money
            if enough_resources:
                print(f"{brew} costs {resources_needed['cost']}")
                while resources_needed['cost'] > coffee_machine.money:
                    coffee_machine.insert_coins()
                    abort = input("Abort? (y/n)")
                    if abort == "y":
                        cost = 0
                        coffee_machine.give_change(cost)
                        break
                coffee_machine.make_coffee(brew, cost, water_needed, milk_needed)
                coffee_machine.give_change(cost)
            else:
                print("Not enough resources...")




        
        quitting = input("Turn off coffee machine? (y/n) ")
        if quitting == "y":
            coffee_machine.turn_off()
            quit = True

coffee_machine_init()