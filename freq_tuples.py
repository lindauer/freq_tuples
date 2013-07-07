#!/usr/bin/env python
#
# Copyright (C) 2013 Brian Lindauer
#
#  Licensed under the Apache License, Version 2.0 (the 'License');
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an 'AS IS' BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

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

