#!/usr/bin/python
import re

STR2NUM = {
    "one": "o1e",
    "two": "t2o",
    "three": "th3ee",
    "four": "f4r",
    "five": "f5ve",
    "six": "s6x",
    "seven": "se7en",
    "eight": "ei8ht",
    "nine": "n9ne",
}


def replace_words(text: str) -> str:
    for k, v in STR2NUM.items():
        text = text.replace(k, v)
    return text


def calibration(text: str) -> int:
    return sum(int(l[0] + l[-1]) for l in re.sub(r"[A-z]", "", text).split("\n"))


def main() -> int:
    text = open("input.txt").read()
    print(calibration(text))
    print(calibration(replace_words(text)))


if __name__ == "__main__":
    result = main()
