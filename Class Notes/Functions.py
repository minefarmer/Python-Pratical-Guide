# blockchain = []

# def add_value():
#     blockchain.append(5.3)
#     print(blockchain)
    
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



blockchain = [[1]]

def add_value(transaction_amount):
    blockchain.append([blockchain[-1], transaction_amount])
    print(blockchain)
    
add_value(2)  # [[1], [[1], 2]]
add_value(0.9)  # [[1], [[1], 2], [[[1], 2], 0.9]]
add_value(10.89)  # [[1], [[1], 2], [[[1], 2], 0.9], [[[[1], 2], 0.9], 10.89]]