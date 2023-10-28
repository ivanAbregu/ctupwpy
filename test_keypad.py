


def time_to_input(code, keypad):
    result = 0
    dic_values = get_dic_values()

    prev_index = keypad.index(code[0])

    for index in range(1, len(code)):
        value = code[index]
        index_key = keypad.index(value)

        if value == code[index - 1]:
            prev_index = index_key
            continue

        if index_key in dic_values[prev_index]:
            result += 1
        else:
            result += 2
        prev_index = index_key


    return result

def get_dic_values():
    return {
        0: [1, 3, 4],
        1: [0, 2, 3, 4, 5],
        2: [1, 4, 5],
        3: [0, 1, 4, 6, 7],
        4: [0, 1, 2, 3, 5, 6, 7, 8],
        5: [1, 2, 4, 7, 8],
        6: [3, 4, 7],
        7: [3, 4, 5, 6, 8],
        8: [4, 5, 7],
    }
