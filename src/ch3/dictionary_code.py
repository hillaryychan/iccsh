def find_prefix_entry(message, dictionary):
    """
    Find the longest entry in dictionary which is a prefix of the given message
    """
    for entry in dictionary[::-1]:
        if message.startswith(entry[0]):
            return dictionary.index(entry)
    return -1


def lz78_encode(message, *args, **kwargs):
    dictionary = []
    while len(message) > 0:
        prefix_entry = find_prefix_entry(message, dictionary)
        if prefix_entry == -1:
            next_char = message[0]
            entry = (next_char, (0, next_char))
            message = message[1:]
        else:
            prefix = dictionary[prefix_entry][0]
            next_char = message[len(prefix)]
            value = prefix + next_char
            entry = (value, (prefix_entry + 1, next_char))
            message = message[len(value) :]
        dictionary.append(entry)
    return dictionary


def lz78_decode(outputs, *args, **kwargs):
    dictionary = []
    message = ""
    for i, c in outputs:
        if i == 0:
            suffix = c
            dictionary.append((c, (i, c)))
        else:
            entry = dictionary[i - 1]
            suffix = entry[0] + c
            dictionary.append((entry[0] + c, (i, c)))
        message += suffix
    return message
