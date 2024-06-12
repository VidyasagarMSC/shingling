import numpy as np


def generate_hash_functions(num_hashes, max_val):
	"""
	Generate a list of hash functions.

	Args:
		num_hashes (int): Number of hash functions to generate.
		max_val (int): Maximum value for the hash function coefficients.

	Returns:
		list of tuples: Each tuple contains coefficients (a, b) for a hash function.
	"""
	hash_funcs = []
	for _ in range(num_hashes):
		a = np.random.randint(1, max_val)
		b = np.random.randint(0, max_val)
		hash_funcs.append((a, b))
	return hash_funcs


def minhash_signature_matrix(data, num_hashes):
	"""
	Compute the MinHash signature matrix for a collection of sets.

	Args:
		data (list of sets): The input sets.
		num_hashes (int): The number of hash functions to use.

	Returns:
		numpy.ndarray: The MinHash signature matrix.
	"""
	num_sets = len(data)
	max_val = max(max(s) for s in data) + 1
	hash_funcs = generate_hash_functions(num_hashes, max_val)

	# Initialize the signature matrix with infinity
	signature_matrix = np.full((num_hashes, num_sets), np.inf)

	for set_idx, input_set in enumerate(data):
		for x in input_set:
			for i, (a, b) in enumerate(hash_funcs):
				hash_val = (a * x + b) % max_val
				if hash_val < signature_matrix[i, set_idx]:
					signature_matrix[i, set_idx] = hash_val

	return signature_matrix


data = [{1, 2, 3}, {2, 3, 4}, {1, 4, 5}]
set_A = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}, {4, 5}, {5}]
set_B = [{3, 4}, {4, 5}, {5, 6}, {6, 7}, {3}, {4}, {5}, {6}, {7}]
sets = [set_A, set_B]
num_hash_functions = 3
signature_matrix = minhash_signature_matrix([sets], 3)
print(signature_matrix)