#!/usr/bin/python
"""
Day 3: Mull It Over - Solution Script

This script reads a file with memory corrupted operations,
extracts each multiplication operations, and make the sum
of these operations.

Then it recalculate this sum after enbling or disabling
some operations.
"""
import re


def sum_for_lines(instruction) -> int:
    """
    Search operation in instructions, and returns the sum of their result.

    Returns:
        int: The sum of operations found in instructions
    """
    return sum(
        [
            int(a) * int(b)
            for a, b in re.findall(
                r"mul\((?P<first_nb>\d{1,3}),(?P<sec_nb>\d{1,3})\)",
                instruction
            )
        ]
    )


def main() -> tuple[int, int]:
    """
    Reads 'input.txt', processes the numbers, and calculates the result.

    Returns:
        int: The sum of each multiplication operation.
        int: The sum of each multiplication operation after disable and enable.
    """
    memory = 0
    adjusted_memory = 0
    mul_enabled = True
    with open("input.txt", encoding="utf-8") as f:
        for lines in f:
            memory += sum_for_lines(lines)
            instructions = re.split(r"(do\(\)|don't\(\))", lines)
            for instruction in instructions:
                if instruction == "do()":
                    mul_enabled = True
                elif instruction == "don't()":
                    mul_enabled = False
                if mul_enabled:
                    adjusted_memory += sum_for_lines(instruction)
    return memory, adjusted_memory


if __name__ == "__main__":
    memory, adjusted_memory = main()
    print(f"The total is {memory} after fixing memory.")
    print(f"The adjusted memory gives {adjusted_memory}.")
