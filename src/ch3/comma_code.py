from src.exceptions import IccshValueError


def check_comma_message_symbols(length, message):
    gt_length = list(filter(lambda s: int(s) > (length + 1), message))
    if gt_length:
        raise IccshValueError(
            (
                "Message contains symbols which can't be "
                f"encoded by a comma code of length {length}"
            )
        )


def generate_comma_code(length):
    code = []
    for i in range(length + 1):
        if i == 0:
            code.append("0")
        elif i == length:
            code.append("1" * i)
        else:
            code.append("1" * i + "0")
    return code


def comma_encode(length, message, *args, **kwargs):
    message = list(filter(lambda s: s, message.split("s")))
    check_comma_message_symbols(length, message)
    code = generate_comma_code(length)
    encoded = ""
    for s in message:
        index = int(s) - 1
        encoded += code[index]
    return encoded


def find_comma_prefix(message, code):
    for c in code[::-1]:
        if message.startswith(c):
            return code.index(c)
    return -1


def comma_decode(length, message, *args, **kwargs):
    code = generate_comma_code(length)
    decoded = ""
    while len(message) > 0:
        prefix = find_comma_prefix(message, code)
        message = message[len(code[prefix]) :]
        decoded += f"s{prefix+1}"
    return decoded
