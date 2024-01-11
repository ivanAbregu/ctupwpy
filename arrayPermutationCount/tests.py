from main import ArrayChallenge

def test_one_relation():
    arr = ["A>B"]

    result = ArrayChallenge(arr)

    assert result==1

def test_2_relations():
    arr = ["A>B", "B>C"]

    result = ArrayChallenge(arr)

    assert result==1

def test_3_relations():
    arr = ["A>B", "B>C", "C>D"]

    result = ArrayChallenge(arr)

    assert result==1

def test_3_relations_with_2_orders():
    arr = ["A>B", "B>C", "D>B"]

    result = ArrayChallenge(arr)

    assert result==2

def test_3_relations_with_3_orders():
    arr = ["A>B", "B<C", "D>A"]

    result = ArrayChallenge(arr)

    assert result==3


def test_10_relations_with_1_order():
    arr = ["A>B", "B>C", "C>D", "D>E", "E>F", "F>G", "G>H","H>I", "I>J", "J>K"]

    result = ArrayChallenge(arr)

    assert result==1