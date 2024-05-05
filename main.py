""" Main module of ab language.
Mostly for research and development purposes.
"""

import examples


def Main(input: str) -> str:
    content = input.strip() + '\n'
    lexemes: list[str] = []
    current: str = ''
    for char in content:
        if char == ' ' or char == '\'' or char == '\n':
            if current != '':
                lexemes.append(current)
                current = ''
            continue
        else:
            current += char

    print(lexemes)
    result = f"{lexemes[0]}(\"{lexemes[1]}\"); "
    return result


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
