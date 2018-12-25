MINING_REWARD = 10

genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transaction = []
owner = 'torik'
participants = {'torik'}


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in
                    blockchain]
    amount_receive = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_receive += tx[0]

    return amount_receive - amount_sent


def add_transaction(recipient, sender=owner, amount=1.0):
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transaction.append(transaction)
    participants.add(sender)
    participants.add(recipient)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {'sender': 'MINING', 'recipient': owner, 'amount': MINING_REWARD}
    open_transaction.append(reward_transaction)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transaction
    }
    blockchain.append(block)
    return True


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def get_transaction_value():
    tx_recipient = input('Enter the recipient of the transaction ')
    tx_amount = float(input('Enter the amount of the transaction '))
    return tx_recipient, tx_amount


def get_user_choice():
    return input("Your chaise ")


def print_blockchain_element():
    for idx, element in enumerate(blockchain):
        print('Outputting Block')
        print(element)
        print(idx)
    else:
        print('-' * 20)


def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


def print_message():
    print('Please choose')
    print('1: Add a new transaction')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output participants')
    print('h: Manipulate the chain')
    print('q: Quit')


while True:
    print_message()
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transaction)
    elif user_choice == '2':
        if mine_block():
            open_transaction = []
    elif user_choice == '3':
        print_blockchain_element()
    elif user_choice == '4':
        print(participants)
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'shariar', 'recipient': 'rohit', 'amount': 85.0}]
            }
    elif user_choice == 'q':
        break
    else:
        print('Input was indvalid, please pick a value from the list')

    if not verify_chain():
        print('Invalid blockchain')
        print_blockchain_element()
        break



print('Done')
