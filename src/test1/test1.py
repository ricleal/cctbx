import common

from cctbx import miller
from cctbx import crystal
from cctbx import sgtbx

from pprint import pprint

ms = miller.build_set(
   crystal_symmetry=crystal.symmetry(
     space_group_symbol="P212121",
     unit_cell=(6, 6, 6, 90, 90, 90)),
   anomalous_flag=False,
   d_min=3.0)
print ms.size()

s = sgtbx.space_group("P 31")
h = (10, 10, 10)
e = miller.sym_equiv_indices(s,h)
#pprint(list(e.indices()))
pprint(dir(e))

print e.indices()