from test_keypad import time_to_input

def test_simple():
    code = "423692"
    keypad = "923857614"

    result = time_to_input(code, keypad) 

    assert result == 8

def test_simple1():
    code = "5111"
    keypad = "752961348"

    result = time_to_input(code, keypad) 

    assert result == 1

def test_simple2():
    code = "91566165"
    keypad = "639485712"

    result = time_to_input(code, keypad) 

    assert result == 11

def test_simple3():
    code = "7436357276439613468239"
    keypad = "628547931"

    result = time_to_input(code, keypad) 

    assert result == 29

def test_simple4():
    code = "721981847441173183672391897415976961531854997879548596537229887167411364756586577191365647434662115558865182265"
    keypad = "619784325"

    result = time_to_input(code, keypad) 

    assert result == 148

def test_simple5():
    code = "1111111111112999999999999989999999999"
    keypad = "123456789"

    result = time_to_input(code, keypad) 

    assert result == 5
