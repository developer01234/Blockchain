import json
import os


def create_block(user, amoutCoin, transactionTo, hash=''):
    blockchain_dir = os.curdir + '/blockchain/'
    files = sorted(os.listdir(blockchain_dir))

    data = {"user": user,
            "amoutCoin": amoutCoin,
            "transactionTo": transactionTo,
            "hash": hash}

    with open(blockchain_dir + '2', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def main():
    create_block(user='Alexsey', amoutCoin=10, transactionTo='Andrey')

if __name__ == '__main__':
    main()