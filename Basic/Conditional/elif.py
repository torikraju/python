blockchain = []


def add_value(transaction_amount, last_transaction):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def get_transaction_value():
    return float(input("your transaction amount please "))


def get_user_choise():
    return (input("Your choise "))


def print_blockchain_element():
    for idx, element in enumerate(blockchain):
        print('Outputting Block')
        print(element)
        print(idx)
    else:
        print('-'*20)


def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        if block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


wating_for_input = True


def print_message():
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')


while wating_for_input:
    print_message()
    user_choise = get_user_choise()

    if user_choise == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choise == '2':
        print_blockchain_element()
    elif user_choise == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choise == 'q':
        wating_for_input = False
    else:
        print('Input was indvalid, please pick a vlaue from the list')

    if not verify_chain():
        print('Invalid blockchain')
        print_blockchain_element()
        break
else:
    print('User left')


print('Done')
