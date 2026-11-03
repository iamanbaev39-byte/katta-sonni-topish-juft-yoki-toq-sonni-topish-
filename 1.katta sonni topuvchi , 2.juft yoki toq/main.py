def max_son(a, b):
    if a > b:
        return a
    return b


def juft_mi(son):
    if son % 2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    son = int(input("Butun son kiriting: "))
    # print(juft_mi(son))

    a = int(input("Birinchi sonni kiriting: "))
    b = int(input("Ikkinchi sonni kiriting: "))
    # print(max_son(a, b))
