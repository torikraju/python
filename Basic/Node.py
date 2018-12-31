from AppUitl import print_message, get_user_choice
from Blockchain import Blockchain
from Utility.Verification import Verification


class Node:

    def __init__(self):
        # self.id = str(uuid4())
        self.id = 'torik'
        self.blockchain = Blockchain(self.id)

    def get_transaction_value(self):
        """ Returns the input of the user (a new transaction amount) as a float. """
        tx_recipient = input('Enter the recipient of the transaction ')
        tx_amount = float(input('Enter the amount of the transaction '))
        return tx_recipient, tx_amount

    def print_blockchain_element(self):
        """ Output all blocks of the blockchain. """
        for element in self.blockchain.chain:
            print('Outputting Block')
            print(element)
        else:
            print('-' * 20)

    def listen_for_input(self):
        while True:
            print_message()
            user_choice = get_user_choice()

            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                print('Added transaction') if self.blockchain.add_transaction(recipient, self.id,
                                                                              amt=amount) else print(
                    'Transacting failed')
                print('Open_Transactions: ', self.blockchain.get_open_transactions())
            elif user_choice == '2':
                self.blockchain.mine_block()
            elif user_choice == '3':
                self.print_blockchain_element()
            elif user_choice == '4':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(),
                                                    self.blockchain.get_balance):
                    print('all transactions are valid')
                else:
                    print('There are invalid transactions')
            elif user_choice == 'q':
                break
            else:
                print('Input was invalid, please pick a value from the list')
            if not Verification.verify_chain(self.blockchain.chain):
                self.print_blockchain_element()
                print('Invalid blockchain')
                break

            print('Balance of {} : {:.2f} '.format(self.id, self.blockchain.get_balance()))

        print('Done')


node = Node()
node.listen_for_input()
