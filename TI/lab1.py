#! /usr/bin/env python


from math import log2
from collections import Counter
import re
import random


def Open(filename: str, language: str):
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


def CalcEntropy1(text, row):

    split = list(
        text[i: i + row] for i in range(len(text) - row + 1)
    )

    actual_probability = {k: v / len(text) for k, v in Counter(split).items()}

    if row ==1:
        print(f'Алфавит: {len(actual_probability)}\nH = log({len(actual_probability)}) = {log2(len(actual_probability))}\n')

    result = -sum(x * log2(x) for x in actual_probability.values())

    return result / row


def Read(filename, symbols_streak):
    print(f'\n\n -Полученная энтропия-:\n\n')
    for i in range(1, symbols_streak):

        print(f'{i} символ(ы): {CalcEntropy1(filename, i)}\n')

def CalcEntropy2(filename, row):
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
    print(f'-Фактическая-:\n {sorted(actual_probability.items())}\n')

    result = -sum(x * log2(x) for x in actual_probability.values())

    return result / row


def Randomize(alphabet, filename, symbols_num):

    symbolsList = list(alphabet.keys())
    symbolsWeight = list(alphabet.values())
    with open(filename, 'w') as fileObj:
        for i in range(symbols_num):
            fileObj.write(''.join(random.choices(symbolsList, symbolsWeight)))
        fileObj.close()

    print(f'Алфавит: {alphabet}\n')
    for i in range(1, 4):
        print(f'-Энтропия-:\n {i} символ(ы)) {CalcEntropy2(filename, i)} \n')
    print()
if __name__ == '__main__':
    e = {'М': 1/3, 
          'И': 1/3, 
          'Р': 1/3}
    d = {'М': 0.1, 
            'И': 0.3, 
            'Р': 0.6}
    print("Равная вероятность (5000 симв.)")
    Randomize(e, 'fileOne.txt', 50000)
    print("\n")
    print("max = log(3) =")
    print(log2(3))
    print("\n")
    print("Заданная вероятность (50000 симв.)")
    Randomize(d, 'fileTwo.txt', 50000)
    print("Мастер и Маргарита. Глава 2. Понтий Пилат")
    text = Open('text1.txt', 'ru')
    Read(text, 6)
