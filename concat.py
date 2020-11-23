from dipy.io.streamline import load_tractogram, save_tractogram
from dipy.io.stateful_tractogram import Space, StatefulTractogram
import numpy as np

fnA = './ISMRM_2015_Tracto_challenge_ground_truth_bundles_TCK_v2/CST_left.trk'
A = load_tractogram(fnA, 'same')

fnB = './ISMRM_2015_Tracto_challenge_ground_truth_bundles_TCK_v2/CST_right.trk'
B = load_tractogram(fnB, 'same')

A.streamlines.extend(B.streamlines)
concat = StatefulTractogram(A.streamlines, fnA, Space.RASMM)

save_tractogram(concat, 'concat.trk')
