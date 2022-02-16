import re
import operator
import numpy as np


class Number:
    DEFAULT_OPERATION_BASE = 10

    def __init__(self, str_repr, base: int):
        self.str_repr = str(str_repr)
        self.base = base

    def convert(self, to_base: int) -> str:
        return np.base_repr(int(self.str_repr, self.base), to_base)

    def __perform(self, other, oper):
        return Number(
            int(oper(
                int(self.convert(Number.DEFAULT_OPERATION_BASE)),
                int(other.convert(Number.DEFAULT_OPERATION_BASE))
            )),
            Number.DEFAULT_OPERATION_BASE
        )

    def __add__(self, other):
        return self.__perform(other, operator.add)

    def __sub__(self, other):
        return self.__perform(other, operator.sub)

    def __mul__(self, other):
        return self.__perform(other, operator.mul)

    def __truediv__(self, other):
        return self.__perform(other, operator.truediv)

    def __str__(self):
        return self.str_repr


class Parser:
    SPLIT_PATTERN = "="

    @staticmethod
    def parse(string):
        expr, res_base = map(
            lambda x: x.strip(),
            re.split(
                Parser.SPLIT_PATTERN,
                string.replace("n", Number.__name__)
            )
        )
        return eval(expr).convert(int(res_base))


def main(*args, **kwargs):
    print(Parser.parse(input()))


if __name__ == '__main__':
    main()
