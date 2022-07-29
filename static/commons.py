def valid_request_keys(keys_in, keys):
    """Check if request has all necessary keys"""
    return set(keys_in.keys()).issubset(keys)
