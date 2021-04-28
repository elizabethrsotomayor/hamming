def distance(strand_a: str, strand_b: str) -> int:
    hamming_distance = 0
    if len(strand_a) == len(strand_b):
        for char in range(0, len(strand_a)):
            if strand_a[char] != strand_b[char]:
                hamming_distance += 1

        return hamming_distance
    else:
        raise ValueError(".+")
