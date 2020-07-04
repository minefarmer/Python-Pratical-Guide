# Initializing our (empty) blockchain list
blockchain = [1]


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain."""
    return blockchain[-1]

# this function accepts two arguments.
# One required one (transaction_amount) and one optional one(last_transaction)
# the optional one is optional because it has a default value +> [1]
def add_value(transaction_amount, last_transaction=[1]):
    """ Appendd a new value as well as the last blockchain value to the blockchain.
    
    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The amount that should be added.
    """
    blockchain.append([last_transaction, transaction_amount])
    
    
def get_user_input():
    """ Returns the input of the user (a new transaction amount) as a floor."""
    # get the user input, transform it from a string to a float and store it.
    user_input = float(input('Your transaction ampunt please: '))
    return user_input




# Get the first transaction input and add the value to the blockchain
tx_amount = get_user_input()
add_value(tx_amount)

while True:
    tx_amount = get_user_input()
    add_value(tx_amount, get_last_blockchain_value())

    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)
    
print('Done!')












