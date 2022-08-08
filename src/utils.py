# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd


def get_mineral_cs_tuple() -> pd.DataFrame:
    mineral_attr = pd.read_csv("data/rruff_database_2021_12_25.csv")

    mineral_attr["Crystal Systems"] = mineral_attr["Crystal Systems"].str.replace(
        r", +", "|"
    )
    mineral_attr["Crystal Systems"] = mineral_attr["Crystal Systems"].str.split("|")
    mineral_attr = mineral_attr.explode("Crystal Systems")
    mineral_attr = mineral_attr[mineral_attr["Crystal Systems"] != "unknown"]
    mineral_attr = mineral_attr.dropna(subset="Crystal Systems")
    mineral_attr.rename(
        columns={"Mineral Name": "mineral_name", "Crystal Systems": "crystal_system"},
        inplace=True,
    )

    return mineral_attr[["mineral_name", "crystal_system"]]


def get_mineral_pm_tuple() -> pd.DataFrame:
    mineral_pm = pd.read_csv("data/2021_hazen_pgm.csv")

    mineral_pm.rename(columns={"Mineral Name": "mineral_name"}, inplace=True)
    mineral_pm = mineral_pm.loc[1:, :]
    mineral_pm.set_index("mineral_name", inplace=True)

    pm_columns_ = mineral_pm.columns[mineral_pm.columns.str.match(r"p[0-9]+")]
    mineral_pm[pm_columns_] = mineral_pm[pm_columns_]

    mineral_pm["p45"] = mineral_pm[["p45a", "p45b"]].any(axis=1)
    mineral_pm["p47"] = mineral_pm[
        ["p47a", "p47b", "p47c", "p47d", "p47e", "p47f", "p47g", "p47h", "p47i"]
    ].any(axis=1)
    mineral_pm[["p45", "p47"]] = mineral_pm[["p45", "p47"]].replace(False, np.nan)
    mineral_pm[["p45", "p47"]] = mineral_pm[["p45", "p47"]].replace(True, 1.0)
    mineral_pm = mineral_pm[
        mineral_pm.columns[mineral_pm.columns.str.match(r"p[0-9]+$")]
    ]

    mineral_pm_tuple = mineral_pm.stack()
    mineral_pm_tuple = mineral_pm_tuple.reset_index().rename(
        columns={"level_1": "paragenetic_mode"}
    )
    mineral_pm_tuple = mineral_pm_tuple[["mineral_name", "paragenetic_mode"]]

    return mineral_pm_tuple
