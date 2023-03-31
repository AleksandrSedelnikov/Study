# функция кодирования сообщения с помощью ключа
def chifr_encode(string, key):
    encode_string = ""
    j = 0
    for i in range(len(string)):
        if (j < len(key)):
            string_buff = chr(ord(string[i]) ^ ord(key[j]))
            encode_string += string_buff
            j += 1
        else:
            j = 0
            string_buff = chr(ord(string[i]) ^ ord(key[j]))
            encode_string += string_buff
            j += 1
    return encode_string


# функция декодирования сообщения с помощью ключа
def chifr_decode(encode, key):
    decode_string = ""
    j = 0
    for i in range(len(encode)):
        if (j < len(key)):
            string_buff = chr(ord(encode[i]) ^ ord(key[j]))
            decode_string += string_buff
            j += 1
        else:
            j = 0
            string_buff = chr(ord(encode[i]) ^ ord(key[j]))
            decode_string += string_buff
            j += 1
    return decode_string


def main():
    string = input('Введите предложение: ')
    key = input('Введите ключ: ')
    encode = chifr_encode(string, key)
    print("Закондированное сообщение: {}".format(encode))
    decode = chifr_decode(encode, key)
    print("Декодированное сообщение: {}".format(decode))

if __name__ == "__main__":
    main()