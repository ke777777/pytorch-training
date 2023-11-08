from .function import add

def count_word(input_str,x):
    assert isinstance(input_str,str)
    assert isinstance(x,str) and len(x) == 1
    count = 0
    for i in range(len(input_str)):
        if input_str[i] == x:
            count = add(count,1)
    return count
