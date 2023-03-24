class Token:
    def __init__(self, token_type, lexeme):
        self.type = token_type
        self.lexeme = lexeme

    def __str__(self):
        return self.lexeme


class Tokenizer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.current_position = 0
        self.tokens = []

    def tokenize(self):
        while self.current_position < len(self.input_string):
            char = self.input_string[self.current_position]
            if char.isdigit():
                self.tokens.append(self.tokenize_number())
            elif char.isalpha():
                self.tokens.append(self.tokenize_identifier())
            elif char in '+-*/':
                self.tokens.append(Token('OPERATOR', char))
                self.current_position += 1
            elif char == '(':
                self.tokens.append(Token('LPAREN', char))
                self.current_position += 1
            elif char == ')':
                self.tokens.append(Token('RPAREN', char))
                self.current_position += 1
            elif char.isspace():
                self.current_position += 1
            else:
                raise ValueError(
                    f"Invalid character '{char}' at position {self.current_position}")

        # Return list of lexemes as strings

        while self.current_position < len(self.input_string):
            char = self.input_string[self.current_position]
            if char.isdigit():
                self.tokens.append(self.tokenize_number())
            elif char.isalpha():
                self.tokens.append(self.tokenize_identifier())
            elif char in '+-*/':
                self.tokens.append(Token('OPERATOR', char))
                self.current_position += 1
            elif char == '(':
                self.tokens.append(Token('LPAREN', char))
                self.current_position += 1
            elif char == ')':
                self.tokens.append(Token('RPAREN', char))
                self.current_position += 1
            elif char.isspace():
                self.current_position += 1
            else:
                raise ValueError(
                    f"Invalid character '{char}' at position {self.current_position}")

        return [token.lexeme for token in self.tokens]

    def tokenize_number(self):
        start_position = self.current_position
        while self.current_position < len(self.input_string) and self.input_string[self.current_position].isdigit():
            self.current_position += 1

        return Token('NUMBER', self.input_string[start_position:self.current_position])

    def tokenize_identifier(self):
        start_position = self.current_position
        while self.current_position < len(self.input_string) and self.input_string[self.current_position].isalpha():
            self.current_position += 1

        return Token('IDENTIFIER', self.input_string[start_position:self.current_position])


tokenizer = Tokenizer('3 + 4 * 2 / (1 - 5)')

print(tokenizer.tokenize())
