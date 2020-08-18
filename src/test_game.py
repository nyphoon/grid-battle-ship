import pytest
from game import one_round

def test_one_round():
    N = 4
    S = '1B 2C,2D 4D'
    T = '2B 2D 3D 4D 4A'
    assert '1,1' == one_round(N, S, T)

    N = 3
    S = '1A 1B,2C 2C'
    T = '1B'
    assert '0,1' == one_round(N, S, T)

    N=12
    S='1A 2A,12A 12A'
    T='12A'
    assert '1,0' == one_round(N, S, T)

    N = 2
    S = '1A 2A'
    T = ''
    assert '0,0' == one_round(N, S, T)

    N = 26
    S = '1B 2C,2D 4D,5A 5C,6B 6C'
    T = '2A 4B'
    assert '0,0' == one_round(N, S, T)