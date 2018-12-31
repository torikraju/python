from Block import Block

genesis_block = Block(0, '', [], 100, 0)


def print_message():
    print('Please choose')
    print('1: Add a new transaction')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output participants')
    print('5: Check transaction validity')
    print('q: Quit')


def get_user_choice():
    return input("Your chaise ")
