# Initializing our (empty) blockchain list
genesis_block = {
        'previous_hash': '',
        'index': 0,
        'transactions': []
    }
blockchain = [genesis_block]
open_transactions = []
owner = 'Rich'


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]


def add_transaction(sender, recipient, amount):
    """ Append a new value as well as the last blockchain value to the blockchain.

    Arguments:
        :sender:  The sender of the coins
        :recipient: the recipient of the coins
        :amount: the amount of coins sent with the transaction (default = 1.0)
    """
    transaction = {
        'sender': sender, 
        'recipient': recipient, 
        'amount': amount
    }
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    last_block['']
    for keys in last_block:
        value = last_block[keys]
        hashed_block = hashed_block + str(value)
        
    print(hashed_block)
    block = {
        'previous_hash': 'XYZ',
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    #  get user input. transform it from a rtring to a float and store it,
    tx_recipient = input('Enter the recipient of the transaction:')
    tx_amount = float(input('Your transaction amount: '))
    return tx_recipient, tx_amount


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input



def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)
        

       
def verify_chain():
    """ Verify the current blockchain and return True if it's valid,False otherwise. """
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            #  If we're checking the first block, we should skip the iteration.
            continue
        # Check the privious block (the entire one) vs the first element of the block
        elif blockchain[block_index][0] == block[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
    #         break
    #         block_index += 1
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    return is_valid


waiting_for_input = True

#  a whike loop for the user input interface
# It,s a loop that exists once waiting_for_input becomes False or when break
while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        #  add the transaction amountnto the blockchain
        add_transaction(sender=sender, recipient=recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h':
        #  make sure that you don't try to "hack" the blockchain if it's empty
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print('Invalid blockchain!')
        break
else:
    print('User left!')
    

print('Done!')