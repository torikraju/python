import functools
import hashlib
import json
from collections import OrderedDict
import pickle

from Hash_uitl import hash_block, hash_string_256
from AppUitl import print_message, get_user_choice, genesis_block

MINING_REWARD = 10
blockchain = [genesis_block]
open_transactions = []
owner = 'torik'
participants = {'torik'}


def load_data():
    with open('blockchain.p', mode='rb') as f:
        file_content = pickle.loads(f.read())
        global blockchain
        global open_transactions
        blockchain = file_content['chain']
        open_transactions = file_content['ot']
        # # [:-1] is used for escaping the last line the \n
        # blockchain = json.loads(file_content[0][:-1])
        # updated_blockchain = []
        # for block in blockchain:
        #     updated_block = {
        #         'previous_hash': block['previous_hash'],
        #         'index': block['index'],
        #         'proof':  block['proof'],
        #         'transactions': [OrderedDict(
        #             [('sender', tx['sender']), ('recipient', tx['recipient']), ('amount', tx['amount'])]) for tx in block['transactions']]
        #     }
        #     updated_blockchain.append(updated_block)
        # blockchain = updated_blockchain
        # open_transactions = json.loads(file_content[1])
        # updated_transactions = []
        # for tx in open_transactions:
        #     updated_transaction=OrderedDict(
        #             [('sender', tx['sender']), ('recipient', tx['recipient']), ('amount', tx['amount'])])
        #     updated_transactions.append(updated_transaction)
        # open_transactions = updated_transactions


load_data()


def save_data():
    with open('blockchain.p', mode='wb') as f:
        # f.write(json.dumps(blockchain))
        # f.write('\n')
        # f.write(json.dumps(open_transactions))
        save_data = {
            'chain': blockchain,
            'ot':open_transactions
        }
        f.write(pickle.dumps(save_data))


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions']
                  if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount']
                      for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = functools.reduce(
        lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum+0, tx_sender, 0)

    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in
                    blockchain]
    amount_receive = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum+0, tx_recipient,
                                      0)
    return amount_receive - amount_sent


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def add_transaction(recipient, sender=owner, amount=1.0):
    transaction = OrderedDict(
        [('sender', sender), ('recipient', recipient), ('amount', amount)])

    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = OrderedDict(
        [('sender', 'MINING'), ('recipient', owner), ('amount', MINING_REWARD)])
    copied_transaction = open_transactions[:]
    copied_transaction.append(reward_transaction)
    proof = proof_of_work()
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': copied_transaction,
        'proof': proof
    }
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
    for  element in enumerate(blockchain):
        print('Outputting Block')
        print(element)
        print('-' * 20)
    else:
        print('-' * 20)


def valid_proof(transacitons, last_hash, proof):
    guess = (str(transacitons) + str(last_hash) + str(proof)).encode()
    guess_hash = hash_string_256(guess)
    print(guess_hash)
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
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
        if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
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
            recipient, amount=amount) else print('Transacting failed')
        print(open_transactions)
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
            print('all transaciton are valid')
        else:
            print('Ther are invalid transacitons')
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

    print('Balance of {} : {:.2f} '.format(owner, get_balance('torik')))

print('Done')
