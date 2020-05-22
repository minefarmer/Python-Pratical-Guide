
# #  Streamlined version
# blockchain = []

# def get_last_blockchain_value():
#     return blockchain[-1]
    
# def add_value(transaction_amount, last_transaction=[1]):
#     blockchain.append([last_transaction, transaction_amount])
    
# def get_user_input():
#     return float(input('Your transaction amount please: '))
#     return user_input


# tx_amount = get_user_input() 
# add_value(tx_amount)

# while True:
#     tx_amount = get_user_input()
#     add_value(tx_amount, get_last_blockchain_value())

# #  Output the blockchain list to the console
#     for block in blockchain:
#         print('Outputting Block')
#         print(block)

# print('Done!')
#             # Your transaction amount please: 10
#             # Your transaction amount please: 5.3
#             # Outputting Block
#             # [[1], 10.0]
#             # Outputting Block
#             # [[[1], 10.0], 5.3]
#             # Your transaction amount please:



# #  Streamlined version
# blockchain = []

# def get_last_blockchain_value():
#     return blockchain[-1]
    
# def add_value(transaction_amount, last_transaction=[1]):
#     blockchain.append([last_transaction, transaction_amount])
    
# def get_user_input():
#     return float(input('Your transaction amount please: '))
#     return user_input


# tx_amount = get_user_input() 
# add_value(tx_amount)

# while True:
#     tx_amount = get_user_input()
#     add_value(tx_amount, get_last_blockchain_value())

# #  Output the blockchain list to the console
#     for block in blockchain:
#         print('Outputting Block')
#         print(block)

# print('Done!')
#             # Your transaction amount please: 10
#             # Your transaction amount please: 5.3
#             # Outputting Block
#             # [[1], 10.0]
#             # Outputting Block
#             # [[[1], 10.0], 5.3]
#             # Your transaction amount please:
            
            
            

#  Streamlined version  ^^^ added to
blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]
    
def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])
    
def get_user_input():
    return float(input('Your transaction amount please: '))
    return user_input


tx_amount = get_user_input() 
add_value(tx_amount)

while True:
    tx_amount = get_user_input()
    add_value(tx_amount, get_last_blockchain_value())

#  Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)

print('Done!')
            # Your transaction amount please: 10
            # Your transaction amount please: 5.3
            # Outputting Block
            # [[1], 10.0]
            # Outputting Block
            # [[[1], 10.0], 5.3]
            # Your transaction amount please: