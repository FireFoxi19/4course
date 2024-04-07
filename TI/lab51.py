import random
import numpy as np
import math

def check_error_block(word, start_word):
    error_counts = []
    for i in range(0, len(word), 4):
        count = 0
        text =""
        substring = word[i: i + 4]
        substring_start = start_word[i: i + 4]
        for j in range(4):
            text += substring[j]
        if(text != substring_start):
            count += 1
        error_counts.append(count)
    return error_counts


def error_fix(word, provmatrix):
    result = [0] * 3
    for i in range(3):
        prommini = [0] * len(word)
        prom = 0
        for j in range(len(word)):
            prommini[j] = word[j] * provmatrix[j][i]
        for k in range(len(word)):
            prom ^= prommini[k]
        result[i] = prom
    resultCh = result[0] * (4) + result[1] * (2) + result[2] * (1)
    if resultCh != 0:
        if word[resultCh - 1] == 0:
            word[resultCh - 1] = 1
        else:
            word[resultCh - 1] = 0


def encode_data(data):
    r = 3
    while 2 ** r < len(data) + r + 1:
        r += 1
    encoded_data = [0] * (len(data) + r)
    j = 0
    count = 0
    for i in range(len(encoded_data)):
        if i + 1 == 2 ** count:
            count += 1
        else:
            encoded_data[i] = int(data[j])
            j += 1

    for i in range(r):
        mask = 1 << i
        parity = 0
        for j in range(mask - 1, len(encoded_data), 2 * mask):
            for k in range(j, min(j + mask, len(encoded_data))):
                if k != mask - 1:
                    parity ^= encoded_data[k]
        encoded_data[mask - 1] = parity

    return encoded_data


def decode_data(encoded_data):
    r = 3
    while 2 ** r < len(encoded_data):
        r += 1
    decoded_data = []
    j = 0
    for i in range(len(encoded_data)):
        if not ((i + 1) & i):
            continue

        decoded_data.append(str(encoded_data[i]))
        j += 1

    return ''.join(decoded_data)


def main():
    file = open('coded_shannon.txt')

    f = file.read()
    file.close

    provmatrix = [[0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1], ]

    #print("Количество символов в исходном файле: ", len(f))

    substring_length = 4
    encoded_file_data = []

    for i in range(0, len(f), substring_length):
        substring = f[i:i + substring_length]
        encoded_file_data_el = encode_data(substring)
        encoded_file_data += encoded_file_data_el

    #print("Кол-во символов после кодирования: ", len(encoded_file_data))
    p = 0.1
    
    received_file_data = [bit if np.random.uniform() > p else 0 if bit == 1 else 1 for bit in encoded_file_data]

    substring_length_b = 7
    decoded_file_data = []
    for i in range(0, len(received_file_data), substring_length_b):
        substring = received_file_data[i:i + substring_length_b]
        error_fix(substring, provmatrix)

        decoded_file_data_el = decode_data(substring)
        decoded_file_data += decoded_file_data_el

    #print("Кол-во символов после декодирования: ", len(decoded_file_data))

    error_count = sum([1 for i in range(len(f)) if f[i] != decoded_file_data[i]])

   # print("Шанс появления ошибки p = ", p)
    print("Кол-во найденных ошибок:", error_count)

    error_counts_per_block = check_error_block(decoded_file_data, f)
    print("Кол-во ошибок в каждом блоке:", error_counts_per_block)

    total_blocks = len(error_counts_per_block)
    print("Общее количество блоков:", total_blocks)

if __name__ == "__main__":
    exit(main())