import Common
import itertools

def get_repeated(pattern, repeat):
    repeated = []
    for val in pattern:
        repeated.extend(itertools.repeat(val, repeat))
    return repeated


def transform(in_val, pattern = (0,1,0,-1)):
    out_digs = []
    str_val = "0" + in_val
    for repeat, dig in enumerate(in_val):
        repeat += 1
        repeated_pattern = itertools.cycle(get_repeated(pattern, repeat))
        zipped = list(zip(str_val, repeated_pattern))

        to_sum = [int(val) * pattern_val for val, pattern_val in zipped]

        out_dig = abs(sum(to_sum)) % 10

        out_digs.append(str(out_dig))

    return "".join(out_digs)


input_signal = Common.inputAsString()
output_signal = None
for _ in range(100):
    input_signal = transform(input_signal)

print(input_signal[0:8])
