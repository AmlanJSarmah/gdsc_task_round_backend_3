from random import getrandbits


def get_random_id():
    return str(getrandbits(28))
