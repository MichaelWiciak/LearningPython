def ext_vigenere(text, key, option):
    rangeOfValues = [characterCode for characterCode in (chr(i) for i in range(32,127))]

    amountOfValues = len(rangeOfValues)

    if not(text):
        return "Invalid option!"
    if not(key):
        return "Invalid option!"
    if option not in ('decrypt', 'encrypt'):
        return "Invalid option!"
    if any(t not in rangeOfValues for t in key):
        return "Invalid option!"

    output = ''
    LengthKey = len(key)

    for i, l in enumerate(text):
        if l not in rangeOfValues:
            output += l
        else:
            textIndex = rangeOfValues.index(l)

            k = key[i % LengthKey]
            keyIndex = rangeOfValues.index(k)
            if option == 'decrypt':
                keyIndex *= -1

            code = rangeOfValues[(textIndex + keyIndex) % amountOfValues]

            output += code

    return output



