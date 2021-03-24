import itertools


total_found = 0


def get_cipher(file_path):
    cipher = []
    with open(file_path) as file:
        cipher_raw = file.read().replace(',', " ")
        for word in cipher_raw.split():
            cipher.append(int(word))
    return cipher


def get_cipher_as_list(cipher):
    cipher_list = []
    a = cipher.replace(',', ' ')
    for num in a:
        cipher_list.append(num)
    return cipher_list


def convert_to_ascii(text):
    ascii_values = []
    for char in text:
        ascii_values.append(ord(char))
    return ascii_values


def make_cipher(plaintext, short_key):
    cipher = []
    for i, char in enumerate(plaintext):
        cipher.append(ord(char) ^ ord(short_key[i % 3]))
    return cipher


def is_maybe_english(text):
    num_chars = len(text)
    chars = [char for char in text]
    counts_dict = {}
    for char in chars:
        if char not in counts_dict:
            counts_dict[char] = 1
        else:
            counts_dict[char] += 1
    # print(counts_dict)

    percent_spaces = 0
    if ' ' in counts_dict:
        percent_spaces = counts_dict[' '] / num_chars

    percent_e = 0
    if 'e' in counts_dict:
        percent_e = counts_dict['e'] / num_chars

    # print('percent_spaces: ', percent_spaces)
    # print('percent_e: ', percent_e)

    return percent_e > 0.07


def is_maybe_english_from_ascii(ascii_list):
    num_chars = len(ascii_list)
    counts_dict = {}

    for i in range(32, 127):
        counts_dict[i] = 0

    for val in ascii_list:
        if val < 32 or val > 126:
            return False

        if val not in counts_dict:
            counts_dict[val] = 1
        else:
            counts_dict[val] += 1
    # print(counts_dict)

    percent_spaces = 0
    if 32 in counts_dict:
        percent_spaces = counts_dict[32] / num_chars

    # 101 is e
    # 69 is E
    percent_e = 0
    if 101 in counts_dict:
        num_es = counts_dict[101] + counts_dict[69]
        percent_e = num_es / num_chars

    # print('percent_spaces: ', percent_spaces)
    # print('percent_e: ', percent_e)

    return percent_e > 0.07


def decipher(cipher, short_key):
    plaintext = ''
    for i, num_code in enumerate(cipher):
        plaintext += chr(num_code ^ ord(short_key[i % 3]))
    return plaintext


def decipher_to_ascii(cipher, short_key):
    ascii_nums = []
    for i, num_code in enumerate(cipher):
        ascii_nums.append(num_code ^ ord(short_key[i % 3]))
    return ascii_nums


def temp():
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    for i in itertools.product(lower_alphabet, repeat=3):
        print(i)
        count += 1
    print('num permutations: ', count)


def cipher_decipher_test():
    a = 'We the people of the United States'
    print(a)
    b = make_cipher(a, ['a', 'b', 'c'])
    print(b)
    c = decipher_to_ascii(b, ['a', 'b', 'c'])
    # c = decipher(b, ['d', 'e', 'f'])
    print(c)


def is_maybe_english_test():
    a = 'We the people of the United States'
    print(is_maybe_english(a))




def get_solution():
    cipher = get_cipher('input_files/p059_cipher.txt')

    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count_on = 0
    keys = []
    for key in itertools.product(lower_alphabet, repeat=3):
        count_on += 1
        # text = decipher(cipher, key)
        ascii_list = decipher_to_ascii(cipher, key)
        # if is_maybe_english(text):
        if is_maybe_english_from_ascii(ascii_list):
            keys.append(key)
            print('count: ', count_on)
            print('key', key)
            print('text:\n', ''.join(chr(i) for i in ascii_list))
    print('keys: ', keys)


def eval_solution():
    cipher = get_cipher('input_files/p059_cipher.txt')
    ascii_list = decipher_to_ascii(cipher, ['e', 'x', 'p'])
    print('text:\n', ''.join(chr(i) for i in ascii_list))
    print('sum of ascii chars: ', sum(ascii_list))


def run():
    # cipher_decipher_test()
    # temp()
    # is_maybe_english_test()
    # get_solution()
    eval_solution()
