#!/usr/bin/env python
# -*- coding:utf-8 -*-

# There are import oderwise
from firehole.algorithms.flashtext import *
from firehole.algorithms.weight import *
from firehole.algorithms.ahp import *
from firehole.algorithms.similarity import *

import firehole.algorithms.flashtext
import firehole.algorithms.weight
import firehole.algorithms.ahp
import firehole.algorithms.similarity

# Need to test with Numpy, when available
# weight
from firehole.algorithms.weight import (Entropy, COV)
from firehole.algorithms.ahp import parse

# Keyword extraction and replace
from firehole.algorithms.flashtext import KeywordProcessor

# calculate the text similarity
from firehole.algorithms.similarity import (BM25Plus, BM25L, BM25Okapi)
from firehole.algorithms.similarity import (Simhash, SimhashIndex)
