# Initializing our (empty) blockchain list
blockchain = [1]


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain."""
    return blockchain[-1]

# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]
def add_value(transaction_amount, last_transaction=[1]):
    """ Appendd a new value as well as the last blockchain value to the blockchain.
    
    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The amount that should be added.
    """
    blockchain.append([last_transaction, transaction_amount])
    

def get_user_input():
    """ Returns the input of the user (a new transaction amount) as a floor."""
    # Get the user input, transform it from a string to a float and store it.
    user_input = float(input('Your transaction amount please: '))
    return user_input




#  Get first transaction input and add the value to the blockchain.
tx_amount = get_user_input()
add_value(tx_amount)

while True:
    tx_amount = get_user_input()
    add_value(tx_amount, get_last_blockchain_value())

    # Output for the blockchain list in the console
    for block in blockchain:
        print('Outputting block')
        print(block)
    
print('Done!')
