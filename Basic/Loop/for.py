blockchain = []


def add_value(transaction_amount='default value', last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


def get_last_blockchain_value():
    return blockchain[-1]


def get_user_input():
    return float(input("your transaction amount please "))


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(),
          transaction_amount=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())


for element in blockchain:
    print('Outputting Block')
    print(element)

print('Done')
