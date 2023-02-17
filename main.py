import hashlib
import json
import os


def get_hash(filename):
    blockchain_dir = os.curdir + '/blockchain/'
    file = open(blockchain_dir + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()

def check_integrity():
    blockchain_dir = os.curdir + '/blockchain/'
    files = os.listdir(blockchain_dir)
    files = sorted([int(i) for i in files])

    for file in files[1:]:
        f = open(blockchain_dir + str(file))
        h = json.load(f)['hash']

        prev_file = str(file - 1)
        actual_hash = get_hash(prev_file)

        if h == actual_hash:
            res = 'OK!'
        else:
            res = 'Corrupted'

        print('block {} is: {}'.format(prev_file, res))
 
def create_block(user, amoutCoin, transactionTo, hash=''):
    blockchain_dir = os.curdir + '/blockchain/'
    files = os.listdir(blockchain_dir)
    files = sorted([int(i) for i in files])

    last_file = files[-1]
    filename = str(last_file + 1)

    hash = get_hash(str(last_file))

    data = {'user': user,
            'amoutCoin': amoutCoin,
            'transactionTo': transactionTo,
            'hash': hash}

    with open(blockchain_dir + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def main():
    create_block(user='Alexsey', amoutCoin=10, transactionTo='Andrey')

if __name__ == '__main__':
    main()