def metro_time(a, b, n, m):
    max_res = min(n + a * (n + 1), m + b * (m + 1))
    min_res = max(n + a * (n - 1), m + b * (m - 1))
    if max_res < min_res:
        print("-1")
    else:
        print(min_res, max_res, sep=" ")


def main():
    # assert metro_time(1, 3, 3, 2) == (5, 7)
    # assert metro_time(1, 5, 1, 2) == -1

    a, b, n, m = int(input()), int(input()), int(input()), int(input())
    metro_time(a, b, n, m)


if __name__ == "__main__":
    main()
