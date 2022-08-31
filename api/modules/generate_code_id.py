symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
n = m = 4  # dimension of key - n*n
num_keys = (2 ** m) ** (n * n)  # total number of keys
p = 6364136223846793005
s = 1442695040888963407

db = []  # temporary!


# add! support for different code_len

def generate_code_id(index, code_len=16, retries=0):
    """Generate random coji code id"""
    sh_idx = (index * p + s) % num_keys  # map to pseudo-random target
    values = [(sh_idx >> (i * m)) & ((1 << m) - 1)
              for i in range(n * n)]  # split into m-bit words
    id = ''.join([symbols[i] for i in values])
    # add!
    # if id in db:  # if code already exists
    #     if retries < MAX_RETRIES:
    #         return generate_code_id(code_len, retries + 1)
    #     else:
    #         return None
    return id
