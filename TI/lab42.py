from collections import Counter
from math import log2
from lab3 import Node

def preprocess_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def calc_entropy_modified(line, symb_in_row):

    split_line = list(
        line[i: i + symb_in_row] for i in range(len(line) - symb_in_row + 1)
    )

    actual_probability = {k: v / len(line) for k, v in Counter(split_line).items()}

    result = -sum(x * log2(x) for x in actual_probability.values())

    return result / symb_in_row

def huffman_code_modified(text: str, n: int):
    print(f"Хаффман для блока размером {n}: ")

    # Создаем блоки текста заданной длины
    split_line = [text[i: i + n] for i in range(0, len(text), n)]

    # Вычисляем вероятности символов в блоках
    probabilities = {k: v / len(split_line) for k, v in Counter(split_line).items()}
    probabilities = dict(sorted(probabilities.items(), key=lambda item: item[1], reverse=True))

    # Строим дерево Хаффмана
    leaf = [Node(k, v) for k, v in probabilities.items()]
    while len(leaf) != 1:
        leaf.sort(key=lambda node:node.value, reverse=True)
        node = Node(value=(leaf[-1].value + leaf[-2].value))
        node.lchild = leaf.pop(-1)
        node.rchild = leaf.pop(-1)
        leaf.append(node)
    tree = leaf[0]

    # Создаем коды символов с помощью рекурсивного алгоритма
    codes = dict()
    def generate(node, code=''):
        if not node:
            return
        elif node.name:
            codes[node.name] = code
            return
        generate(node.lchild, code + '0')
        generate(node.rchild, code + '1')

    generate(tree)

    # Выводим коды и вероятности символов
    for i in probabilities.keys():
        print(f"{i}: {probabilities[i]:.10f} - {codes.get(i, '')}")
    l_average = sum(probabilities[i] * len(codes[i]) for i in probabilities.keys())
    print("Средняя длина кодовых слов (L ср.):", l_average)

    # Вычисляем и выводим энтропию
    entropy = calc_entropy_modified(text, n)
    if n == 1:
        print(f"Энтропия для {n} символа подряд: {entropy}")

        print(f"Избыточность для {n} символа подряд: {(l_average - entropy*n)/n}")
    else:
        print(f"Энтропия для {n} символов подряд: {entropy}")

        print(f"Избыточность для {n} символов подряд: {(l_average - entropy*n)/n}")

    return l_average

def main():
    file_name = "fileOne.txt"
    for n in range(1, 5):
        text = preprocess_file(file_name)
        huffman_code_modified(text, n)

if __name__ == "__main__":
    main()
