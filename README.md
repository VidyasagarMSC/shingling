# Code for Shingling

The repository contains code for creating Shingles (set of words) and to calculate Jaccard Similarity between two generated Shingles.

## Usage 
```sh
usage: shingling.py [-h] [-k K] test_a test_b

Pass two sentences...

positional arguments:
  test_a      String 1 to create shingles
  test_b      The field of generative AI evolves swiftly.

optional arguments:
  -h, --help  show this help message and exit
  -k K        the size of shingles
```

## Example

```sh
$ python3 shingling.py "Generates a set of shingles for given text." "Generates a set of shingles." -k 5

Shingles for text_a is  {'es a ', 'rates', 'iven ', ' of s', 'given', 'a set', ' set ', 'n tex', ' for ', 'les f', 'gener', 's a s', 't of ', ' shin', 'en te', 'nerat', 'shing', 'ingle', 'of sh', 'or gi', 'tes a', 'for g', 'ven t', 'set o', 'enera', 'text.', 's for', ' give', 'ngles', 'ates ', 'r giv', ' a se', 'es fo', 'erate', 'et of', 'hingl', ' text', 'gles ', 'f shi'}
Shingles for text_b is  {'es a ', 'rates', ' of s', 'gles.', 'a set', ' set ', 'gener', 's a s', 't of ', ' shin', 'nerat', 'shing', 'ingle', 'of sh', 'tes a', 'set o', 'enera', 'ngles', 'ates ', ' a se', 'erate', 'et of', 'hingl', 'f shi'}
Intersection - text_a ∩ text_b 23
Union - text_a ∪ text_b 40
Jaccard Similarity: 0.5750
```