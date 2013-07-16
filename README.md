freq_tuples
===========

This script finds the most common groups of words occurring within a given window in any order. Unless the requested window and tuples sizes are the same, the words need not be contiguous. The purpose here is to answer the question, "Which words most commonly appear near each other?".

## Dependencies

This script depends on NLTK. Do download NLTK, do the following.

    $ pip install nltk

    $ python  
    >> import nltk  
    >> nltk.download('stopwords')  
    >> nltk.download('punkt')  

## Usage information

    $ ./freq_tuples.py --help
    Usage: freq_tuples.py [options]
    
    Options:
      -h, --help            show this help message and exit
      -w SIZE, --window=SIZE
                            size of window
      -t SIZE, --tuple=SIZE
                            size of tuple

By default, English stopwords, using the NLTK list, are filtered out. To add stopwords to this list, you may add them, one per line, to a file called extra_stopwords.txt in the same directory as the script.

## Examples

To find the most common pairs in a window size of 3, run the following.

    $ ./freq_tuples.py --tuple=2 --window=3 my_input_file.txt

These are the default parameters, so you could also simply run

    $ ./freq_tuples.py my_input_file.txt

You may also feed input from STDIN

    $ cat my_input_file.txt | ./freq_tuples.py
