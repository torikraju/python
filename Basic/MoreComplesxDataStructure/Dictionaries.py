genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transaction = []
owner = 'torik'


def add_transaction(recipient, sender=owner, amount=1.0):
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transaction.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = '-'.join([str(last_block[key]) for key in last_block])
    print(hashed_block)

    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transaction
    }
    blockchain.append(block)


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def get_transaction_value():
    tx_recipient = input('Enter the recipient of the transaction ')
    tx_amount = float(input('Enter the amount of the transaction '))
    return (tx_recipient, tx_amount)


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
    print('1: Add a new transaction')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')


while wating_for_input:
    print_message()
    user_choise = get_user_choise()

    if user_choise == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transaction)
    elif user_choise == '2':
        mine_block()
    elif user_choise == '3':
        print_blockchain_element()
    elif user_choise == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choise == 'q':
        wating_for_input = False
    else:
        print('Input was indvalid, please pick a vlaue from the list')

    # if not verify_chain():
    #     print('Invalid blockchain')
    #     print_blockchain_element()
    #     break

else:
    print('User left')


print('Done')
