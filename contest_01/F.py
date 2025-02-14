def min_table(a, b, c, d):
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    rectangles = [
        (max(b, d), (a + c)),
        (max(a, c), (b + d)),
        (max(a, d), (b + c)),
        (max(b, c), (a + d)),
    ]
    rectangles.sort(key=lambda x: x[0] * x[1])
    return rectangles[0]


def main():
    a, b, c, d = map(int, input().split())
    res = min_table(a, b, c, d)
    print(res[0], res[1], sep=" ")
    # assert min_table(10,2,10,2) == (4,10)
    # assert min_table(5,7,3,2) == (5,9)


if __name__ == "__main__":
    main()
