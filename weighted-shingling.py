import re
import argparse
import json


def main(argv):
	# Define arguments
	parser = argparse.ArgumentParser(description="Pass a text sentence with size and weights...")
	parser.add_argument(
		"text",
		type=str,
		help="The input text.",
	)
	parser.add_argument(
		"weights",
		type=str,
		help="A dictionary mapping words to their weights in string format.",
	)
	parser.add_argument(
		"-k",
		type=int,
		default=5,
		help="The length of shingles.",
	)

	args = parser.parse_args(argv[1:])

	try:
		print(json.loads(args.weights))
		weighted_shingles = generate_weighted_shingles(args.text, json.loads(args.weights), args.k)
		print("List of Shingles with corresponding weights: ", weighted_shingles)
	except Exception as err:
		print(err)
		parser.print_help()


def generate_weighted_shingles(text, weights, k):
	"""
	Generate weighted shingles of length k from the given text.

	Args:
		text (str): The input text.
		k (int): The length of shingles.
		weights (dict): A dictionary mapping words to their weights.

	Returns:
		list: A list of weighted shingles.
	"""
	# Tokenize the text into words
	words = re.findall(r'\w+', text.lower())

	# Generate all shingles of length k
	shingles = [' '.join(words[i:i + k]) for i in range(len(words) - k + 1)]

	# Compute the weight of each shingle
	weighted_shingles = []
	for shingle in shingles:
		shingle_words = shingle.split()
		shingle_weight = sum(weights.get(word, 1) for word in shingle_words)
		weighted_shingles.append((shingle, shingle_weight))

	return weighted_shingles


if __name__ == "__main__":
	import sys
	main(sys.argv)
