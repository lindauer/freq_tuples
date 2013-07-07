freq_tuples
===========

Find the most frequently occurring word tuples (not necessarily adjacent) in a text file.

This script depends on NLTK. Do download NLTK, do the following.

$ pip install nltk

$ python
&gt;&gt; import nltk
&gt;&gt; nltk.download('stopwords')
&gt;&gt; nltk.download('punkt')


$ ./freq_tuples.py --help
Usage: freq_tuples.py [options]

Options:
  -h, --help            show this help message and exit
  -w SIZE, --window=SIZE
                        size of window
  -t SIZE, --tuple=SIZE
                        size of tuple

To find the most common pairs in a window size of 3, run the following.

$ ./freq_tuples.py --tuple=2 --window=3 my_input_file.txt

These are the default parameters, so you could also simply run

$ ./freq_tuples.py my_input_file.txt

You may also feed input from STDIN

$ cat my_input_file.txt | ./freq_tuples.py
