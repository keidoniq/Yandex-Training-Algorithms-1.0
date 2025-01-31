def is_valid_triangle(a, b, c):
    return (
        "YES"
        if (a > 0 and b > 0 and c > 0 and (a < b + c) and (b < a + c) and (c < a + b))
        else "NO"
    )


def main():
    print(is_valid_triangle(int(input()), int(input()), int(input())))


if __name__ == "__main__":
    main()
