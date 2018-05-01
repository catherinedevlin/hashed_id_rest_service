import hashlib
import os

try:
    salt = os.environ['MIRO_ID_SALT']
except KeyError:
    msg = 'Provide an arbitrary, consistent, private string as environment variable MIRO_ID_SALT'
    raise KeyError(msg)


def hash(unhashed):
    '''Returns an MD5 hash of `unhashed`, salted with the MIRO_ID_SALT environment variable'''

    hashable = (unhashed + salt).encode('utf8')
    result = hashlib.md5(hashable)
    return result.hexdigest()
