import sys

class Ean:
    def __init__(self, n):
        self.n = n
        self.alphabet = range(10)
        generator = state_generator()
        self.initial = next(generator)
        self.levels = [[next(generator) for j in range(10)] for i in range(n)]
        self.transitions = transitions(self.initial, self.alphabet, self.levels)

    def __str__(self):
        states = '\n'.join([self.initial.name()] + [state.name() for level in self.levels for state in level])
        accepting = self.levels[self.n - 1][0]
        alphabet = '\n'.join([str(letter) for letter in self.alphabet])
        transitions = '\n'.join([str(transition) for transition in self.transitions])
        return f'#states\n{states}\n#initial\n{self.initial.name()}\n#accepting\n{accepting.name()}\n#alphabet\n{alphabet}\n#transitions\n{transitions}'

def state_generator():
    n = 0
    while True:
        yield State(n)
        n += 1

def transitions(initial, alphabet, levels):
    result = []
    sources = [initial]
    weight = 3 if len(levels) % 2 == 0 else 1
    for level in levels:
        for modulus in range(len(sources)):
            source = sources[modulus]
            for letter in alphabet:
                sink = level[(weight * letter + modulus) % 10]
                result.append(Transition(source, letter, sink))
        sources = level
        weight = 4 - weight
    return result

class State:
    def __init__(self, n):
        self.n = n

    def name(self):
        return f's{self.n}'

class Transition:
    def __init__(self, source, letter, sink):
        self.source = source
        self.letter = letter
        self.sink = sink

    def __str__(self):
        return f'{self.source.name()}:{str(self.letter)}>{self.sink.name()}'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError('Need a EAN size as argument')

    n = int(sys.argv[1])
    dfa = Ean(n)
    print(f'{str(dfa)}')