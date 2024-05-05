
def Main(input: str) -> str:
    content = input.strip() + '\n'
    tokens: list[str] = []
    word: str = ''
    string_mode: bool = False
    for letter in content:
        if (letter == '\n' or letter == ' ') and string_mode == False:
            if word != '':
                tokens.append(word)
            word = ''
        elif letter == '\'':
            if string_mode == True:
                string_mode = False
            else:
                string_mode = True
        else:
            word += letter
    return f"{tokens[0]}(\"{tokens[1]}\"); "


IN = \
    """
printf 'Hello, world!'
"""


OUT = \
    """
printf("Hello, world!");
"""


if __name__ == '__main__':
    result = Main(IN).strip()
    expected = OUT.strip()
    if result == expected:
        print('succeed')
    else:
        print('failed')
        print('\n')
        print('result:')
        print(result)
        print('\n')
        print('expected:')
        print(expected)
        print('\n')
