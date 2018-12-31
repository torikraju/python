from Block import Block

genesis_block = Block(0, '', [], 100, 0)


def print_message():
    print('Please choose')
    print('1: Add a new transaction')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Check transaction validity')
    print('5: Create wallet')
    print('6: Load wallet')
    print('7: Save keys')
    print('q: Quit')


def get_user_choice():
    return input("Your chaise ")
