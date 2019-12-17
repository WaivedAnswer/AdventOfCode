import Common
import itertools


def get_repeated(pattern, repeat):
    repeated = []
    for val in pattern:
        repeated.extend(itertools.repeat(val, repeat))
    return repeated


def generate_patterns(required_length):
    patterns = {}
    pattern = (0, 1, 0, -1)
    pos_pattern = (False, True, False, False)
    neg_pattern = (False, False, False, True)
    for repeat in range(1, required_length + 1):
        repeated_pos = itertools.cycle(get_repeated(pos_pattern, repeat))
        repeated_neg = itertools.cycle(get_repeated(neg_pattern, repeat))
        pos_indices = [idx for idx, use_val in enumerate(itertools.islice(repeated_pos, 1, required_length + 1)) if use_val]
        neg_indices = [idx for idx, use_val in enumerate(itertools.islice(repeated_neg, 1, required_length + 1)) if use_val]
        patterns[repeat] = (pos_indices, neg_indices)
    print("Patterns")

    return patterns


def transform(in_val, patterns):
    out_digs = []
    for idx, dig in enumerate(in_val):
        repeat = idx + 1
        pattern = patterns[repeat]
        pos_indices = pattern[0]
        neg_indices = pattern[1]
        sum_value = sum(in_val[idx] for idx in pos_indices) - sum(in_val[idx] for idx in neg_indices)
        out_dig = abs(sum_value) % 10
        out_digs.append(out_dig)

    return out_digs


input_signal = Common.inputAsString()
input_length = len(input_signal)
numbers = []
for c in input_signal:
    numbers.append(int(c))

input_signal = numbers

input_signal = itertools.repeat(input_signal, 10000)

repeated_patterns = generate_patterns(input_length * 10000)

for _ in range(100):
    input_signal = transform(input_signal, repeated_patterns)
    print(input_signal)

print(input_signal[0:8])
