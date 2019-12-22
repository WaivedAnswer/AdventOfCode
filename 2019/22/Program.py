import Common


class NewStackOperation:
    def __init__(self, size):
        self.deck_size = size

    def get_index(self, pos):
        return self.deck_size - pos - 1


class CutOperation:
    def __init__(self, size, cut_size):
        self.deck_size = size
        self.cut_size = cut_size

    def get_index(self, pos):
        return (pos + self.cut_size) % self.deck_size


class IncrementOperation:
    def __init__(self, size, increment_size):
        self.deck_size = size
        self.increment_size = increment_size

    def get_index(self, pos):
        rounds = 0
        while (rounds * deck_size + pos) % self.increment_size != 0:
            rounds += 1
        return int((rounds * deck_size + pos) / self.increment_size)


class Deck:
    def __init__(self, size):
        self.deck_size = size
        self.index_ops = []

    def get_at(self, position):
        assert (position < self.deck_size)

        if not self.index_ops:
            return position
        index = position
        for op in reversed(self.index_ops):
            index = op.get_index(index)
        return index

    def deal_new_stack(self):
        self.index_ops.append(NewStackOperation(self.deck_size))

    def cut_n(self, n):
        self.index_ops.append(CutOperation(self.deck_size, n))

    def deal_increment(self, increment):
        self.index_ops.append(IncrementOperation(self.deck_size, increment))


def deal_new_stack(cards):
    return cards[-1::-1]


def cut_n(cards, n):
    cut = cards[:n]
    return cards[n:] + cut


def deal_increment(cards, increment):
    new = [None for card in cards]
    insert_index = 0
    for card in cards:
        new[insert_index] = card
        insert_index = (insert_index + increment) % len(cards)
    return new


"""cards = list(range(10))

print(deal_new_stack(cards))
print(cut_n(cards, -4))
print(deal_increment(cards, 3))"""

cards = list(range(10007))
lines = Common.inputAsLines()
for line in lines:
    instructions = line.split()
    if instructions[0] == 'cut':
        cards = cut_n(cards, int(instructions[1]))
    elif instructions[0] == 'deal' and instructions[1] == 'with':
        cards = deal_increment(cards, int(instructions[3]))
    elif instructions[0] == 'deal':
        cards = deal_new_stack(cards)

part1_index = cards.index(2019)
print(part1_index)

seen = set()
deck_size = 119315717514047
deck = Deck(deck_size)
lines = Common.inputAsLines()
for i in range(101741582076661):
    for line in lines:
        instructions = line.split()
        if instructions[0] == 'cut':
            deck.cut_n(int(instructions[1]))
        elif instructions[0] == 'deal' and instructions[1] == 'with':
            deck.deal_increment(int(instructions[3]))
        elif instructions[0] == 'deal':
            deck.deal_new_stack()
    val = deck.get_at(2020)
    print(val)
    if val in seen:
        print(i)
        break
    seen.add(val)

print(deck.get_at(2020))
