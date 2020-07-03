# Initializing our (empty) blockchain list
blockchain = [1]

def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction):
    blockchain.append([last_transaction, transaction_amount])


add_value(2, get_last_blockchain_value())
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=0.9)
add_value(10.89, get_last_blockchain_value())

print(blockchain)