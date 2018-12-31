import functools
import json
from collections import OrderedDict

from HashUtil import hash_block, hash_string_256
from AppUitl import print_message, get_user_choice, genesis_block
from Block import Block
from Transaction import Transaction

MINING_REWARD = 10
blockchain = []
open_transactions = []
owner = 'torik'
participants = {'torik'}


def load_data():
    global blockchain
    global open_transactions
    try:
        with open('blockchain.txt', mode='r') as f:
            # file_content = pickle.loads(f.read())
            file_content = f.readlines()
            # blockchain = file_content['chain']
            # open_transactions = file_content['ot']
            # [:-1] is used for escaping the last line the \n
            blockchain = json.loads(file_content[0][:-1])
            updated_blockchain = []
            for block in blockchain:
                converted_tx = [Transaction(tx['sender'], tx['recipient'], tx['amount']) for tx in
                                block['transactions']]
                updated_block = Block(block['index'], block['previous_hash'], converted_tx, block['proof'],
                                      block['timestamp'])
                updated_blockchain.append(updated_block)
            blockchain = updated_blockchain
            open_transactions = json.loads(file_content[1])
            updated_transactions = []
            for tx in open_transactions:
                updated_transaction = Transaction(tx['sender'], tx['recipient'], tx['amount'])
                updated_transactions.append(updated_transaction)
            open_transactions = updated_transactions
    except (IOError, IndexError):
        blockchain = [genesis_block]
        open_transactions = []
    finally:
        print('Cleanup!')


load_data()


def save_data():
    global blockchain
    global open_transactions
    try:
        with open('blockchain.txt', mode='w') as f:
            savable_chain = [block.__dict__ for block in
                             [Block(block_el.index, block_el.previous_hash,
                                    [tx.__dict__ for tx in block_el.transactions], block_el.proof, block_el.timestamp)
                              for block_el in blockchain]]
            f.write(json.dumps(savable_chain))
            f.write('\n')
            savable_tx = [tx.__dict__ for tx in open_transactions]
            f.write(json.dumps(savable_tx))
            # save_data = {
            #     'chain': blockchain,
            #     'ot':open_transactions
            # }
            # f.write(pickle.dumps(save_data))
    except IOError:
        print('Saving failed!')
    finally:
        print('Cleanup!')


def get_balance(participant):
    tx_sender = [[tx.amount for tx in block.transactions if tx.sender == participant] for block in blockchain]
    open_tx_sender = [tx.amount for tx in open_transactions if tx.sender == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = functools.reduce(
        lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)

    tx_recipient = [[tx.amount for tx in block.transactions if tx.recipient == participant] for block in blockchain]
    amount_receive = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0,
                                      tx_recipient,
                                      0)
    return amount_receive - amount_sent


def verify_transaction(transaction):
    sender_balance = get_balance(transaction.sender)
    return sender_balance >= transaction.amount


def add_transaction(receiver, sender=owner, amt=1.0):
    transaction = Transaction(sender, receiver, amt)
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        save_data()
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = Transaction('MINING', owner, MINING_REWARD)
    copied_transaction = open_transactions[:]
    copied_transaction.append(reward_transaction)
    proof = proof_of_work()
    block = Block(len(blockchain), hashed_block, copied_transaction, proof)
    blockchain.append(block)
    save_data()
    return True


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def get_transaction_value():
    tx_recipient = input('Enter the recipient of the transaction ')
    tx_amount = float(input('Enter the amount of the transaction '))
    return tx_recipient, tx_amount


def print_blockchain_element():
    for element in enumerate(blockchain):
        print('Outputting Block')
        print(element)
        print('-' * 20)
    else:
        print('-' * 20)


def valid_proof(transactions, last_hash, proof):
    guess = (str(tx.to_order_dict() for tx in transactions) + str(last_hash) + str(proof)).encode()
    guess_hash = hash_string_256(guess)
    return guess_hash[0:2] == '00'


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof


def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block.previous_hash != hash_block(blockchain[index - 1]):
            return False
        if not valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
            print("Proof of work is invalid")
            return False

    return True


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


while True:
    print_message()
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        print('Added transaction') if add_transaction(
            recipient, amt=amount) else print('Transacting failed')
        print('Open_Transactions: ', open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
            save_data()
    elif user_choice == '3':
        print_blockchain_element()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if verify_transactions():
            print('all transactions are valid')
        else:
            print('There are invalid transactions')
    elif user_choice == 'q':
        break
    else:
        print('Input was indvalid, please pick a value from the list')

    if not verify_chain():
        print('Invalid blockchain')
        print_blockchain_element()
        break

    print('Balance of {} : {:.2f} '.format(owner, get_balance('torik')))

print('Done')
