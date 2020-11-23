#############
# Concatenate multiple trk files into a single trk file
#############

from dipy.io.streamline import load_tractogram, save_tractogram
from dipy.io.stateful_tractogram import Space, StatefulTractogram
import numpy as np
from glob import glob

fns = glob('/home/aritche/Desktop/ismrm_2015_tractography_challenge_scoring/ISMRM_2015_Tracto_challenge_ground_truth_bundles_TCK_v2/*.trk')

concat = load_tractogram(fns[0], 'same')
for fn in fns[1:]:
    new_trk = load_tractogram(fn, 'same')
    concat.streamlines.extend(new_trk.streamlines)

tractogram_to_save = StatefulTractogram(concat.streamlines, fns[0], Space.RASMM)
save_tractogram(tractogram_to_save, 'concat.trk')
