import numpy as np

def minhash_sets(sets, num_hash_functions):
    signature_matrix = np.zeros((num_hash_functions, len(sets[0])))

    for i in range(num_hash_functions):
        hash_functions = np.random.permutation(len(sets[0]))
        for j, set_shingles in enumerate(sets):
            for shingle in set_shingles:
                hash_val = hash_functions[np.argmin([hash(frozenset(shingle | {h})) for h in range(num_hash_functions)])]
                if signature_matrix[i, j] == 0 or hash_val < signature_matrix[i, j]:
                    signature_matrix[i, j] = hash_val

    return signature_matrix


# Example usage
set_A = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}, {4, 5}, {5}]
set_B = [{3, 4}, {4, 5}, {5, 6}, {6, 7}, {3}, {4}, {5}, {6}, {7}]
sets = [set_A, set_B]
num_hash_functions = 3
signature_matrix = minhash_sets(sets, num_hash_functions)
print(signature_matrix)
