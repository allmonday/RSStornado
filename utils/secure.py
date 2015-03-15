from itsdangerous import Signer

s = Signer('tangkikodo')

def _hash(pw):
    return s.sign(pw).split('.')[-1]
