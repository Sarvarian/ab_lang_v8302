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

    print(lexemes)
    # result = f"{lexemes[0]}(\"{lexemes[1]}\"); "
    return input


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
