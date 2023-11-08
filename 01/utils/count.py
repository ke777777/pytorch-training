from .function import add

def count_word(input_str,x):
    assert isinstance(input_str,str)
    assert isinstance(x,str),len(x) == 1
    count = 0
    for char in input_str:
        if char == x:
            count += 1
    return count
