# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from src.constants import SYMMETRY_INDICES_DOLIVO_DOBROVOLSKY
from src.utils import get_mineral_cs_tuple, get_mineral_pm_tuple, get_pm_attrs

FEATURES = [
    "MODE",
    "Mode Description",
    "STAGE (min)",
    "STAGE (max)",
    "AGE (average) Ga",
    "DUR (min) log Yr",
    "DUR (max) log Yr",
    "DUR (average log Yr)",
    "ChemIG Atom",
    "ChemIG Total",
    "StrIG Atom",
    "StrIG Total",
    "Hardness (HoM)",
    "Hardness (Web Max)",
    "Hardness (Average)",
    "Calc Density (gm/cm3)",
    "Web Density (gm/cm3)",
    "Density (Average)",
    "temperature",
    "pressure",
    "symmetry_index",
    "mineral_count",
    "# Elements",
]

mineral_cs_tuple = get_mineral_cs_tuple()
mineral_pm_tuple = get_mineral_pm_tuple()
pm_attrs = get_pm_attrs()

mineral_cs_pm = mineral_pm_tuple.merge(mineral_cs_tuple, on="mineral_name", how="outer")
mineral_cs_pm.dropna(subset=["paragenetic_mode", "crystal_system"], inplace=True)
mineral_cs_pm["symmetry_index"] = mineral_cs_pm["crystal_system"].replace(
    SYMMETRY_INDICES_DOLIVO_DOBROVOLSKY
)

pm_symmetry = mineral_cs_pm.groupby("paragenetic_mode").agg(
    symmetry_index=(
        "symmetry_index",
        lambda x: x.sum() / SYMMETRY_INDICES_DOLIVO_DOBROVOLSKY["cubic"] / x.count(),
    ),
    mineral_count=("mineral_name", "count"),
)

pm_symmetry = pm_symmetry.merge(pm_attrs, left_on="paragenetic_mode", right_on="MODE")

pm_symmetry["temperature"] = pm_symmetry.apply(
    lambda x: np.arange(x["Temp (min) K"], x["Temp (max) K"] + 1, 1), axis=1
)
pm_symmetry["pressure"] = pm_symmetry.apply(
    lambda x: np.arange(x["P (min) log Pa"], x["P (max) log Pa"] + 1, 1), axis=1
)

pm_symmetry = pm_symmetry.explode("temperature")
pm_symmetry = pm_symmetry.explode("pressure")
pm_symmetry[["temperature", "pressure"]] = pm_symmetry[
    ["temperature", "pressure"]
].astype(int)

correlation_pearson = pm_symmetry[FEATURES].corr(method="pearson")
sns.set_theme(style="ticks", font_scale=0.75)
g = sns.heatmap(correlation_pearson, annot=True, fmt=".2", cmap=plt.cm.Reds)
g.figure.set_size_inches(10, 8)
plt.savefig("figures/heatmap/pm_pt_symmetry.jpeg", dpi=500, format="jpeg")
plt.close()
