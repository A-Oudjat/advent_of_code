#!/usr/bin/python
"""
Day 2: Red-Nosed Reports - Solution Script

This script reads a file with list of reports of levels,
extracts each reports, check if reports are increasing
and decreasing below a difference of 3 levels.

Then it checks if a report can be corrected by removing
one level of the report.
"""


def is_safe(line):
    """
    Check if the list is strictly increasing or decreasing with a limit of 3

    Args:
        line (list[int]): The list of int to check

    Returns:
        bool: True if the conditions are met, False otherwise
    """
    return (
        all(i < j <= i + 3 for i, j in zip(line, line[1:]))
        or all(i > j >= i - 3 for i, j in zip(line, line[1:]))
    )


def main() -> tuple[int, int]:
    """
    Reads 'input.txt', processes the numbers, and calculates the result.

    Returns:
        int: The count of lines meeting the initial condition.
        int: The count of lines meeting the condition after corrections.
    """
    with open("input.txt", encoding="utf-8") as f:
        lines = [list(map(int, line.split())) for line in f]
    init_count = sum(is_safe(line) for line in lines)
    corrected_count = sum(
        any(is_safe(line[:i] + line[i+1:]) for i in range(len(line)))
        for line in lines if not is_safe(line)
    )
    return init_count, init_count + corrected_count


if __name__ == "__main__":
    total_safe, corrected = main()
    print(f"There is a total of {total_safe} safe reports")
    print(f"There is a total of {corrected} safe reports after correction")
