def least_instructions_to_halt():
    three = 123 #0

    while three != 72:
        three = three & 456 #1

    three = 0#5
    while True:
        two = three | 65536#6
        three = 1505483#7
        while True:
            four = two & 255#8
            three = three + four#9
            three = three & 16777215#10
            three = three * 65899#11
            three = three & 16777215#12

            if 256 > two:
                break

            four = 0#17
            while True:
                five = four + 1#18
                five = five * 256#19
                five = five > two#20
                if five:
                    break

                four = four + 1#24

            two = four#26
        return three
    return three


def most_instructions_to_halt():
    zero = 0
    three = 123 #0
    last = None
    seen = {}

    while three != 72:
        three = three & 456 #1

    three = 0#5
    while True:
        two = three | 65536#6
        three = 1505483#7
        while True:
            four = two & 255#8
            three = three + four#9
            three = three & 16777215#10
            three = three * 65899#11
            three = three & 16777215#12

            if 256 > two:
                break

            four = 0#17
            while True:
                five = four + 1#18
                five = five * 256#19
                five = five > two#20
                if five:
                    break

                four = four + 1#24

            two = four#26
        if three in seen:
            return last
        seen[three] = True
        last = three

        if three == zero:
            break
    return three


print(least_instructions_to_halt())
print(most_instructions_to_halt())