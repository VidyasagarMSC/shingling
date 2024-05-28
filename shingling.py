# Shingling.py

def create_shingles(text, k=3):
	"""Generates a set of shingles for given text."""
	return set(text[i:i + k] for i in range(len(text) - k + 1))


def compute_jaccard_similarity(set1, set2):
	"""Calculates the Jaccard similarity between two shingle sets."""
	intersection = len(set1 & set2)
	union = len(set1 | set2)
	print(intersection)
	print(union)
	return intersection / union


text_a = "Generative AI is evolving rapidly."
text_b = "The field of generative AI evolves swiftly."

# Generate shingles
shingles_a = create_shingles(text_a.lower(), 5)
print(shingles_a)

shingles_b = create_shingles(text_b.lower(), 5)
print(shingles_b)

# Compute similarity
similarity_score = compute_jaccard_similarity(shingles_a, shingles_b)
print(f"Jaccard Similarity: {similarity_score:.4f}")


