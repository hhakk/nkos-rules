#!/usr/bin/env python3

import numpy as np
import itertools

import argparse
import os
from PIL import Image


def rule_generator(rule_number: int, size_x: int, size_y: int, steps: int) -> np.array:
    """
    rule: NumPy reprsentaion of Stephen Wolfram rules in NKOS
    :param rule_number: which rule to return
    :param size_x: x size of NumPy array
    :param size_y: y size of NumPy array
    :param steps: how many steps to count
    :yields: a NumPy array of size_y x size_x for every step
    """
    assert steps < size_y

    # The center element
    center = size_x // 2

    # Creating a "canvas" array
    canvas = np.zeros((size_y, size_x))
    canvas[0, center] = 1

    # Creating all possible combinations of environments of tiles
    conditions = np.array(
        sorted(
            set(itertools.combinations_with_replacement([0, 1, 0, 1], r=3)),
            reverse=True,
        )
    )
    # Making a binary representation of rule name
    bin_rule = np.unpackbits(np.array([rule_number], dtype=np.uint8))

    for i in range(0, steps):
        for j in range(0, size_x - 3):
            env = canvas[i, j : j + 3]
            canvas[i + 1, j + 1] = bin_rule[np.where((conditions == env).all(axis=1))]

        yield canvas


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("rule_number", type=int, help="Rule number")
    parser.add_argument("size_x", type=int, help="Canvas X size")
    parser.add_argument("size_y", type=int, help="Canvas Y size")
    parser.add_argument(
        "steps", type=int, help="Number of steps, must be smaller than rule_number",
    )
    args = parser.parse_args()
    os.mkdir(f"{args.rule_number}")
    for idx, r in enumerate(
        rule_generator(args.rule_number, args.size_x, args.size_y, args.steps)
    ):
        frame = Image.fromarray(r * 255).convert("L")
        frame.save(f"./{args.rule_number}/frame_{idx:05d}.png")
