#! /usr/bin/env python

from math import log2, ceil
from collections import Counter
import re
import random


def FileOpen(filename: str, language: str):
    with open(filename, 'r', encoding='utf-8') as fileObj:
        text = fileObj.read()
        fileObj.close()
    text = text.lower()
    if language == "ru":
        text = re.sub(r'[^а-яА-Я0-9 ]', '', text)

    elif language == "en":
        text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    else:
        exit(1)
    return text
def EntropyFirst(line, symb_in_row):

    split_line = list(
        line[i: i + symb_in_row] for i in range(len(line) - symb_in_row + 1)
    )

    actual_probability = {k: v / len(line) for k, v in Counter(split_line).items()}

    if symb_in_row ==1:
        print(f'Алфавит: {len(actual_probability)}\nH = log({len(actual_probability)}) = {log2(len(actual_probability))}\n')

    result = -sum(x * log2(x) for x in actual_probability.values())

    return result / symb_in_row
def FileRead(filename, symbols_streak):
    print(f'\n\nЭнтропия:\n\n')
    for i in range(1, symbols_streak):

        print(f'{i} символ(ы): {EntropyFirst(filename, i)}\n')
def EntropySecond(filename, row):
    with open(filename, 'r') as fileObj:
        text = fileObj.read()
        fileObj.close()

    textLine = []

    for i in range(len(text)):
        if i + row >= len(text):
            break
        textLine.append(text[i: i + row])

    Occur = {}

    for symb in textLine:
        if symb in Occur:
            Occur.update({symb: Occur.get(symb) + row})
        else:
            Occur.update({symb: 1})

    actual_probability = {k: v / len(text) / row for k, v in Occur.items()}
    print(f'Фактическая: {sorted(actual_probability.items())}\n')

    result = -sum(x * log2(x) for x in actual_probability.values())

    return result / row
def RandFile(alphabet, filename, symbols_num):

    symbolsList = list(alphabet.keys())
    symbolsWeight = list(alphabet.values())
    with open(filename, 'w') as fileObj:
        for i in range(symbols_num):
            fileObj.write(''.join(random.choices(symbolsList, symbolsWeight)))
        fileObj.close()

    print(f'Алфавит: {alphabet}\n')
    for i in range(1, 4):
        print(f'Энтропия: {i} символ(ы)) {EntropySecond(filename, i)} \n')
    print()


    #2 LAB
def Dec(num):
    if num == 0.0:
        return 0.0
    while num > 1:
        num /= 10
    return num
def Float(number: float, places: int):
    whole, dec = str(number).split(".")
    whole = int(whole)
    dec = int(dec)
    res = bin(whole).strip("0b") + "."
    for x in range(places):
        whole, dec = str((Dec(dec)) * 2).split(".")
        dec = int(dec)
        res += whole
    return res
def SHANON(text: str):

    print("Результаты метода Шенона:")

    splited = list(text[i: i + 1] for i in range(len(text)))

    probabilities = {k: v / len(splited) for k, v in Counter(splited).items()}
    probabilities = dict(
        sorted(probabilities.items(), key=lambda item: item[1], reverse=True)
    )
    # print(probabilities)

    code_length = [ceil(-log2(i)) for i in probabilities.values()]
    # print(code_length)

    cumulative_probs = [float(0) for _ in range(len(probabilities))]
    for i in range(1, len(probabilities)):
        cumulative_probs[i] = (
            cumulative_probs[i - 1] + list(probabilities.values())[i - 1]
        )
    # print(cumulative_probs)

    codes = list()
    for i in range(len(cumulative_probs)):
        codes.append(Float(cumulative_probs[i], code_length[i])[1:])
        print(
            f"({list(probabilities.keys())[i]}) {list(probabilities.values())[i]:.4f} - {codes[i]}"
        )

    # print(codes)
    l_average = sum(
        list(probabilities.values())[i] * code_length[i]
        for i in range(len(probabilities.items()))
    )
    print("Средняя длина кодовых слов (L ср.):", l_average)

    with open("codedshanon.txt", "w") as f:
        for i in text:
            index = list(probabilities.keys()).index(i)
            f.write(codes[index])

    with open("codedshanon.txt", "r") as f:
        text = f.readline()
    for i in range(1, 4):
        print(f'Энтропия для {i} символа(ов) подряд:', EntropyFirst(text, i))
    return l_average
class Node(object):
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.lchild = None
        self.rchild = None

def HUFFMAN(text: str):

    print("Результаты метода Хаффмана:")

    splited = list(text[i: i + 1] for i in range(len(text)))

    probabilities = {k: v / len(splited) for k, v in Counter(splited).items()}
    probabilities = dict(
        sorted(probabilities.items(), key=lambda item: item[1], reverse=True)
    )


    list_ = [Node(k,v) for k, v in probabilities.items()]
    while len(list_) != 1:
        list_.sort(key=lambda node:node.value, reverse=True)
        n = Node(value=(list_[-1].value + list_[-2].value))
        n.lchild = list_.pop(-1)
        n.rchild =list_.pop(-1)
        list_.append(n)
    tree = list_[0]


    codes = dict()
    def generate(tree, code=''):
        node = tree
        if (not node):
            return
        elif node.name:
            codes[node.name] = code
            return
        generate(node.lchild, code + '0')
        generate(node.rchild, code + '1')
    
    generate(tree)

    for i in probabilities.keys():
        print( f"({i}) {probabilities[i]:.4f} - {codes[i]}")
    l_average = sum(probabilities[i] * len(codes[i]) for i in probabilities.keys())
    print("Средняя длина кодовых слов:", l_average)

    with open("codedhuffman.txt", "w") as f:
        for i in text:
            f.write(codes[i])

    with open("codedhuffman.txt", "r") as f:
        text = f.readline()
    for i in range(1, 4):
        print(f'Энтропия для {i} символа(ов) подряд:', EntropyFirst(text, i))
    return l_average


if __name__ == '__main__':

    #print("Мастер и Маргарита Глава 2. Понтий Пилат")

    text = FileOpen("text1.txt", "ru")
    #text = FileOpen("fileOne.txt", "ru")
    #text = FileOpen("fileTwo.txt", "ru")
    orig_entropy = EntropyFirst(text, 1)
    print("Энтропия оригинального текста:", orig_entropy)

    shanon = SHANON(text)
    huffman = HUFFMAN(text)

    print("Избыточность кодирования Шенон: ", shanon - orig_entropy)
    print("Избыточность кодирования Хаффман: ",huffman - orig_entropy)
    # tree = HuffmanTree(text)
    # tree.get_code()
