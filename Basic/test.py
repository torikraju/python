test = 'global'


def setTest(test):
    globals()['test'] = test


setTest('setting from global')
print(test)


for b in range(0, 10, 2):
    print(b)
