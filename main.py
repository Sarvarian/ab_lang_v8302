""" Main module of ab language.
Mostly for research and development purposes.
"""

import examples


def Main(input: str) -> str:
    content = input.strip() + '\n'
    lexemes: list[str] = []
    char: str = ''
    i: int = 0
    word: str = ''
    while (i < len(content)):
        char = content[i]
        if char == ' ':
            if word != '':
                lexemes.append(word)
                word = ''
        elif char == '\'':
            if word != '':
                lexemes.append(word)
            lexemes.append('COMMA')
            word = ''
        elif char == '\n':
            if word != '':
                lexemes.append(word)
            lexemes.append('EOL')
            word = ''
        else:
            word += char
        i += 1

    body: list[list[str]] = []

    i: int = 0
    for lexeme in lexemes:
        if len(body) <= i:
            body.append([])

        if lexeme == 'EOL':
            i += 1
        else:
            body[i].append(lexeme)

    root: list[list[str]] = []

    for statement_old in body:
        statement: list[str] = []
        root.append(statement)
        string_mode = False
        string_array: list[str] = []
        for lexeme in statement_old:
            if lexeme == 'COMMA':
                if string_mode == True:
                    statement.append(' '.join(string_array))
                    string_mode = False
                else:
                    string_mode = True
            elif string_mode:
                string_array.append(lexeme)
            else:
                statement.append(lexeme)

    lines: list[str] = []

    for statement in root:
        if len(statement) < 1:
            continue
        elif statement[0] == 'return':
            lines.append(f'return {statement[1]};\n')
        elif statement[0] == 'printf':
            lines.append(f'printf(\"{statement[1]}\");\n')

    # print(root)
    # result = f"{lexemes[0]}(\"{lexemes[1]}\"); "
    return ''.join(lines)


if __name__ == '__main__':
    for i in range(len(examples.examples)):
        example = examples.examples[i]
        print(f"==================== Example {i} ====================")
        result = Main(example[0]).strip()
        expected = example[1].strip()
        if result == expected:
            print('========== Succeed ==========')
        else:
            print('========== Failed ==========')
            print('===== Result =====')
            print(result)
            print('===== Expected =====')
            print(expected)
        print(f"=====================================================")

    # subprocess.run(
    #     'py -3.12 -m unittest discover --start-directory ./ --pattern \"*_test.py\"')
