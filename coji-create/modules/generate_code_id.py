import hashlib
import time

HASH_LEN = 128
MAX_RETRIES = 6
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
db = []  # temporary!


def generate_code_id(code_len=16, retries=0):
    """Generate random coji code id"""
    hashed = hashlib.sha512(
        str(time.time()).encode('utf-8')).hexdigest()  # get random hash (current time is used as seed)

    digits = []
    for i in range(HASH_LEN):
        cur_value = hashed[i]
        if cur_value in alphabet:  # convert chars to int
            cur_value = str(alphabet.index(cur_value))
        digits.append(cur_value)

    chunk_len = int(HASH_LEN / code_len)
    id = []
    for i in range(0, HASH_LEN, chunk_len):  # group digits in to string of 8 numbers (16 * 8 = 128)
        letter_i = int(''.join(digits[i:i + chunk_len])) % code_len  # decrese to 0 - 16
        id.append(alphabet[letter_i])

    # add!
    # if id in db:  # if code already exists
    #     if retries < MAX_RETRIES:
    #         return generate_code_id(code_len, retries + 1)
    #     else:
    #         return None
    return ''.join(id)
