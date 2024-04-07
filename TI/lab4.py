def main():
    f = open('matrix1.txt')
    n = -1
    m = -1
    matr = []
    ma = []
    alp = []

    for line in f:
        if n == -1 and m == -1:
            n, m = map(int, line.split())
        else:
            ma = ((line.split()))
            # print(ma)
            matr.append(ma)
    f.close()

    print(f"Порождающая матрица {n} на {m}:")
    for i in range(n):
        for j in range(m):
            matr[i][j] = int(matr[i][j])
            alp.append(matr[i][j])
        print(matr[i])
    print("Размерность кода: ", n)
    print("Количество кодовых слов: ", pow(2, n))

    # count = m + 1
    # for code in range(len(matr)):
    #     for i in range(code + 1, len(matr)):
    #         cou = 0
    #         #print(count)
    #         for j in range(len(matr[i])):
    #             if matr[code][j] != matr[i][j]:
    #                 cou += 1
                    
    #         if cou < count:
    #             count = cou
    # print("Минимальное кодовое расстояние: ", count)


    count = m  
    for code in range(len(matr)):
        for i in range(code + 1, len(matr)):
            cou = 0
            for j in range(len(matr[i])):
                if matr[code][j] != matr[i][j]:
                    cou += 1

            if cou < count:
                count = cou

            if sum(matr[code]) != 0:
                cou_sum = sum(matr[code])
                if cou_sum < count:
                    count = cou_sum
            if sum(matr[i]) != 0:
                cou_sum = sum(matr[i])
                if cou_sum < count:
                    count = cou_sum

    print("Минимальное кодовое расстояние: ", count)

if __name__ == "__main__":
    exit(main())