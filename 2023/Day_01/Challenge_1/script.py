#!/usr/bin/python


def main() -> int:
    result_list = []
    for line in list(open("input.txt")):
        for char in line:
            if char.isdigit():
                first_digit = char
                break
        for char in reversed(line):
            if char.isdigit():
                second_digit = char
                break
        result_list.append(int(f"{first_digit}{second_digit}"))
    return sum(result_list)


if __name__ == "__main__":
    result = main()
    print(result)
