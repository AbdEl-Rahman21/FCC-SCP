class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def get_balance(self):
        return sum(entry['amount'] for entry in self.ledger)

    def check_funds(self, amount):
        return False if self.get_balance() < amount else True

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount): return False
        
        self.ledger.append({'amount': -amount, 'description': description})

        return True

    def transfer(self, amount, category):
        if not self.check_funds(amount): return False

        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self.name}')

        return True

    def __str__(self):
        menu = ''
        line_length = 30 - len(self.name)

        for _ in range(0, line_length):
            menu += '*'

            if len(menu) == line_length / 2: menu += self.name

        menu += '\n'

        for entry in self.ledger:
            menu += entry['description'][:23]

            line_length = 30 - len(entry['description'][:23]) - len(str(int(entry['amount']))) - 3

            for _ in range(0, line_length): menu += ' '

            menu += f"{entry['amount']:.2f}\n"

        menu += f'Total: {self.get_balance()}'

        return menu

def create_spend_chart(categories):
    chart = 'Percentage spent by category\n'
    total_spent_per = []

    for category in categories:
        total_spent_per.append(sum(entry['amount'] if entry['amount'] < 0 else 0 for entry in category.ledger))

    total_spent = sum(total_spent_per)

    percentages = [category / total_spent * 100 for category in total_spent_per]

    for y in range(100, -10, -10):
        if y == 100:
            chart += f'{y}| '
        elif y == 0:
            chart += f'  {y}| '
        else:
            chart += f' {y}| '

        for percent in percentages:
            chart += 'o  ' if percent >= y else '   '

        chart += '\n'

    chart += '    -'

    for _ in range(len(categories)): chart += '---'

    chart += '\n'

    index = 0
    name_print = True

    while(name_print):
        name_print = False
        chart += '     '

        for category in categories:
            try:
                chart += f'{category.name[index]}  '

                name_print = True
            except IndexError:
                chart += f'   '

        chart += '\n'

        index += 1

    return '\n'.join(chart.split('\n')[:-2])

food = Category('Food')
clothing = Category('Clothing')

food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
food.transfer(50, clothing)

print(food)
print(create_spend_chart([food, clothing]))
