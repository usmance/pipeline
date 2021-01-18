
def test(num):
    if num==2:
        raise ValueError('The value should be less than 2')

test(2)