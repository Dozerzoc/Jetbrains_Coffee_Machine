class CoffeeTypeRecipe:
    water: int = 0
    milk: int = 0
    beans: int = 0
    cost: int = 0

    def __init__(self, water: int, milk: int, beans: int, cost: int):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cost = cost

    def get_water(self):
        return self.water

    def get_milk(self):
        return self.milk

    def get_beans(self):
        return self.beans

    def get_cost(self):
        return self.cost


class CoffeeMachine:
    water: int = 0
    milk: int = 0
    beans: int = 0
    disposable_cups: int = 0
    money: int = 0

    def fill(self, water: int, milk: int, beans: int, disposable_cups: int, money: int):
        self.water += water
        self.milk += milk
        self.beans += beans
        self.disposable_cups += disposable_cups
        self.money += money

    def remaining(self):
        print(f'The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.disposable_cups} of disposable cups')
        print(f'${self.money} of money')

    def make_coffee(self, recipe):
        self.water -= recipe.get_water()
        self.milk -= recipe.get_milk()
        self.beans -= recipe.get_beans()
        self.disposable_cups -= 1
        self.money += recipe.get_cost()

    def take_money(self):
        took_money: int = self.money if self.money > 0 else 0
        self.money -= took_money
        return took_money

    def get_not_enough_resources(self, recipe):
        not_enough_resources = []
        if recipe.get_water() > self.water:
            not_enough_resources.append('water')
        if recipe.get_milk() > self.milk:
            not_enough_resources.append('milk')
        if recipe.get_beans() > self.beans:
            not_enough_resources.append('bean')
        return not_enough_resources


def start_state(machine):
    machine.fill(water=400, milk=540, beans=120, disposable_cups=9, money=550)


class MakeCoffee:

    @staticmethod
    def espresso() -> CoffeeTypeRecipe:
        return CoffeeTypeRecipe(water=250, milk=0, beans=16, cost=4)

    @staticmethod
    def latte() -> CoffeeTypeRecipe:
        return CoffeeTypeRecipe(water=350, milk=75, beans=20, cost=7)

    @staticmethod
    def cappuccino() -> CoffeeTypeRecipe:
        return CoffeeTypeRecipe(water=200, milk=100, beans=12, cost=6)


def action_buy(machine):
    make = MakeCoffee()
    coffee_type_storage = {
        '1': make.espresso(),
        '2': make.latte(),
        '3': make.cappuccino(),
        'back': None
    }
    coffee_type_id = input('What do you want to buy?'
                           ' 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    coffee_type = coffee_type_storage[coffee_type_id]
    if not coffee_type:
        return
    not_enough_resources = machine.get_not_enough_resources(coffee_type)
    if not_enough_resources:
        print('Sorry, not enough ' + ', '.join(not_enough_resources) + '!')
        return
    print('I have enough resources, making you a coffee!')
    machine.make_coffee(coffee_type)


def action_fill(machine):
    water = int(input(f'Write how many ml of water do you want to add:'))
    milk = int(input(f'Write how many ml of milk do you want to add:'))
    beans = int(input(f'Write how many grams of coffee beans do you want to add:'))
    cups = int(input(f'Write how many disposable cups of coffee do you want to add:'))
    machine.fill(water=water, milk=milk, beans=beans, disposable_cups=cups, money=0)


def action_take(machine):
    print(f'I gave you ${machine.take_money()}')


def main():
    machine = CoffeeMachine()
    start_state(machine)

    while True:
        action: str = input('Write action (buy, fill, take, remaining, exit):')
        if action == 'buy':
            action_buy(machine)
        elif action == 'fill':
            action_fill(machine)
        elif action == 'take':
            action_take(machine)
        elif action == 'remaining':
            machine.remaining()
        elif action == 'exit':
            break
        else:
            print('Unknown action')


main()
