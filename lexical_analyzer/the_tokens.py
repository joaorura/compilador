from categories import Categories


class Token:
    def __init__(self, line: int, col: int, lexeme: str, category: Categories):
        self._line = line
        self._col = col
        self._lexeme = lexeme
        self._category = category

    def get_line(self) -> int:
        return self._line

    def get_col(self) -> int:
        return self._col

    def get_category(self) -> Categories:
        return self._category

    def get_lexeme(self) -> str:
        return self._lexeme

    def __str__(self) -> str:
        return f'{" "*14}[{"{:04d}".format(self._line)}, {"{:04d}".format(self._col)}] ' \
               + f'({"{:04d}".format(self._category.value)}, {"{:20s}".format(self._category.name)})' \
                 + f' {"{"}{self._lexeme}{"}"}'
