### Data ###
recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###
class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient in ingredients:
            if self.machine_resources[ingredient] < ingredients[ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        dollars = int(input("how many large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))

        total = (
            dollars * 1.00 +
            half_dollars * 0.50 +
            quarters * 0.25 +
            nickels * 0.05
        )
        return total
    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        change = round(coins - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")


### Make an instance of SandwichMachine class and write the rest of the codes ###
krustyKrab = SandwichMachine(resources) # I like Spongebob :)

is_running = True
while is_running:
    optionNoLowercase = input("What would you like? (small/ medium/ large/ off/ report): ")
    selection = optionNoLowercase.lower()

    if selection in recipes:
        recipe = recipes[selection]
        required_ingredients = recipe["ingredients"]
        sandwich_price = recipe["cost"]

        if krustyKrab.check_resources(required_ingredients):
            total_inserted = krustyKrab.process_coins()
            if krustyKrab.transaction_result(total_inserted, sandwich_price):
                krustyKrab.make_sandwich(selection, required_ingredients)
    elif selection == "report":
        for resource_name, amount in krustyKrab.machine_resources.items():
            label = "slice(s)" if resource_name in ["bread", "ham"] else "ounce(s)"
            print(f"{resource_name.capitalize()}: {amount} {label}")

    elif selection == "off":
        is_running = False

    else:
        print("Invalid option. Please choose small, medium, large, off, or report.")


# Sorry for submitting late!