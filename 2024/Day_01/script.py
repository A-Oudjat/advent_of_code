#!/usr/bin/python
"""
Day 1: Historian Hysteria - Solution Script

This script reads a file with two list of location ID, extracts each list,
sorts the first and second lists separately, and computes the sum of
absolute differences between the sorted locations to get the total distance.
Then it computes de similarity score between the lists.
"""


def main() -> tuple[int, int]:
    """
    Reads 'input.txt', processes the numbers, and calculates the result.

    Returns:
        int: The sum of absolute differences between location one and two.
        int: The sum of location count from the first list in the second one.
    """
    with open("input.txt", encoding="utf-8") as f:
        lines = [list(map(int, line.split())) for line in f]
    list_one = sorted(line[0] for line in lines)
    list_two = sorted(line[1] for line in lines)
    return (
        sum(abs(a - b) for (a, b) in zip(list_one, list_two)),
        sum(location * list_two.count(location) for location in list_one)
    )


if __name__ == "__main__":
    distance, similarity = main()
    print(f"The total distance is: {distance}")
    print(f"The similarity score is: {similarity}")
