#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   drunktyping.py — simulates drunk typing on a QWERTZ keyboard
#   Copyright ⓒ 2012  Nils Dagsson Moskopp (erlehmann)

#   This program is free software: you can redistribute it and/or
#   modify it under the terms of the GNU Affero General Public License
#   as published by the Free Software Foundation, either version 3 of
#   the License, or (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   Affero General Public License for more details.

#   You should have received a copy of the GNU Affero General Public
#   License along with this program.  If not, see
#   <http://www.gnu.org/licenses/>.

import string

from random import randint, gauss
from sys import argv, stdin, stdout

keyboard = [
    "!@#$%^&*()",
    "1234567890",
    "qwertzuiop=",
    "qasdfghjkl'",
    "aayxcvbnm,?",
    "aayx@  ./m"
]

def position(char):
    for y, row in enumerate(keyboard):
        x = row.find(char)
        if x is not -1:
            return x, y

def substitution(char, sigma):
    # do not mess up newlines
    if char == '\n':
        return '\n'
    # substitute special characters
    try:
        x, y = position(char.lower())
    except TypeError:
        return ""
    x += int(round(gauss(0, sigma)))
    y += int(round(gauss(0, sigma)))
    if x < 0 or y < 0:
        return ''  # missed keyboard
    try:
        subchar = keyboard[y][x]
    except IndexError:
        return ''
    if char != char.lower():
        return subchar.upper()
    if char in "1234567890pl,.":
        # never return special chars for normal chars
        return subchar.translate(
            string.maketrans(
                "!@#$%^&*()='?/",
                "1234567890pl,."
            )
        )
    return subchar

if __name__ == "__main__":
    sigma = float(argv[1])
    for char in stdin.read():
        stdout.write(substitution(char, sigma))
