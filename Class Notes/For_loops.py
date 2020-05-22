#  For loop starts at 6
#  strreamlined version is missing *** modified streamed lined version in while loops



# # For loop  **********************************************
#  Streamlined version
# blockchain = []

# def get_last_blockchain_value():
#     return blockchain[-1]
    
# def add_value(transaction_amount, last_transaction=[1]):
#     blockchain.append([last_transaction, transaction_amount])
    
# def get_user_input():
#     return float(input('Your transaction amount please: '))

# tx_amount = get_user_input()  # 10
# add_value(tx_amount)

# tx_amount = get_user_input()  # 11
# add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

# tx_amount = get_user_input()  # 12
# add_value(tx_amount, get_last_blockchain_value())

# #  Output the blockchain list to the console
# for block in blockchain:
#     print('Outputting Block')
#     print(block)
#                     # Outputting Block
#                     # [[1], 10.0]
#                     # Outputting Block
#                     # [[[1], 10.0], 11.0]
#                     # Outputting Block
#                     # [[[[1], 10.0], 11.0], 12.0]
    
# print('Done!')  # Done



