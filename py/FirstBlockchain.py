# Initializing our (empty) blockchain list
blockchain = [1]
open_transactions = []
owner = 'Carl'


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain."""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]


def add_transaction(sender, recipient, amount=1.0):
    """ Appendd a new value as well as the last blockchain value to the blockchain.
    
    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The amount that should be added.
        :amount: The amount of coins sent with the transaction (defauls = 1.0)
    """
transaction = {
    'sender': sender,
    'recipient': recipient,
    'amount': amount
}
open_transactions.append(transaction)


def mine_block():
    pass
        
        
def get_transaction_value():
    """  Returns the input of the user (a new transaction amount) as floatdatetime A combination of a date and a time."""
    # Get the user input, transform it from a string to a float and store it.
    tx_recipient = input('Enter the sender of the transaction:')
    tx_amount = float(input('Your transaction amount please: '))
    return (tx_recipent, tx_amount)


def get_user_choice():
    """ Prompts the user for its choice and returns it. """   
    user_input = input('Your choice: ')
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
