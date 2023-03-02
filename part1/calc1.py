from enum import Enum


class TokenType(Enum):
    INTEGER = "INTEGER"
    PLUS = "PLUS"
    MINUS = "MINUS"
    EOF = "EOF"


class Token:
    def __init__(self, type_: TokenType, value) -> None:
        self.type = type_
        self.value = value

    def __str__(self) -> str:
        return f"Token({self.type}, {self.value})"

    def __repr__(self) -> str:
        return self.__str__()


class Interpreter:
    def __init__(self, text: str) -> None:
        self.text: str = text
        self.pos: int = 0
        self.current_token: Token | None = None

    def error(self, c: str):
        raise TypeError(f"Invalid token {c}")

    def get_next_token(self):
        if self.pos > len(self.text) - 1:
            return Token(TokenType.EOF, None)

        pre_pos = self.pos
        curr_char: str = self.text[self.pos]

        while curr_char == ' ':
            self.pos += 1
            curr_char = self.text[self.pos]

        while curr_char.isdigit():
            self.pos += 1
            if self.pos < len(self.text) and self.text[self.pos].isdigit():
                curr_char = self.text[self.pos]
            else:
                return Token(TokenType.INTEGER, int(self.text[pre_pos:self.pos]))

        if curr_char == '+':
            self.pos += 1
            return Token(TokenType.PLUS, curr_char)

        if curr_char == '-':
            self.pos += 1
            return Token(TokenType.MINUS, curr_char)

        self.error(curr_char)

    def eat(self, token_types: set[TokenType]):
        if self.current_token.type in token_types:
            self.current_token = self.get_next_token()
        else:
            self.error(self.current_token.value)

    def expr(self) -> int:
        self.current_token = self.get_next_token()
        left = self.current_token
        self.eat({TokenType.INTEGER})

        op = self.current_token
        self.eat({TokenType.PLUS, TokenType.MINUS})

        right = self.current_token
        self.eat({TokenType.INTEGER})

        if op.type == TokenType.PLUS:
            result = left.value + right.value
        else:
            result = left.value - right.value
        return result


def main():
    while True:
        try:
            text = input("calc>")
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
