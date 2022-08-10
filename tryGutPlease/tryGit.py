def number_length(a: int) -> int:
    count = 0
    if a == 0:
        return 1
    while a > 0:
        a = a // 10
        count += 1
    return count


print('Example:')
print(number_length(10))

assert number_length(10) == 2
assert number_length(0) == 1
assert number_length(4) == 1
assert number_length(44) == 2

print("The mission is done! Click 'Check' to earn cool rewards!")