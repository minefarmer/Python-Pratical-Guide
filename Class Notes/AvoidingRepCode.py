# Start of lesson
blockchain = [1]

def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])

tx_amount = float(input('Your transaction amount please: '))
add_value(tx_amount)

tx_amount = float(input('Your transaction amount please: '))
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=0.9)

tx_amount = float(input('Your transaction amount please: '))
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)




# Initializing our (empty) blockchain list 
blockchain = [1]

def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])
    
    
def get_user_input():
    return float(input('Your transaction amount please: '))

tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)