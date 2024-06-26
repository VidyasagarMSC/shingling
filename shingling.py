# Shingling.py

import argparse


def main(argv):
    # Define arguments
    parser = argparse.ArgumentParser(description="Pass two sentences...")
    parser.add_argument(
        "text_a",
        type=str,
        help="text 1 to create shingles",
    )
    parser.add_argument(
        "text_b",
        type=str,
        help="text 2 to create shingles and compare for similarity.",
    )
    parser.add_argument(
        "-k",
        type=int,
        default=5,
        help="the size of shingles",
    )

    args = parser.parse_args(argv[1:])

    try:
        similarity_score = compute_jaccard_similarity(args.text_a, args.text_b, args.k)
        print(f"Jaccard Similarity: {similarity_score:.4f}")
    except Exception as err:
        print(err)
        parser.print_help()


def create_shingles(text, k=5):
    """Generates a set of shingles for given text."""
    return set(text[i: i + k] for i in range(len(text) - k + 1))


def compute_jaccard_similarity(text_a, text_b, k):
    """Calculates the Jaccard similarity between two shingle sets."""
    shingles_a = create_shingles(text_a.lower(), k)
    print("Shingles for text_a is ", shingles_a)
    shingles_b = create_shingles(text_b.lower(), k)
    print("Shingles for text_b is ", shingles_b)
    intersection = len(shingles_a & shingles_b)
    union = len(shingles_a | shingles_b)
    print("Intersection - text_a ∩ text_b: ", intersection)
    print("Union - text_a ∪ text_b: ", union)
    return intersection / union


if __name__ == "__main__":
    import sys
    main(sys.argv)