def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string
    sequence (string): an arbitrary string to permute.
    Returns: a list of all permutations of sequence
    '''

    if len(sequence) <= 1:
        return [sequence]
    else:
        permutations = []
        first_char = sequence[0]
        next_chars = sequence[1:]
        permutations_of_subsequence = get_permutations(next_chars)
        for seq in permutations_of_subsequence:
            for index in range(len(seq) + 1):
                new_seq = seq[0:index] + first_char + seq[index:len(seq) + 1]
                permutations.append(new_seq)

        # print(permutations)
        return permutations