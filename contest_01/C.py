import re


def to_numbers_only(str_number):
    numbers = re.sub(r"\-|\+|\(|\)", "", str_number)
    if len(numbers) == 11:
        numbers = numbers[1:]
    elif len(numbers) == 7:
        numbers = "495" + numbers
    return numbers


def main():
    given_number = to_numbers_only(input())
    for _ in range(3):
        try_number = to_numbers_only(input())
        print("YES") if try_number == given_number else print("NO")


if __name__ == "__main__":
    main()
