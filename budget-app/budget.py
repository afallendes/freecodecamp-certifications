from __future__ import annotations

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []


    def deposit(self, amount:int, description:str = "") -> None:
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount:int, description:str = "") -> bool:
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False
    
    def get_balance(self) -> float:
        return sum([ _["amount"] for _ in self.ledger ]) or 0.0

    def transfer(self, amount:int, category:Category) -> bool:
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False
    
    def check_funds(self, amount:int) -> bool:
        return False if amount > self.get_balance() else True
    
    def __str__(self):
        # Title
        middle = len(self.name) // 2
        s = self.name[:middle].rjust(15, '*') + \
            self.name[middle:].ljust(15, '*') + '\n'
        # Ledger registries
        for _ in self.ledger:
            s += _['description'][:23].ljust(23) + \
                str("%.2f"%_['amount']).rjust(7) + '\n'
        # Total
        s += 'Total: ' + "%.2f"%self.get_balance()
        return s

    def __repr__(self):
        return f'Category: {self.name}'

def create_spend_chart(categories:list):
    # Obtain expenditures (only withdrawels)
    expenditures = []
    for category in categories:
        expenditures.append(
            abs(sum([ _['amount'] for _ in category.ledger if _['amount'] < 0 ]))
        )

    # Calculate percentages per category
    percentages = []
    for expenditure in expenditures:
        percentage = expenditure / sum(expenditures) if sum(expenditures) > 0 else 0
        # Round floor to nearest multiple of 10
        percentage = round_to_nearest_by(percentage * 100, 10, 'floor')
        percentages.append(percentage)

    # Construct histogram

    # Add title
    s = 'Percentage spent by category\n'

    # Add axis and values
    for i in range(100, -10, -10):
        s += str(i).rjust(3) + '|'
        s += ''.join([' o ' if _ >= i else '   ' for _ in percentages]) + ' \n'

    # Add separator line
    s += '    ' + '---' * len(categories) + '-\n'

    # Add labels
    names = [ _.name for _ in categories ]
    max_len_name =  max([ len(name) for name in names ]) 

    for i in range(max_len_name):
        s += '    '
        for name in names:
            try:
                s += f' {name[i]} '
            except IndexError:
                s += '   '
            else:
                pass
        if i < max_len_name - 1:
            s += ' \n'
        else:
            s += ' '
    
    return s

def round_to_nearest_by(n:float, x:int=1, round_mode:str='auto') -> int:
    """ Rounds n to nearest number by value of x.
        n:float = Number to round.
        x:int   = Multiple to round by.
        Optional round_mode can be 'auto', 'floor', 'ceil'.
    """
    v = n / x

    if round_mode == 'auto':
        return int(v) * x if v - int(v) < 0.5 else (int(v) + 1) * x
    elif round_mode == 'floor':
        return int(v) * x
    elif round_mode == 'ceil':
        return (int(v) + 1) * x
    else:
        raise ValueError('Invalid round_mode value')
