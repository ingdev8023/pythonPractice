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

    total_spend = 0
    final_list= []
    
    for category in categories:
        category_spend = 0
        for transaction in category.ledger:
            if transaction['amount'] < 0:
                category_spend -= transaction['amount']
        final_list.append({'category': category.name,'category_spend': category_spend})
        total_spend += category_spend 

    for category in final_list:
        percentage_cal = (((category['category_spend'] / total_spend * 100)) // 10) * 10
        category['percentage'] = percentage_cal
        
    #final_chart = f'Percentage spent by category\n'

    chart_lines = ["Percentage spent by category"]
    
    for i in range(100, -1, -10):
        percentage_line = f'{i:>3}| '

        for category in final_list:
            if category['percentage'] >= i:
                percentage_line += 'o  '
            else:
                percentage_line += "   " 
    #final_chart += percentage_line + '\n'
        chart_lines.append(percentage_line)

    #eje x
    """ eje_x = ''
    eje_x += f'{'':<4}{"--" * len(final_list)}--\n'
    categories_names = []
    for category in final_list:
            
        categories_names.append(category['category'])
        # 1. Find the length of the longest word
        max_len = max(len(w) for w in categories_names)
        # 2. Pad each word with spaces so they all have the same length
        padded_words = [w.ljust(max_len) for w in categories_names]
        # 3. Combine them row by row using a space as a separator
        lines = []
        for i in range(max_len):
            row = " ".join(word[i] for word in padded_words)
            lines.append(row)
        # 4. Join all rows with a newline
        result =  f'{'':<5}{"\n".join(lines)}'

    eje_x += result

    final_chart += eje_x        

    print(final_chart)                 

    pass """

    horizontal_line = "    " + "---" * len(final_list) + "-"
    chart_lines.append(horizontal_line)


    category_names = [category['category'] for category in final_list]

    longest_name = max(len(name) for name in category_names)

    for character_index in range(longest_name):
        name_line = "     "

        for name in category_names:
            if character_index < len(name):
                name_line += name[character_index] + "  "
            else:
                name_line += "   "

        chart_lines.append(name_line)

    return "\n".join(chart_lines)







test = Category('Food')
test_2 = Category('Auto')
test_3 = Category('Clothing')
test_4 = Category('Rent')

test.deposit(1000, 'initial deposit')
test_2.deposit(1000, 'initial deposit')
test_3.deposit(1000, 'initial deposit')
test_4.deposit(1000, 'initial deposit')
test.withdraw(200.50, 'restaurant')
test.withdraw(250, 'restaurant')
test.withdraw(300, 'restaurant')
test_2.withdraw(200, 'wheels')
test_2.withdraw(300, 'paint')
test_3.withdraw(300, 'shirt')
test_3.withdraw(200, 'Tshirt')
test_4.withdraw(1000, 'rent')


create_spend_chart([test,test_2,test_3, test_4])

