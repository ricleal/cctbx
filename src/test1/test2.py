import common

from cctbx.array_family import flex
from cctbx import miller
from cctbx.development import debug_utils
import sys

from pprint import pprint

def get_all_incides(space_group, abs_range):
  result = {}
  for h0 in xrange(-abs_range, abs_range + 1):
    for h1 in xrange(-abs_range, abs_range + 1):
      for h2 in xrange(-abs_range, abs_range + 1):
        h = (h0, h1, h2)
        if (h == (0, 0, 0)): continue
        equiv = miller.sym_equiv_indices(space_group, h).indices()
        for h_e in equiv:
          h_s = h_e.h()
          assert h_s == h_e.hr()
          result[h_s] = 0
  return flex.miller_index(result.keys())


pprint (get_all_incides("P212121", abs_range=4))
