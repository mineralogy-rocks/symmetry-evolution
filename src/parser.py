# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd

rruff = pd.read_csv("data/input/rruff_point_space_group.csv")
rruff = rruff.replace("\xa0", np.nan)
rruff = rruff.dropna(subset=["point group", "space group"])
rruff.drop_duplicates(inplace=True)

rruff.to_csv("data/output/rruff_pg_sg_ungrouped.csv")

rruff = rruff.groupby("mineral name").agg(
    {"point group": "; ".join, "space group": "; ".join}
)
rruff.to_csv("data/output/rruff_pg_sg_grouped.csv")
