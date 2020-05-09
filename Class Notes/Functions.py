#  Return keyword -- line 62
#  Can return values -- line 88
#  Default Argumunts -- line 98
#  Key words  -- line 123
#  Input Function -- line 117
#  Streamlined version  -- line 203






# blockchain = []

# def add_value():
#     blockchain.append(5.3)
#     print(blockchain    
# add_value()  # [5.3]
# add_value()  # [5.3, 5.3]
# add_value()  # [5.3, 5.3, 5.3]



# blockchain = [1]

# def add_value():
#     blockchain.append([blockchain[0], 5.3])
#     print(blockchain)
    
# add_value()  # [1, [1, 5.3]]
# add_value()  # [1, [1, 5.3], [1, 5.3]]
# add_value()  # [1, [1, 5.3], [1, 5.3], [1, 5.3]]



# blockchain = [1]

# def add_value():
#     blockchain.append([blockchain[-1], 5.3])
#     print(blockchain)
    
# add_value()  # [1, [1, 5.3]]
# add_value()  # [1, [1, 5.3], [[1, 5.3], 5.3]]
# add_value()  # [1, [1, 5.3], [[1, 5.3], 5.3], [[[1, 5.3], 5.3], 5.3]]



# blockchain = [[1]]

# def add_value(transaction_amount):
#     blockchain.append([blockchain[-1], transaction_amount])
#     print(blockchain)
    
# add_value(2)  # [[1], [[1], 2]]
# add_value(0.9)  # [[1], [[1], 2], [[[1], 2], 0.9]]
# add_value(10.89)  # [[1], [[1], 2], [[[1], 2], 0.9], [[[[1], 2], 0.9], 10.89]]




# RETURN KEY WORD  ********************************************************************************

# def sum(a, b):
#     return a + b

# print(sum(2, 5))  # 7



# blockchain = [[1]]

# def get_last_blockchain_value():
#     return blockchain[-1]
    
# def add_value(transaction_amount):
#     blockchain.append([get_last_blockchain_value(), transaction_amount])
    
# add_value(2)
# add_value(0.9)
# add_value(10.89)

# print(blockchain)  # [[1], [[1], 2], [[[1], 2], 0.9], [[[[1], 2], 0.9], 10.89]]




# # Return values************************************************************************************

# def sum(a, b):
#     return a + b

# print(sum(2, 5))  # 7




# Default argemunts ****************************************************************************

# def greet(name, age=81):
#     print('Hello ' + name + ', I am ' + age)
    
# greet('Rich')


# blockchain = []

# def get_last_blockchain_value():
#     return blockchain[-1]
    
# def add_value(transaction_amount, last_transaction=[1]):
#     blockchain.append([last_transaction, transaction_amount])
    
# add_value(2)
# add_value(0.9, get_last_blockchain_value())
# add_value(10.89, get_last_blockchain_value())

# print(blockchain)  # [[[1], 2], [[[1], 2], 0.9], [[[[1], 2], 0.9], 10.89]]




#  Keywords ************************************************************************************

# def greet(name, age):
#     print('Hello ' + name + ', I am ' + age)
    
# greet(age=81, name='Carl')

# blockchain = []

# def get_last_blockchain_value():
#     return blockchain[-1]
    
# def add_value(transaction_amount, last_transaction=[1]):
#     blockchain.append([last_transaction, transaction_amount])
    
# add_value(2)
# add_value(last_transaction=get_last_blockchain_value(), transaction_amount=0.9)
# add_value(10.89, get_last_blockchain_value())

# print(blockchain)  # [[[1], 2], [[[1], 2], 0.9], [[[[1], 2], 0.9], 10.89]]




#  Input Function

# blockchain = []

# def get_last_blockchain_value():
#     return blockchain[-1]
    
# def add_value(transaction_amount, last_transaction=[1]):
#     blockchain.append([last_transaction, transaction_amount])

# tx_amount = input('Your transaction amount please: ')
# add_value(tx_amount)
# add_value(last_transaction=get_last_blockchain_value(), transaction_amount=0.9)
# add_value(10.89, get_last_blockchain_value())

# print(blockchain)  # [[[1], '5.99'], [[[1], '5.99'], 0.9], [[[[1], '5.99'], 0.9], 10.89]]

#  Float  ** sees as a number = this removes the "" arount 5.99  ******************************************************

# blockchain = []

# def get_last_blockchain_value():
#     return blockchain[-1]
    
# def add_value(transaction_amount, last_transaction=[1]):
#     blockchain.append([last_transaction, transaction_amount])

# tx_amount = float(input('Your transaction amount please: '))
# add_value(tx_amount)
# add_value(last_transaction=get_last_blockchain_value(), transaction_amount=0.9)
# add_value(10.89, get_last_blockchain_value())

# print(blockchain)  # [[[1], 5.99], [[[1], '5.99'], 0.9], [[[[1], '5.99'], 0.9], 10.89]]


# blockchain = []

# def get_last_blockchain_value():
#     return blockchain[-1]
    
# def add_value(transaction_amount, last_transaction=[1]):
#     blockchain.append([last_transaction, transaction_amount])

# tx_amount = float(input('Your transaction amount please: '))  # 100
# add_value(tx_amount)

# tx_amount = float(input('Your transaction amount please: '))  # 99.9
# add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

# tx_amount = float(input('Your transaction amount please: '))  # 4.8
# add_value(tx_amount, get_last_blockchain_value())

# print(blockchain)  # [[[1], 100.0], [[[1], 100.0], 99.9], [[[[1], 100.0], 99.9], 4.8]]



#  Streamlined version
# blockchain = []

# def get_last_blockchain_value():
#     return blockchain[-1]
    
# def add_value(transaction_amount, last_transaction=[1]):
#     blockchain.append([last_transaction, transaction_amount])
    
# def get_user_input():
#     return float(input('Your transaction amount please: '))

# tx_amount = get_user_input()  # 99.9
# add_value(tx_amount)

# tx_amount = get_user_input()  # 12.4
# add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

# tx_amount = get_user_input()  # 7.2
# add_value(tx_amount, get_last_blockchain_value())

# print(blockchain)  # [[[1], 99.9], [[[1], 99.9], 12.4], [[[[1], 99.9], 12.4], 7.2]]


