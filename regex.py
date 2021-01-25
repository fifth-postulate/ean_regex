import sys
from lib.automaton import Ean

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError('Need a EAN size as argument')

    n = int(sys.argv[1])
    dfa = Ean(n)
    print(dfa.regular_expression())