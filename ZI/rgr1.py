from collections import defaultdict
import random
import matplotlib.pyplot as plt
import networkx as nx
from lab2 import *
# проверка на простоту числа используя теореме Ферма
def check_prime(p):
    if p <= 1:
        return False
    elif p == 2:
        return True
    a = random.randint(2, p - 1)
    # print(p, "-", a)
    if pow_module(a, (p - 1), p) != 1 or gcd(p, a) > 1:
        return False
    return True
# генерируем простое число в указанных границах
def generate_prime(left, right):
    while True:
        p = random.randint(left, right)
        # print("--", p)
        if check_prime(p):
            return p
# генерируем взаимно-простое число
def generate_coprime(p):
    result = random.randint(2, p)
    # print(result)
    while gcd(p, result) != 1:
        result = random.randint(2, p)
    # print(result)
    return result
# возведение в степень по модулю
def pow_module(a, x, p):
    result = 1
    a = a % p
    if a == 0:
        return 0;
    while x > 0:
        if x & 1 == 1: # если крайний правый бит степени равен lib
            result = (result * a) % p
        a = (a ** 2) % p
        x >>= 1 # побитово смещаем степень
    return result
# Алгоритм Евклида, для нахождения наибольшего общего делителя
def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
def gcd_modified(a, b):
    U = (a, 1, 0)
    V = (b, 0, 1)
    while V[0] != 0:
        q = U[0] // V[0]
        T = (U[0] % V[0], U[1] - q * V[1], U[2] - q * V[2])
        U = V
        V = T
    return U

def read_graph_from_file(file_path='Path.txt'):
    try:
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
    except OSError:
        print("Ошибка открытия файла с графами")
        return -1

    N = int(lines[0])
    M = int(lines[1])
    node_ids = list(range(1, N + 1))
    header = "\t" + "\t".join(map(str, node_ids))

    graph_G = [[0] * N for _ in range(N)]
    graph_H = [[0] * N for _ in range(N)]

    print("Стартовый граф:")
    print(header)
    
    for i in range(N):
        print(f" {node_ids[i]}", end="\t")
        for j in range(N):
            graph_G[i][j] = 0
            print(graph_G[i][j], end="\t")
        print()

    print("\nГраф после заполнения Алисой:")
    print(header)
    
    for k in range(M):
        line = lines[k + 2]
        i, j = map(int, line.split(","))
        graph_G[i - 1][j - 1] = 1
        graph_G[j - 1][i - 1] = 1
        graph_H[i - 1][j - 1] = 1
        graph_H[j - 1][i - 1] = 1

    for i in range(N):
        print(f" {node_ids[i]}", end="\t")
        for j in range(N):
            print(graph_G[i][j], end="\t")
        print()

    return N, M, graph_G, graph_H, header

def visualize_graph(graph, header, graph_type):
    G = nx.Graph()
    N = len(graph)

    for i in range(N):
        G.add_node(i + 1)

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                G.add_edge(i + 1, j + 1) 

    pos = nx.spring_layout(G)

    plt.figure(figsize=(10, 8))
    plt.title(f"Визуализация графа {graph_type}")
    nx.draw(G, pos, with_labels=True, node_size=700, font_size=10, font_color="black")
    plt.show()

def all_paths(graph):
    paths = defaultdict(list)
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                paths[i].append(j + 1)
    return paths

def search_hamilton_cycle(graph, size, pt, path=[]):
    if pt not in set(path):
        path.append(pt)
        if len(path) == size:
            return path
        for pt_next in graph.get(pt - 1, []):
            res_path = path.copy()
            candidate = search_hamilton_cycle(graph, size, pt_next, res_path)
            if candidate is not None:
                return candidate

def rsa_matrix_encode(new_graph, x, p, N):
    temp_graph = [[0] * N for _ in range(N)]
    for i in range(len(new_graph)):
        for j in range(len(new_graph[i])):
            temp_graph[i][j] = pow_module(new_graph[i][j], x, p)
    return temp_graph

def hamilton_cycle():
    N, M, graph_G, graph_H, header = read_graph_from_file()
    list_path = list()
    new_graph_H = [[0] * N for _ in range(N)]
    new_graph_G = [[0] * N for _ in range(N)]
    left_random = list(range(1, N + 1))
    random.shuffle(left_random)

    print(f"\nN = {N}, M = {M}")
    paths = all_paths(graph_G)

    print("\nПереходы:")
    for i in range(len(paths)):
        print(f"{i + 1}: {paths[i]}")

    cycle_path = search_hamilton_cycle(paths, N, 1, list_path)
    print(f"\nГамильтонов цикл: {cycle_path}\n")

    print("--------------------------------------")
    print("Действия первого абонента - Алисы")
    print("--------------------------------------")

    new_list = list(range(N))
    random.shuffle(new_list)
    new_list_str = [i + 1 for i in new_list]
    print(f"Алиса рандомит вершины графа: {new_list_str} \n")

    k, z = 0, 0
    for i in new_list:
        for j in new_list:
            new_graph_H[k][z] = graph_G[int(i)][int(j)]
            z += 1
        z = 0
        k += 1

    print("Изоморфный граф: ")
    print(header)
    for i in range(len(new_graph_H)):
        print(" " + str(i + 1), end="\t")
        for j in range(len(new_graph_H[i])):
            print(new_graph_H[i][j], end="\t")
        print("\n", end="")

    print("\nПеред кодировкой алгоритмом RSA\n" +
          f"Припишем рандомное число из списка {left_random}")

    k, z = 0, 0
    for i in left_random:
        for j in left_random:
            new_graph_H[k][z] = int(str(j) + str(new_graph_H[k][z]))
            z += 1
        z = 0
        k += 1

    print("\nПодготовленная матрица до RSA:")
    print(header)
    for i in range(len(new_graph_H)):
        print(" " + str(i + 1), end="\t")
        for j in range(len(new_graph_H[i])):
            print(new_graph_H[i][j], end="\t")
        print("\n", end="")

    print("\nАлиса генерирует ключи: ")
    P = generate_prime(0, 10 ** 9)
    Q = generate_prime(0, 10 ** 9)
    N_encode = P * Q
    print("Ключ N: ", N_encode)
    Phi = (P - 1) * (Q - 1)
    d = generate_coprime(Phi)
    c = gcd_modified(d, Phi)[1]
    if c < 0:
        c += Phi
    print("Ключ c: ", c)
    graph_F = rsa_matrix_encode(new_graph_H, d, N_encode, N)

    print("\nМатрица после RSA, для Боба:")
    print(header)
    for i in range(len(graph_F)):
        print(" " + str(i + 1), end="\t")
        for j in range(len(graph_F[i])):
            print(graph_F[i][j], end="\t")
        print("\n", end="")

    print()
    print("--------------------------------------")
    print("Действия Второго абонента - Боба")
    print("--------------------------------------")
    print("Боб получил матрицу F\n")
    print("Какой вопрос выберет Боб?")
    print("1.'Алиса, каков Гамильтонов цикл для графа H?'")
    print("2.'Алиса, действительно ли граф H изоморфен G?'")

    answer = int(input())
    if answer == 1:
        print("-'Алиса, покажи Гамильтонов цикл?'")
        print(f"Гамильтонов цикл: {cycle_path}")
        print("Боб проходит по Матрице Н-штрих, преобразуя соответствующий элемент цикла")
        print("Если элементы Матрицы F равны этим преобразованным, то Боб пытается по данному циклу пройти свой граф\n"
              + "Если ему это удается, то Все в порядке. Если нет, то возникла ошибка в алгоритме")
        bob_check = rsa_matrix_encode(new_graph_H, d, N_encode, N)
        flag = all(bob_check[i][j] == graph_F[i][j] for i in range(len(graph_F)) for j in range(len(graph_F[i])))
        if flag:
            print(f"\nМатрицы идентичны, т.к. flag = {flag}")
            print(f"Гамильтонов цикл Алисы: {cycle_path}")
            print(f"Гамильтонов цикл Боба: {cycle_path}")
        else:
            print(f"Матрицы разные flag = {flag}")

    if answer == 2:
        print("-'Докажи изоморфизм, Алиса?'")
        print("\nАлиса отсылает Бобу матрицу, которая еще не преобразована в RSA\n" +
              "И рандом столбцов, который она использовала после получения Гамильтонова цикла")
        print("\nБоб проверяет матрицы: сравнивает матрицы F и H-штрих путем\n" +
              "повторного шифрования и сравнения матриц")
        bob_check = rsa_matrix_encode(new_graph_H, d, N_encode, N)
        flag = all(bob_check[i][j] == graph_F[i][j] for i in range(len(graph_F)) for j in range(len(graph_F[i])))
        if flag:
            print(f"\nМатрицы идентичны, т.к. flag = {flag}")
        else:
            print(f"\nМатрицы разные flag = {flag}")
        print("Далее Боб отбрасывает все разряды кроме единичного от каждого элемента матрицы и получает матрицу,\n" +
              "изоморфную стартовой\n")
        print(header)
        for i in range(len(new_graph_H)):
            print(" " + str(i + 1), end="\t")
            for j in range(len(new_graph_H[i])):
                num_str = str(new_graph_H[i][j])
                new_graph_H[i][j] = int(num_str[-1])
                print(new_graph_H[i][j], end="\t")
            print("\n", end="")

    print("\nЗатем Боб переставляет столбцы в соответствии с полученной нумерацией от Алисы")
    print(f"\nРандом Алисы вершин графа: {new_list_str}")

    k, z = 0, 0
    for i in new_list:
        for j in new_list:
            new_graph_G[int(i)][int(j)] = new_graph_H[k][z]
            z += 1
        z = 0
        k += 1

    print("\nЗатем Алиса проверяет граф H, преобразуя его по ряду Алисы, и исходный граф Алисы\n" +
          "Если они идентичны, то из графа H мы получили граф G")
    flag = all(graph_H[i][j] == new_graph_G[i][j] for i in range(len(graph_H)) for j in range(len(graph_H[i])))
    if flag:
        print()
        print(f"Матрицы идентичны, т.к. flag = {flag}")
    else:
        print(f"Матрицы разные flag = {flag}")

    print("\nГраф G:")
    visualize_graph(graph_G, header, "G")

    print("Изоморфный граф H:")
    visualize_graph(new_graph_H, header, "H")

if __name__ == '__main__':
    hamilton_cycle()
