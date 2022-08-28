import hashlib


def get_model_card_hash(params):
    return hashlib.sha256(
        ''.join(params.values()).encode()
    ).hexdigest()


def safety_wrapper(function):
    try:
        func = function
    except:
        func = ''
    return func
