# Code for Shingling

The repository contains code for creating Shingles (set of words) and to calculate Jaccard Similarity between two generated Shingles.

## Usage 

### Jaccard Similarity
```sh
usage: shingling.py [-h] [-k K] test_a test_b

Pass two sentences...

positional arguments:
  text_a      text 1 to create shingles
  text_b      text 2 to create shingles and compare for similarity.

optional arguments:
  -h, --help  show this help message and exit
  -k K        the size of shingles
```

### Weighted Shingling

```commandline
usage: weighted-shingling.py [-h] [-k K] text weights

Pass a text sentence with size and weights...

positional arguments:
  text        The input text.
  weights     A dictionary mapping words to their weights in string format.

optional arguments:
  -h, --help  show this help message and exit
  -k K        The length of shingles.

```

## Example

### Jaccard Similarity
```sh
$ python3 shingling.py "Generates a set of shingles for given text." "Generates a set of shingles." -k 5

Shingles for text_a is  {'es a ', 'rates', 'iven ', ' of s', 'given', 'a set', ' set ', 'n tex', ' for ', 'les f', 'gener', 's a s', 't of ', ' shin', 'en te', 'nerat', 'shing', 'ingle', 'of sh', 'or gi', 'tes a', 'for g', 'ven t', 'set o', 'enera', 'text.', 's for', ' give', 'ngles', 'ates ', 'r giv', ' a se', 'es fo', 'erate', 'et of', 'hingl', ' text', 'gles ', 'f shi'}
Shingles for text_b is  {'es a ', 'rates', ' of s', 'gles.', 'a set', ' set ', 'gener', 's a s', 't of ', ' shin', 'nerat', 'shing', 'ingle', 'of sh', 'tes a', 'set o', 'enera', 'ngles', 'ates ', ' a se', 'erate', 'et of', 'hingl', 'f shi'}
Intersection - text_a ∩ text_b 23
Union - text_a ∪ text_b 40
Jaccard Similarity: 0.5750
```

### Weighted shingling 

```commandline
$ python3 weighted-shingling.py "This is a sample text with some important words like neural networks and deep learning" '{"neural": 2, "deep": 2, "networks": 1.5, "learning": 1.5}' -k 5
{'neural': 2, 'deep': 2, 'networks': 1.5, 'learning': 1.5}


List of Shingles with corresponding weights:  [('this is a sample text', 5), ('is a sample text with', 5), ('a sample text with some', 5), ('sample text with some important', 5), ('text with some important words', 5), ('with some important words like', 5), ('some important words like neural', 6), ('important words like neural networks', 6.5), ('words like neural networks and', 6.5), ('like neural networks and deep', 7.5), ('neural networks and deep learning', 8.0)]
```


