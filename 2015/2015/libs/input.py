import re


def file() -> list[str]:
    return open("input.txt").read().strip().split("\n")


def grid() -> list[list[str]]:
    return [[char for char in line] for line in file()]


def sub_grid() -> list[list[list[str]]]:
    return [[[char for char in line] for line in grid.split("\n")] for grid in open("input.txt").read().strip().split("\n\n")]


def nums(lines: list[str], sort: bool = False) -> list[list[int]]:
    return [sorted([int(x) for x in re.findall(r'-?\d+', line)]) if sort else [int(x) for x in re.findall(r'-?\d+', line)] for line in lines]


def pairs(array: list[any]) -> list[tuple[any, any]]:
    length = len(array)
    _ret = []
    
    for i in range(length - 1):
        _ret.append((array[i], array[i + 1]))
    
    return _ret

def triples(array: list[any]) -> list[tuple[any, any, any]]:
    length = len(array)
    _ret = []
    
    for i in range(length - 2):
        _ret.append((array[i], array[i + 1], array[i + 2]))
    
    return _ret
