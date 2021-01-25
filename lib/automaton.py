class Ean:
    def __init__(self, n):
        self.n = n
        self.alphabet = range(10)
        generator = state_generator()
        self.initial = next(generator)
        self.levels = [[next(generator) for j in range(10)] for i in range(n)]
        self.accepting = self.levels[self.n - 1][0]
        self.transitions = transitions(self.initial, self.alphabet, self.levels)

    def __str__(self):
        states = '\n'.join([self.initial.name()] + [state.name() for level in self.levels for state in level])
        alphabet = '\n'.join([str(letter) for letter in self.alphabet])
        transitions = '\n'.join([str(transition) for transition in self.transitions])
        return f'#states\n{states}\n#initial\n{self.initial.name()}\n#accepting\n{self.accepting.name()}\n#alphabet\n{alphabet}\n#transitions\n{transitions}'

    def regular_expression(self):
        current = [transition for transition in self.transitions if transition.source == self.initial]
        for level in self.levels[1:]:
            current = [s.combine(t) for s in current for t in [transition for transition in self.transitions if transition.source == s.sink]]
        return '|'.join([transition.letter for transition in current if transition.sink == self.accepting])

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

    def combine(self, other):
        if not isinstance(other, Transition):
            raise ValueError(f'{other} should be a Transition')
        if not self.sink == other.source:
            raise ValueError(f'sink of {self} does not match source of {other}')
        return Transition(self.source, str(self.letter) + str(other.letter), other.sink)
