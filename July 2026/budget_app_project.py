class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount:int, description=""):
        deposit_details = {
            'amount': amount,
            'description': description
        }
        self.ledger.append(deposit_details)
        

    def withdraw(self, amount:int, description=""):
        
        if self.check_funds(amount):
            withdraw_details = {
                        'amount': amount * -1,
                        'description': description
                        }
            self.ledger.append(withdraw_details)
            return True
        
        return False
    
    def get_balance(self):
        balance = 0.00
        for transaction in self.ledger:
            balance += transaction['amount']
        return balance
    
    def transfer(self, amount:int, receiver):

        if self.check_funds(amount):
            transfer_details_sender = {
                'amount': amount * -1,
                'description': "Transfer to " + receiver.name
            }
            transfer_details_receiver = {
                'amount': amount,
                'description': "Transfer from " + self.name
            }
            self.ledger.append(transfer_details_sender)
            receiver.ledger.append(transfer_details_receiver)

            
            return True
        
        return False
    
    def __str__(self):
        output = f"{self.name:*^30}\n"

        for entry in self.ledger:
            description = entry["description"][:23]
            amount = entry["amount"]

            output += f"{description:<23}{amount:>7.2f}\n"

        output += f"Total: {self.get_balance():.2f}"

        return output

    def check_funds(self, amount:int):
        if amount > self.get_balance():
            return False
        return True

    
        
def create_spend_chart(categories):
    print('Percentage spent by category')
        

    pass

test = Category('Food')
test_2 = Category('test_2')

test.deposit(100, 'initial deposit')
test.deposit(200, 'second deposit')
test.deposit(300, 'third deposit')
test.withdraw(200.50, 'restaurant')

test.get_balance()

test_2.deposit(100)

test.transfer(300, test_2)
test_2.get_balance()

print(test)

