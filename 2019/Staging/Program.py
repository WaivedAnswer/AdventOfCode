import Common
import itertools

def get_repeated(pattern, repeat):
    repeated = []
    for val in pattern:
        repeated.extend(itertools.repeat(val, repeat))
    return repeated


def transform(in_val, pattern = [0,1,0,-1]):
    out_digs = []
    str_val = "0" + str(in_val)
    for repeat, dig in enumerate(str(in_val)):
        repeat += 1
        repeated_pattern = itertools.cycle(get_repeated(pattern, repeat))
        zipped = list(zip(str_val, repeated_pattern))
        print(zipped)
        to_sum = [ int(val) * pattern_val for val, pattern_val in zipped ]
        print(to_sum)
        out_dig = abs(sum(to_sum)) % 10

        out_digs.append(out_dig)
    return out_digs


input_signal = 12345678
output_signal = None
print(transform(12345678))
for _ in range(100):
    output_signal = transform(input_signal)
    input_signal = output_signal

orbit_graph = nx.Graph()"""
