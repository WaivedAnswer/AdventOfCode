def elf_code(start_val):
    zero = start_val
    five = 896

    if zero == 1:
        zero = 0
        five = 10551296

    for first_factor in range(1, five + 1):
        if five % first_factor == 0:
            zero += first_factor
    return zero

print("Answer: " + str(elf_code(0)))

print("Answer: " + str(elf_code(1)))