blockchain = []


def add_value(transaction_amount='default value', last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


def get_last_blockchain_value():
    return blockchain[-1]


def get_transaction_value():
    return float(input("your transaction amount please "))


def get_user_choise():
    return (input("Your choise "))


def print_blockchain_element():
    for element in blockchain:
        print('Outputting Block')
        print(element)


tx_amount = get_transaction_value()
add_value(tx_amount)

while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    user_choise = get_user_choise()

    if user_choise == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    else:
        print('dfsfd')
        print_blockchain_element()

print('Done')
