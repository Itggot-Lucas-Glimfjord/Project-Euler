__author__ = 'lucas.glimfjord'

def collatz_length(values):

    if values[-1] > 1:
        if values[-1] % 2 == 0:
            values.append(values[-1]/2)
            collatz_length(values=values)
        else:
            values.append(values[-1]*3+1)
            collatz_length(values=values)

    return len(values)


def longest_collatz_below(number):
    longest = 0
    longest_number = 0
    for num in range(number):
        curr_length = collatz_length(values=[num])
        if curr_length > longest:
            longest = curr_length
            longest_number = num
    return longest_number

print longest_collatz_below(10**6)
# Answer = 837799