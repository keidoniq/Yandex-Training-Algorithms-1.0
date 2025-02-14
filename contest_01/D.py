import math


def solve_equation(a, b, c):
    if c < 0:
        return "NO SOLUTION"
    if a == 0 and math.sqrt(b) == c:
        return "MANY SOLUTIONS"
    x = c * c - b
    if a != 0 and x % a == 0:
        return int(x / a)
    return "NO SOLUTION"


def main():
    assert solve_equation(1, 0, 0) == 0
    assert solve_equation(1, 2, 3) == 7
    assert solve_equation(1, 2, -3) == "NO SOLUTION"
    assert solve_equation(0, 0, 0) == "MANY SOLUTIONS"
    a, b, c = int(input()), int(input()), int(input())
    print(solve_equation(a, b, c))


if __name__ == "__main__":
    main()
