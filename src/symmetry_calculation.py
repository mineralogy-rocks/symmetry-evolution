# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

from src.utils import get_mineral_cs_tuple, get_mineral_pm_tuple
from src.constants import SYMMETRY_INDICES_DOLIVO_DOBROVOLSKY


mineral_cs_tuple = get_mineral_cs_tuple()
mineral_pm_tuple = get_mineral_pm_tuple()

mineral_cs_pm = mineral_pm_tuple.merge(mineral_cs_tuple, on='mineral_name', how='outer')
mineral_cs_pm.dropna(subset=['paragenetic_mode', 'crystal_system'], inplace=True)
mineral_cs_pm['symmetry_index'] = mineral_cs_pm['crystal_system'].replace(SYMMETRY_INDICES_DOLIVO_DOBROVOLSKY)

pm_symmetry = mineral_cs_pm.groupby('paragenetic_mode').agg(
    symmetry_index=('symmetry_index', lambda x: x.sum() / SYMMETRY_INDICES_DOLIVO_DOBROVOLSKY['cubic'] / x.count()),
    mineral_count=('mineral_name', 'count'),
)
