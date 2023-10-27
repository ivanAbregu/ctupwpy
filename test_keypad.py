def time_to_input(code, keypad):
    dic = {
        0: [1,3,4],
        1: [0,2,3,4,5],
        2: [1,4,5],
        3: [0,1,4,6],
        4: [0,1,2,3,5,6,7,8],
        5: [1,2, 4,7,8],
        6: [3,4,7],
        7: [3,4,5,6,8],
        8: [4,5,7],
    }
    result = 0
    for index in range(len(code)):
        if index+1 >= len(code):
            break 
        value = code[index]
        next_value = code[index+1]
        if value == next_value:
            continue

        index_key = keypad.index(value)
        next_index_key = keypad.index(next_value)
        list_ne = dic[index_key]
        if next_index_key in list_ne:
            result +=1
        else:
            result +=2
    return result


if __name__== "__main__":
    """"
    Test case 1:
    5111
    752961348
    result: 1

    Test case 2:
    91566165
    639485712
    result: 11

    Test case 4:
    7436357276439613468239
    628547931
    result: 29
    721981847441173183672391897415976961531854997879548596537229887167411364756586577191365647434662115558865182265
    619784325
    result 148
    """
    code = "721981847441173183672391897415976961531854997879548596537229887167411364756586577191365647434662115558865182265"
    keypad = "619784325"
    print(time_to_input(code, keypad))
