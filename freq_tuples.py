#!/usr/bin/env python
#
# The MIT License (MIT)
#
# Copyright (c) 2013 Brian Lindauer
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from optparse import OptionParser
import fileinput
import sys, os
from sets import Set
from collections import deque, Counter
from itertools import combinations
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk.corpus

import pprint
pp = pprint.PrettyPrinter(indent=4)

parser = OptionParser()

parser.add_option("-w", "--window", dest="window_size", default=3, type="int",
                  help="size of window", metavar="SIZE")

parser.add_option("-t", "--tuple", dest="tuple_size", default=2, type="int",
                  help="size of tuple", metavar="SIZE")

(options, args) = parser.parse_args()

counts = Counter()

stopwords = Set(nltk.corpus.stopwords.words('english'))
try:
  sw_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "extra_stopwords.txt")
  with open(sw_file) as f:
    for w in f.readlines():
      stopwords.add(w.rstrip())
except IOError as err:
  print >> sys.stderr, "Could not open '%s': %s. This is not a big deal unless you meant to define extra stopwords." % (sw_file, err)

for line in fileinput.input(args):
  buf = deque()
  line = line.rstrip()
  for sent in sent_tokenize(line):
    for word in word_tokenize(sent):
      if (word not in stopwords) and (word.isalnum()):
        buf.append(word)
      if (len(buf) > options.window_size):
        buf.popleft()
      for c in combinations(buf, options.tuple_size):
        counts[c] += 1

for k in sorted(counts.keys(), key=lambda x: counts[x], reverse=True):
  print "%s: %d" % (k, counts[k])

sys.exit(0)

