from os import path
from pathlib import Path


class Read:
    def __init__(self, path_file: str):
        if Path(path_file).suffix != '.d' or \
                not path.isfile(path_file):
            raise Exception()

        path_file = path.relpath(path_file)
        self._reader = open(path_file, 'r')
        self._line = 0

        self._actual_line = None
        self._cols = None
        self._lexemes = None
        self._actual_lexeme = None

        self._read_line()

    def _separate_lexemes(self, line: str):
        self._lexemes = []
        lexeme = ''
        count = None
        count_white = None
        sem_aspas = True

        for i, j in enumerate(line):
            if j == ' ' and sem_aspas:
                if count_white is not None:
                    count_white += 1

                if lexeme != '':
                    self._lexemes.append([count, count_white, lexeme])
                    lexeme = ''
                    count = count_white = None
            else:
                if j == '"':
                    sem_aspas = not sem_aspas

                if count is None:
                    count = i + 1
                    count_white = 0

                lexeme += j

        if lexeme != '':
            self._lexemes.append([count, 0, lexeme])

        if len(self._lexemes) > 0:
            self._lexemes[len(self._lexemes) - 1][1] = 0

        return

    def _read_line(self):
        result = self._reader.readline()

        if result == '':
            return False

        result = result.replace('\n', '')
        result = result.replace('\t', '    ')
        self._actual_line = result

        self._line += 1

        print("\n\n{:04d}  {:s}".format(self._line, result))

        self._cols = 1
        self._actual_lexeme = 0

        self._separate_lexemes(result)

        return True

    def _jump_white_line(self):
        while len(self._lexemes) == 0:
            test = self._read_line()

            if not test:
                return False

        return True

    def _check_end_line(self):
        if self._actual_lexeme == len(self._lexemes):
            return self._read_line()

        return True

    def get_line(self) -> int:
        return self._line

    def get_col(self):
        return self._cols

    def add_lexeme(self, rest_token: str, lexeme: str):
        if rest_token == '':
            return

        if self._actual_lexeme >= len(self._lexemes):
            the = self._lexemes[self._actual_lexeme - 1]
            the[2] = lexeme
            col = the[0] + the[1] + len(lexeme)
            self._lexemes.append([col, 0, rest_token])
        else:
            the0 = self._lexemes[self._actual_lexeme - 1]
            the0[2] = lexeme

            the1 = self._lexemes[self._actual_lexeme]
            col = the1[0] - the0[1] - len(rest_token)
            new = [col, the0[1], rest_token]
            self._lexemes.insert(self._actual_lexeme, new)
            the0[1] = 0

    def get_lexeme(self) -> str:
        if not self._check_end_line() or not self._jump_white_line():
            return None

        col, white, lexeme = self._lexemes[self._actual_lexeme]
        self._cols = col
        self._actual_lexeme += 1

        return lexeme

